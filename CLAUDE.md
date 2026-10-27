# Claude Guidelines

## Before Starting Work

**Always run `git pull` first** - The production server automatically scrapes Apple docs on a schedule. Your local repo may be out of date with new documentation files.

## Git Commit Rules

**NEVER commit without explicit written permission** - Only commit when the user explicitly asks with phrases like "commit this", "push these changes", or "git commit". Never assume permission to commit.

**NEVER add Claude attribution to commits** - Do not include "Co-Authored-By: Claude" or any other attribution. Keep commits simple with just the message.

## Deployment Testing

**Public server:** https://xdocs.dev/mcp

```bash
# Test health endpoint (returns real-time Meilisearch stats)
curl https://xdocs.dev/health

# Test MCP endpoint
curl -X POST https://xdocs.dev/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}'
```

**Server details:**
- URL: `https://xdocs.dev/mcp`
- Transport: Streamable HTTP (native MCP)
- Rate Limit: 60 req/min per IP (bypassed with API key)
- Host allow-list: `ALLOWED_HOSTS` env, default `xdocs.dev,www.xdocs.dev` (localhost always allowed; any other Host header gets 421 from fastmcp's guard)

**VPS layout:**
- MCP server: `~/apple-dev-docs/mcp-server/`
- Landing page served from: `/var/www/xdocs/`
- Caddy config: `~/caddy/Caddyfile`
- Caddy docker-compose: `~/caddy/docker-compose.yml`
- Caddy needs volume mount: `/var/www/xdocs:/var/www/xdocs:ro`

**Health endpoint status codes:**
- `200 OK` with `status: healthy` - Ready for use (400K+ docs indexed)
- `503 Service Unavailable` with `status: indexing` - The live index was just updated: an incremental update, or a rebuild's swap (<3.5 min after its last add); it serves every search. A rebuild in progress never shows as `indexing`: `/health` reports only the live `apple-docs` index, with its old `documents` count, until the swap
- `503 Service Unavailable` with `status: degraded` - Partial index (<363K docs); on a fresh volume, 0 docs until its first build is renamed in
- `503 Service Unavailable` with `status: unhealthy` - Meilisearch unavailable

**Container healthcheck:** Docker health curls the MCP app itself (`localhost:$HTTP_PORT/health`) with `Host: ${ALLOWED_HOSTS%%,*}`, so app-level failures (e.g. Host header rejection) show as `unhealthy` in `docker ps`. A rebuild over a live index doesn't turn the container unhealthy (it is built beside the live index and swapped in); only the short `indexing` window after an update or a swap can. A fresh volume's first build still does, since there is no live index yet: 0 docs, `degraded` (503) until the rename-swap and through the short `indexing` window after it — that's intentional, not a bug.

**Health endpoint timestamps:**
- `docs_updated` - When docs were last changed (last git commit to `documentation/`, set at image build time)
- `last_indexed` - When Meilisearch indexing last completed
- `last_index_full` - When the last full rebuild was swapped in
- `image_built` - When Docker image was created

## Docker ENV Gotcha

**IMPORTANT:** When changing default values, update ALL locations:
1. Python code: `os.getenv("VAR", "default")` - only used if env var not set
2. `Dockerfile`: `ENV VAR=value` - baked into image, overrides Python default
3. `docker-compose.yml`: `VAR=${VAR:-default}` - runtime override
4. `.env.example`: documentation for users

Docker ENV takes precedence over Python defaults. If you change a default in Python but not in Dockerfile, the old value persists.

## Auto-Deploy Behavior

GitHub Actions deploys via `docker compose pull && docker compose up -d --remove-orphans --force-recreate`: the old container keeps serving while the image downloads, then it is **recreated** (~10-20 s outage).

On every start, `startup_check.py` runs the indexer, and the live `apple-docs` index keeps serving every search:
- **Incremental update** (the usual deploy): new and changed docs are added first, then the documents they no longer have and those of removed docs are deleted by `file_path` (add-then-sweep, by `index_gen`). A start with no doc changes queues no task on the live index (settings are applied only where they differ), so `/health` stays 200
- **Rebuild by swap** when one is due: no live index yet (fresh volume), a new `PROCESSOR_VERSION`, a hash file that doesn't describe the live index (`meilisearch_hashes.json` records the `createdAt` of the index its hashes belong to), an older indexer has run on the live index (a rollback: older indexers drop `index_gen` from its filterable attributes and only add, leaving stale documents), 6.5 days since the live index was built (UTC, from its `createdAt`), the live index lacking a filterable, sortable or searchable attribute the indexer's settings name (a new indexed field), or more than 25% of the files changed. The new index is built in `apple-docs-build` (~15-20 min on Meilisearch v1.49) and swapped in atomically, so disk peaks at two indexes: ~9.6 GB (one full index takes ~4.8 GB on disk; `/stats` `usedDatabaseSize` says ~3.1 GB), plus the ~2.5 GB image
- **Disk check:** a full disk would crash Meilisearch (SIGBUS) and keep it from starting again while the unfinished build fills the disk, so over a live index the indexer starts a rebuild only with 1.2× the database's size on disk + 1 GiB free on `/data/meilisearch` (~6.8 GB today), and stops it (deleting `apple-docs-build`) if free space falls under 1 GiB between two batches. The log shows `✓ Disk: …` or the shortfall
- **A due rebuild that fails before its swap, or isn't started for lack of disk,** leaves the live index serving; the same run then applies the incremental update to it (after waiting up to 2 min for Meilisearch to answer again, if it crashed or was OOM-killed mid-build: supervisord restarts it), records the rebuild as still due in the hash file (`rebuild_due`) and exits 1, and every start retries the rebuild until one succeeds (`last_index_full` moves). New docs and Apple's removals keep reaching search meanwhile. After a rollback, that update also re-indexes the files the older indexer added documents for, so their stale documents don't wait for the rebuild
- **Image completeness:** docker-build bakes the checkout's `.md` count into the image (`DOC_FILE_COUNT`). An image holding another count is truncated: the indexer swaps, adds and deletes nothing, exits 1, and the live index keeps serving. Local builds carry no count and fall back to requiring 90% of the live index's size

**If a deploy happens during indexing:** the container is destroyed mid-run, and the live index is never left partial. A rebuild was going into `apple-docs-build`: the next start deletes it and rebuilds by swap again (its hash file still describes the old index). An update saved no new hashes, but it recorded the docs it was sending as pending in the hash file before its first add: the next start sends them again, or deletes their documents if they were removed since.

**Scrape schedule:** Tue/Fri at 2:07 AM EST (7:07 AM UTC), triggered via VPS cron

**Meilisearch volume:** Production data lives in the `meilisearch_v149` named volume (renamed from `meilisearch` for the v1.33→v1.49 engine upgrade — a Meilisearch database is only readable by the version that created it, so engine upgrades need a fresh volume + full reindex; the old volume is kept for rollback until the new one has served traffic).

## Rate Limiting Notes

Each MCP tool call generates ~4 HTTP requests (protocol overhead). Claude Desktop can make 8-10 tool calls in rapid bursts when searching. At 60 req/min:
- Normal usage: ~15 tool calls/min = fine
- Aggressive bursts: 10 calls in 30 seconds = ~40 requests = fine
- Very heavy usage: may still hit limit

If issues persist, consider:
- Increasing to 100-120 req/min
- Using API key for unlimited access (set `MCP_API_KEY` env var)

## Project Overview

MCP server for Apple Developer Documentation with Meilisearch backend. 400+ frameworks and modules, 400K+ documents, ~16 ms median search.

## Critical Rules

- **NEVER blame external services** (Claude, Anthropic, Google, Reddit, etc.) for issues. If something isn't working, the problem is in THIS codebase. Investigate our code first, add logging, and find the real cause. Blaming external parties wastes time.
- **NEVER create mock data** unless explicitly told to
- **NEVER replace existing code with simplified versions** - fix the actual problem
- **ALWAYS find root cause** - don't create workarounds
- **NEVER dismiss issues as "pre-existing"** - All issues must be fixed when discovered. No issue is someone else's problem. If you find a bug during unrelated work, fix it or flag it clearly — never wave it away as "pre-existing" or "out of scope"
- **NEVER SUGGEST SPECIAL HANDLING FOR SPECIFIC PATTERNS** - 400+ frameworks means no special cases
- Update existing files, don't create new ones unless necessary
- Use relative paths in scripts
- Follow MCP spec from https://modelcontextprotocol.io/specification/

## Web Fetching

**CRITICAL: NEVER use WebFetch directly. ALWAYS use fetchaller first.**
Load via `ToolSearch("fetchaller")` then use `mcp__fetchaller__fetch`. It has no domain restrictions.
Add `raw: true` for raw HTML instead of markdown. If raw:true fails, use `curl` via Bash as fallback.
Only fall back to WebFetch if fetchaller fails entirely.
If a dedicated MCP exists (GitHub, Slack, etc.), use that instead.

## Reddit Searching and Browsing

Load via `ToolSearch("fetchaller")` first. Use `mcp__fetchaller__browse_reddit` to browse subreddits, `mcp__fetchaller__search_reddit` to find posts, and `mcp__fetchaller__fetch` to read full discussions.

## Python Environment

Python is managed via **uv** (see `~/Code/CLAUDE.md` for global setup).

```bash
# Create venv and install dependencies: the MCP server, the indexer and mcp-server/tests
# run on Python 3.11 with both files, as in the Docker image
uv venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt -r mcp-server/requirements.txt

# The scrapers and the tests in tests/ and scripts/tests/ run on Python 3.12, as the
# scheduled scrape workflow does: scripts/scrape_mlx_docs.py needs wafer-py
# (requirements-scrape.txt, scrape workflow only); without it its tests
# (scripts/tests/test_scrape_mlx_docs.py) are skipped
uv venv --python 3.12 .venv-scrape
source .venv-scrape/bin/activate
uv pip install -r requirements.txt -r requirements-scrape.txt
```

## Python Standards

- Python 3.11+ with type hints
- PEP 8 style
- asyncio for concurrent operations
- Proper logging (not print)
- Run mypy before considering complete

## Security

- API keys in environment variables only
- Never hardcode keys
- Use `.env` file (gitignored) for local dev

## Architecture

- **Scraper**: Uses Apple's JSON API (not HTML)
- **Nested modules** (D6): a module Apple nests under an umbrella (Intents under SiriKit, simd under Accelerate) gets its own `documentation/<Module>/` dir and hash file (`metadata.module` records its parents); it's removed automatically when no parent links it any more. `scraper/site.py` (`DocCSite`) and `scraper/sink.py` (`Sink`/`SinkRegistry`) route each page to its dir
- **Search**: Meilisearch (~16 ms median search on the full index; engine version pinned in `mcp-server/Dockerfile`, Python client pinned in both requirements files — keep them matched)
- **MCP Server**: FastMCP with Streamable HTTP transport
- **Indexing**: ~15-20 minutes for 322K+ documents on Meilisearch v1.49 (measured in production 2026-07-07; was ~2 hours on v1.33)

## Core Commands

```bash
# Scrape Apple framework docs and the DocC sites (docs.swift.org, the SPI packages)
python scrape.py --all --yes

# Only some DocC sites (names in scraper/site.py: swift-org, spi-carekit, spi-swift-log, ...)
python scrape.py --sites swift-org spi-carekit --yes

# Scrape Swift language docs (from GitHub)
python scripts/scrape_swift_docs.py

# Scrape Human Interface Guidelines (HIG)
python scripts/scrape_hig_docs.py

# Scrape MLX, CoreML Tools, the other Sphinx/GitHub docs and the App Store pages
python scripts/scrape_mlx_docs.py

# Index to Meilisearch
cd scripts && python index_to_meilisearch.py

# Run MCP server
cd mcp-server && python apple_docs_mcp.py

# Docker deployment
cd mcp-server && docker-compose up -d
```

## Production Debugging

```bash
# View MCP server logs (on production server)
docker exec apple-docs-mcp cat /data/logs/mcp-server.log | tail -200

# View Meilisearch logs
docker exec apple-docs-mcp cat /data/logs/meilisearch.log | tail -100

# Follow logs in real-time
docker exec apple-docs-mcp tail -f /data/logs/mcp-server.log

# Check container status
docker ps | grep apple-docs

# Indexer output of the last start (its mode: incremental update or rebuild by swap, and why)
docker exec apple-docs-mcp tail -50 /data/logs/startup-check.log

# Check the live index (real-time stats from Meilisearch)
docker exec apple-docs-mcp sh -c 'curl -s -H "Authorization: Bearer $MEILI_MASTER_KEY" localhost:7700/indexes/apple-docs/stats'

# Check a rebuild's progress (the new index, built beside the live one until the swap)
docker exec apple-docs-mcp sh -c 'curl -s -H "Authorization: Bearer $MEILI_MASTER_KEY" localhost:7700/indexes/apple-docs-build/stats'

# Redeploy with latest image
docker pull ghcr.io/averyy/apple-dev-docs:latest
docker stop apple-docs-mcp && docker rm apple-docs-mcp
# Then run docker-compose up -d or your docker run command
```

**Note:** The `/health` endpoint returns real-time stats from Meilisearch (not cached), for the live index only: during a rebuild it shows the old live `documents` count (the rebuild's progress is in `apple-docs-build`'s stats, above), and on a fresh volume 0 docs (`degraded`) until the first build is renamed in.

## Document Count Discrepancy

The landing page and health API show slightly different document counts - this is expected:

- **Landing page** (`find` count): Number of markdown files on disk (~403.2K)
- **Health API** (Meilisearch count): Number of indexed documents (~403.7K)

The difference (~490) is because `DocumentProcessor` chunks large files (>50KB) into multiple Meilisearch documents, each with its own id (`<sha1 of file_path>_chunk_<n>`; an unchunked file's id is the bare sha1): on 2026-10-26 the 98 files over 50KB gave 592 documents, 403,243 files 403,737. One markdown file can produce multiple indexed documents. This is intentional for search performance.

## Local Testing

Run locally with a separate compose file (3GB memory limit for stress testing; builds the host's native architecture — the amd64 Meilisearch release binary segfaults under QEMU emulation on Apple Silicon):

```bash
cd mcp-server
docker compose -f docker-compose.local.yml up --build
```

A plain local build leaves `DOC_FILE_COUNT` empty, so the indexer falls back to the 90%-of-the-live-index check. To build as docker-build does (the count gates every production swap and delete), pass it to `build`, then start without `--build`, which would drop it:
```bash
docker compose -f docker-compose.local.yml build --build-arg DOC_FILE_COUNT=$(find ../documentation -name '*.md' | wc -l | xargs)
docker compose -f docker-compose.local.yml up -d
```

Monitor progress:
```bash
# Memory usage
docker stats apple-docs-mcp-local --no-stream --format "{{.MemUsage}}"

# Live index (during a rebuild, its old count until the swap)
curl -s http://localhost:8001/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d.get('documents',0):,} docs ({d.get('status','?')})\")"

# A rebuild's progress
docker exec apple-docs-mcp-local sh -c 'curl -s -H "Authorization: Bearer $MEILI_MASTER_KEY" localhost:7700/indexes/apple-docs-build/stats'
```

Search eval, once the index is complete: scores `search_apple_docs` on the golden queries (`mcp-server/tests/golden_queries.json`, expectations keyed by canonical URL) by hit@3 and MRR, and `expand_result`'s symbol lookups (entries with `"expand": true`) by expand@1. It runs on the host, from the repo root, since it resolves the expectations through `.hashes` and `documentation/`:
```bash
python scripts/tests/eval_search.py                        # http://localhost:8001/mcp, Bearer test123
python scripts/tests/eval_search.py --save /tmp/eval.json  # also records the per-query results
```

Clean up:
```bash
docker compose -f docker-compose.local.yml down -v  # -v removes volumes
```

## Landing Page & SKILL.md

**`landing/SKILL.md` is the only copy of the skill.** Edit it there and nowhere else: `landing/index.html` fills both skill blocks (Claude Code tab `id="claude-skills"`, Claude Desktop tab `id="desktop-skills"`, marked `data-skill`) with `fetch('/SKILL.md')` at page load, their Copy buttons copy the fetched text, and both tabs link to it for download. The deploy copies `landing/` to the web root, so the page and `https://xdocs.dev/SKILL.md` always show the same file. Never paste the skill text into `index.html`.

**SKILL.md rules** (per Anthropic docs):
- Description must be **third person** ("Searches..." not "Search...")
- MCP tools use **fully qualified names**: `apple-docs:search_apple_docs`
- Don't include stateful tools that don't persist over HTTP

## Project Structure

```
apple-dev-docs/
├── scrape.py                      # Apple frameworks + the DocC sites (docs.swift.org, SPI packages) scraper
├── scraper/site.py, scraper/sink.py  # DocCSite configs; Sink/SinkRegistry route pages to their docs dir (modules, sites)
├── documentation/                 # Scraped markdown files
│   ├── HIG/                      # Human Interface Guidelines (design docs)
│   ├── Swift-Book/               # Swift language docs (from GitHub)
│   ├── MLX/, MLX-Swift/, coremltools/  # MLX & CoreML Tools docs
│   ├── apple-fm-sdk/, container/, sourcekit-lsp/, swift-format/, game-porting-toolkit/  # other Apple Sphinx/GitHub docs
│   ├── App-Store/                # App Store Review Guidelines and privacy pages
│   ├── Swift-Org/<Root>/         # docs.swift.org DocC site (migration guide, SwiftPM, Embedded Swift, DocC…)
│   └── SPI/<package>/<Module>/   # Swift Package Index packages (CareKit, MLX Swift, swift-log, …)
├── scripts/
│   ├── index_to_meilisearch.py   # Indexer
│   ├── scrape_swift_docs.py      # Swift language docs scraper
│   ├── scrape_hig_docs.py        # Human Interface Guidelines scraper
│   └── scrape_mlx_docs.py        # MLX, CoreML Tools, other Sphinx/GitHub docs and App Store pages scraper
├── mcp-server/
│   ├── apple_docs_mcp.py         # Native HTTP MCP server
│   ├── docker-compose.yml        # Docker deployment
│   └── Dockerfile
└── landing/
    ├── index.html                # xdocs.dev landing page
    └── SKILL.md                  # Claude Code skill file (the only copy; index.html loads it)
```
