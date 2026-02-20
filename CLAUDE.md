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

**Health endpoint status codes:**
- `200 OK` with `status: healthy` - Ready for use (335K+ docs indexed)
- `200 OK` with `status: indexing` - Index building (check `documents` and `progress`)
- `503 Service Unavailable` with `status: degraded` - Partial index (<300K docs)
- `503 Service Unavailable` with `status: unhealthy` - Meilisearch unavailable

**Health endpoint timestamps:**
- `last_docs_change` - When docs were last updated (most recent file mtime)
- `last_index_full` - When Meilisearch full rebuild ran
- `image_built` - When Docker image was created

## Docker ENV Gotcha

**IMPORTANT:** When changing default values, update ALL locations:
1. Python code: `os.getenv("VAR", "default")` - only used if env var not set
2. `Dockerfile`: `ENV VAR=value` - baked into image, overrides Python default
3. `docker-compose.yml`: `VAR=${VAR:-default}` - runtime override
4. `.env.example`: documentation for users

Docker ENV takes precedence over Python defaults. If you change a default in Python but not in Dockerfile, the old value persists.

## Auto-Deploy Behavior

GitHub Actions deploys via `docker compose down && docker compose up -d`, which **recreates the container**.

**Important:** If deploy happens during indexing:
1. Container is destroyed mid-indexing
2. New container starts with low doc count
3. `startup_check.py` sees <90% of expected docs (needs ~301K to skip rebuild)
4. Full rebuild triggers (~2 hours for 335K docs)

Once index completes (335K+ docs), subsequent deploys will be fast (incremental updates only).

**Scrape schedule:** Tue/Fri at 2:07 AM EST (7:07 AM UTC), triggered via VPS cron

## Rate Limiting Notes

Each MCP tool call generates ~4 HTTP requests (protocol overhead). Claude Desktop can make 8-10 tool calls in rapid bursts when searching. At 60 req/min:
- Normal usage: ~15 tool calls/min = fine
- Aggressive bursts: 10 calls in 30 seconds = ~40 requests = fine
- Very heavy usage: may still hit limit

If issues persist, consider:
- Increasing to 100-120 req/min
- Using API key for unlimited access (set `MCP_API_KEY` env var)

## Project Overview

MCP server for Apple Developer Documentation with Meilisearch backend. 370+ frameworks, 334K+ documents, sub-3ms search.

## Critical Rules

- **NEVER blame external services** (Claude, Anthropic, Google, Reddit, etc.) for issues. If something isn't working, the problem is in THIS codebase. Investigate our code first, add logging, and find the real cause. Blaming external parties wastes time.
- **NEVER create mock data** unless explicitly told to
- **NEVER replace existing code with simplified versions** - fix the actual problem
- **ALWAYS find root cause** - don't create workarounds
- **NEVER dismiss issues as "pre-existing"** - All issues must be fixed when discovered. No issue is someone else's problem. If you find a bug during unrelated work, fix it or flag it clearly — never wave it away as "pre-existing" or "out of scope"
- **NEVER SUGGEST SPECIAL HANDLING FOR SPECIFIC PATTERNS** - 370+ frameworks means no special cases
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
# Create venv and install dependencies
uv venv --python 3.11
source .venv/bin/activate
uv pip install -r requirements.txt
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
- **Search**: Meilisearch (<3ms latency)
- **MCP Server**: FastMCP with Streamable HTTP transport
- **Indexing**: ~2 hours for 335K+ documents (streaming batches)

## Core Commands

```bash
# Scrape Apple framework docs
python scrape.py --all --yes

# Scrape Swift language docs (from GitHub)
python scripts/scrape_swift_docs.py

# Scrape Human Interface Guidelines (HIG)
python scripts/scrape_hig_docs.py

# Scrape MLX & CoreML Tools docs
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

# Check indexing progress (real-time stats from Meilisearch)
docker exec apple-docs-mcp curl -s localhost:7700/indexes/apple_docs/stats

# Redeploy with latest image
docker pull ghcr.io/averyy/apple-dev-docs:latest
docker stop apple-docs-mcp && docker rm apple-docs-mcp
# Then run docker-compose up -d or your docker run command
```

**Note:** The `/health` endpoint returns real-time stats from Meilisearch (not cached). Use it to check `documents` and `is_indexing` status.

## Document Count Discrepancy

The landing page and health API show slightly different document counts - this is expected:

- **Landing page** (`find` count): Number of markdown files on disk (~334K)
- **Health API** (Meilisearch count): Number of indexed documents (~334.3K)

The difference (~300-400) is because `DocumentProcessor` chunks large files (>50KB) into multiple Meilisearch documents. One markdown file can produce multiple indexed documents. This is intentional for search performance.

## Local Testing

Run locally with a separate compose file (2GB memory limit for stress testing):

```bash
cd mcp-server
docker compose -f docker-compose.local.yml up --build
```

Monitor progress:
```bash
# Memory usage
docker stats apple-docs-mcp-local --no-stream --format "{{.MemUsage}}"

# Indexing progress
curl -s http://localhost:8001/health | python3 -c "import sys,json; d=json.load(sys.stdin); print(f\"{d.get('documents',0):,} docs ({d.get('progress','?')})\")"
```

Clean up:
```bash
docker compose -f docker-compose.local.yml down -v  # -v removes volumes
```

## Landing Page & SKILL.md

**IMPORTANT:** When updating the SKILL.md content, update ALL THREE locations:
1. `landing/SKILL.md` - standalone file for download/reference
2. `landing/index.html` - Claude Code tab (search for `id="claude-skills"`)
3. `landing/index.html` - Claude Desktop tab (search for `id="desktop-skills"`)

**SKILL.md rules** (per Anthropic docs):
- Description must be **third person** ("Searches..." not "Search...")
- MCP tools use **fully qualified names**: `apple-docs:search_apple_docs`
- Don't include stateful tools that don't persist over HTTP

## Project Structure

```
apple-dev-docs/
├── scrape.py                      # Apple framework documentation scraper
├── documentation/                 # Scraped markdown files
│   ├── HIG/                      # Human Interface Guidelines (design docs)
│   ├── Swift-Book/               # Swift language docs (from GitHub)
│   └── mlx-docs/                 # MLX & CoreML Tools docs
├── scripts/
│   ├── index_to_meilisearch.py   # Indexer
│   ├── scrape_swift_docs.py      # Swift language docs scraper
│   ├── scrape_hig_docs.py        # Human Interface Guidelines scraper
│   └── scrape_mlx_docs.py        # MLX & CoreML Tools scraper
├── mcp-server/
│   ├── apple_docs_mcp.py         # Native HTTP MCP server
│   ├── docker-compose.yml        # Docker deployment
│   └── Dockerfile
└── landing/
    ├── index.html                # xdocs.dev landing page
    └── SKILL.md                  # Claude Code skill file (keep in sync with index.html)
```
