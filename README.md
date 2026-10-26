# xdocs - Apple Developer Documentation MCP Server

> **Note:** This is an independent project not affiliated with, endorsed by, or sponsored by Apple Inc. Documentation content is © Apple Inc. and provided for development use only.

An MCP server that gives Claude and other AI assistants instant access to Apple's complete developer documentation. 390+ frameworks, 322K+ documents, ~16 ms median search.

[![Frameworks](https://img.shields.io/badge/frameworks-390%2B-blue)](https://xdocs.dev)
[![Documents](https://img.shields.io/badge/documents-322K%2B-green)](https://xdocs.dev)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)
[![Twice Weekly Scrape](https://github.com/Averyy/apple-dev-docs/actions/workflows/scheduled-scrape.yml/badge.svg)](https://github.com/Averyy/apple-dev-docs/actions/workflows/scheduled-scrape.yml)

## Quick Start

### Claude Code

```bash
claude mcp add --transport http apple-docs https://xdocs.dev/mcp
```

### Claude Desktop

1. Open Claude Desktop
2. Go to **Settings → Connectors**
3. Click **"Add custom connector"**
4. Name: `apple-docs`
5. URL: `https://xdocs.dev/mcp`
6. Click **Add**

### Cursor

Add to Cursor Settings → MCP:
```json
{
  "apple-docs": {
    "url": "https://xdocs.dev/mcp"
  }
}
```

### VSCode

Create `.vscode/mcp.json`:
```json
{
  "servers": {
    "apple-docs": {
      "type": "http",
      "url": "https://xdocs.dev/mcp"
    }
  }
}
```

### Other MCP Clients

For stdio-only clients, use `mcp-remote` as a bridge:
```json
{
  "mcpServers": {
    "apple-docs": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://xdocs.dev/mcp"]
    }
  }
}
```

## Why?

Apple's developer documentation website uses aggressive lazy-loading, rendering only visible content in the HTML source. This makes it nearly impossible for AI systems to effectively search or reference Apple's documentation.

This project provides a complete, searchable mirror of Apple's documentation in a clean, AI-friendly format. All content is unchanged from the original source - we've simply made it accessible.

**Updated automatically** twice weekly (Tue/Fri) from Apple's live documentation — includes WWDC 2026 content.

## Features

- **390+ frameworks** - SwiftUI, UIKit, Metal, ARKit, Core ML, and more
- **Nested modules** - Intents, Photos, simd, Apple News Format and the other modules Apple nests under an umbrella framework, each in its own folder
- **Human Interface Guidelines** - Apple's design documentation for all platforms
- **Swift Language Guide** - The Swift Programming Language book, API Design Guidelines, C++ Interop
- **MLX & CoreML Tools** - Apple's ML framework documentation, plus the Foundation Models Python SDK
- **Apple open-source tooling docs** - container, SourceKit-LSP, swift-format, Game Porting Toolkit (Metal shader converter)
- **App Store Review Guidelines** - and Apple's app privacy pages
- **Fast search** - Powered by Meilisearch (~16 ms median per search, one result per page)
- **Platform filtering** - iOS, macOS, tvOS, watchOS, visionOS
- **Wildcard search** - `UIView*`, `UI*Controller`, `Button?` (matched against the top matches for the pattern's text and, when it starts with two or more literal characters, every API name starting with them, up to 10,000; names in the pattern's case come first, unless it is all lowercase)
- **Token management** - 1K-25K token budgets
- **Native HTTP** - Streamable HTTP transport (no wrappers needed)

## Available Tools

### `search_apple_docs`
Search documentation with natural language queries (one result per page).

```
query: "SwiftUI Button custom style"
framework: "SwiftUI" (optional)
platform: "ios" (optional)
limit: 10 (1-20)
```

### `expand_result`
Get full documentation for a symbol or file path. A page too long for one response comes in parts: a reply holds as many as fit and ends with which ones (e.g. "Parts 1-4 of 12") and the `part` to pass for the rest (a search result from a long page shows the part it matched, which `part` can start from).

```
file_path: "Button" or "documentation/SwiftUI/view.md"
framework: "SwiftUI" (optional, for symbol names found in several frameworks)
part: 5 (optional, the part of a long page to start from)
```

### `list_frameworks`
Browse all 390+ frameworks with document counts.

```
query: "UI" (optional filter)
```

## Self-Hosting

### Docker (Recommended)

```bash
# Clone
git clone https://github.com/Averyy/apple-dev-docs.git
cd apple-dev-docs

# Configure
cp .env.example .env
# Edit .env: set MEILI_MASTER_KEY (run: openssl rand -hex 32)

# Run
cd mcp-server
docker compose up -d

# Server available at http://localhost:8000/mcp
# First run indexes ~322K docs (~15-20 minutes)
```

### Local Development

```bash
# Install dependencies
pip install -r mcp-server/requirements.txt

# Start Meilisearch
docker run -d -p 7700:7700 \
  -e MEILI_MASTER_KEY=$(openssl rand -hex 32) \
  -v $(pwd)/meilisearch:/meili_data \
  getmeili/meilisearch:v1.49

# Index documents (~15-20 minutes)
cd scripts && python3 index_to_meilisearch.py

# Run server
cd ../mcp-server && python3 apple_docs_mcp.py
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `MEILI_MASTER_KEY` | Yes | Meilisearch auth key (`openssl rand -hex 32`) |
| `MCP_API_KEY` | No | API key for rate limit bypass |
| `ALLOWED_HOSTS` | No | Comma-separated public hostnames accepted in the Host header (default: `xdocs.dev,www.xdocs.dev`; localhost always allowed, others get 421) |
| `HTTP_PORT` | No | Server port (default: 8000) |
| `MEILI_TIMEOUT` | No | Meilisearch connection timeout in seconds (default: 10) |
| `MEILI_MAX_RETRIES` | No | Max retries for transient errors (default: 2) |
| `RATE_LIMIT_REQUESTS` | No | Requests per minute per IP (default: 60) |
| `MIN_EXPECTED_DOCS` | No | Minimum docs for "healthy" status (default: 290000) |
| `EXPECTED_FULL_INDEX_SIZE` | No | Expected full index size for progress calc (default: 322000) |

## Updating Documentation

```bash
# Clean up frameworks Apple has removed
python3 scripts/utilities/cleanup_removed_frameworks.py --dry-run  # Preview
python3 scripts/utilities/cleanup_removed_frameworks.py            # Interactive
python3 scripts/utilities/cleanup_removed_frameworks.py --yes      # Automated

# Scrape Apple framework documentation
python3 scrape.py --all --yes

# Scrape Swift language documentation (from GitHub)
python3 scripts/scrape_swift_docs.py

# Scrape MLX, CoreML Tools, the other Sphinx/GitHub docs and the App Store pages (Python 3.12, with requirements-scrape.txt installed too)
python3 scripts/scrape_mlx_docs.py

# Re-index to Meilisearch
cd scripts && python3 index_to_meilisearch.py
```

### Cleanup Scripts

**`cleanup_removed_frameworks.py`** - Removes entire frameworks that Apple no longer lists in `technologies.json` (the scheduled scrape runs it before `scrape.py`):
- Candidates are the Apple framework hash files (`.hashes/<id>_hashes.json` with Apple JSON-URL keys; not module hash files or anything under `.hashes/<subdir>/`) whose id `technologies.json` doesn't list, compared case-insensitively. It reads `technologies.json` with the same parser as `scrape.py`, scans no doc folders and makes no other request
- Each run that finds a framework unlisted counts it in its hash file (`unlisted_runs`). On the 2nd consecutive run its docs dir and hash file are deleted, however many frameworks are dropped at once. A framework that is listed again starts over: this script resets the count, and so does `scrape.py` for every framework it scrapes
- If `technologies.json` can't be fetched or lists no frameworks, nothing is counted, reset or deleted, and it exits 1. An unlisted framework's hash file that can't be read also exits 1: the run counts as its first, and the file is replaced by one holding that count, so the framework is still removed if the next run finds it unlisted too (a file that can't be read with no docs dir of its id is left alone, since another scraper's state file looks the same). Without `--yes` it asks before deleting; `--dry-run` changes nothing

**`--cleanup-orphans --auto-cleanup`** flags on `scrape.py` - Removes individual pages within frameworks that Apple has deleted (404/410) or no longer links, in the frameworks scraped in that run (without `--auto-cleanup` it lists them and asks once):
- If a framework's orphaned pages are at least half of its files, or more than 1,000, nothing is deleted that run: the list is kept in its hash file (`pending_orphans`), and the next clean run deletes the ones it finds orphaned again. Other orphaned pages that run are deleted with them, unless they are again at least half of the files left (or more than 1,000): then they replace the list and wait for the run after
- A framework's cleanup is skipped for the run, keeping all its files, when one of its requests fails with anything but 404/410 (a server error, a timeout, invalid JSON, a 429 that outlasts the retries, or another 4xx on a page we already have), a page fails to convert or save, its hash file can't be loaded or saved, another error of ours interrupts its scrape, or the run recorded none of its pages (`framework_zero_touched`)
- A page we already have whose fetch fails on 3 consecutive runs stops blocking and is treated as removed: it and the pages reachable only through it are deleted. If Apple answered 304 (unchanged) and only the follow-up fetch for the page's links failed, the page is live: its file is kept, and the pages reachable only through it are deleted
- A page we don't have yet stops blocking when its fetch fails on 3 consecutive runs: it has no file to delete, but the pages reachable only through it are deleted. A 4xx other than 429 on such a page never blocks, so the pages reachable only through it are deleted in the same run
- The 3 failed runs must be in a row: a run in which the page loads, Apple answers 404/410 for it, or it isn't fetched at all (no page reached that run links to it) starts the count again
- If more than 5 pages and more than 1% of a framework's pages hit one of the fetch failures above in one run, that run counts toward a page's 3 failed runs only when it is the 3rd or later such run in a row
- A page that fails to convert or save on 3 runs, with no successful save in between, stops blocking but is kept
- A framework's root page never counts toward the 3 failed fetch runs (a root that fails to convert or save follows the rule above). If the root or its links can't be read (a failure other than 404/410, or a 404/410 after the root answered normally earlier in the same run), the framework's cleanup is skipped on every run until the root recovers. A root that returns 404/410 (Apple may be removing the framework, not an error of ours) skips it too, unless the root answers normally later in the same run. Once it has returned 404/410 on 2 runs with no normal answer in between, the framework's docs dir and hash file are deleted at the end of that run

### Re-indexing

**`scripts/index_to_meilisearch.py`** - Keeps the `apple-docs` index in step with `documentation/` and records each file's hash for the next run. The live index serves every search throughout:
- **Update** (the usual run): new and changed docs are added first, then the documents they no longer have (fewer chunks, a doc that became one document or several) and those of removed docs are deleted by `file_path`, at most 2,000 paths per delete; removed docs leave the hash file. A run with nothing changed sends nothing to the live index (its settings are updated only where they differ)
- **Rebuild** (`--force`, or when one is due): every doc goes into a new index, `apple-docs-build`, which replaces the live index in one atomic swap once it holds at least 90% as many documents as there are files (on a fresh volume it is renamed to `apple-docs`). A rebuild is due when there is no index yet, when the hash file records another processor version (`PROCESSOR_VERSION`, bumped whenever the documents built from a file change) or another index (it records the `createdAt` of the index its hashes describe), when an older version of the indexer has run on the live index (a rollback: it drops `index_gen` from the filterable attributes and leaves stale documents), 6.5 days after the live index was built, or when more than 25% of the files changed. A failed rebuild leaves the live index as it was. Over a live index, a rebuild starts only when Meilisearch's disk has room for the second index (1.2× the database's size on disk plus 1 GiB free, checked in the Docker image, where the indexer runs beside Meilisearch), and stops, deleting its build index, if free space falls under 1 GiB between two batches: a full disk would crash Meilisearch and keep it from starting again. When a due rebuild fails before its swap, or isn't started for lack of disk, the run applies the update to the live index instead (once Meilisearch answers again, if it went down), records the rebuild as still due and exits 1, and the next run retries the rebuild. That update also indexes again any file an older version of the indexer added documents for (a rollback), so the stale documents beside them go. `--limit` (for testing) rebuilds only on a fresh index, never in place of a live one
- **Image completeness:** in the Docker image, `DOC_FILE_COUNT` (set by the docker-build workflow) is the `.md` count of the checkout the image was built from. An image holding another count is incomplete: nothing is swapped, added or deleted, and the run exits 1. Without it (local runs and builds), the docs must number at least 90% of the live index's documents; set `DOC_FILE_COUNT` to the expected count to confirm a larger removal
- It checks the outcome of every Meilisearch task it queues. If one fails, or Meilisearch can't be reached, it stops, saves no hashes and exits 1, so the next run indexes the same files again (an update records the files it sends as pending in the hash file before its first add, so the documents of one removed since are deleted instead of staying in search; a due rebuild's failure is first followed by the update, above); in the Docker image, Meilisearch and the MCP server keep serving the index as it is
- A file it can't index is left out, logged and counted, and the run still exits 0, so one bad file can't fail every run: a file that can't be read or processed, one whose name isn't valid UTF-8 or with a document id Meilisearch would reject (over 511 bytes, or characters other than `A-Z a-z 0-9 _ -`; either would fail its whole batch), or one whose `file_path` is over 468 bytes as Meilisearch filters it (Meilisearch keeps only its first 468 bytes, so a filter on its path never finds or deletes it, and one on another file's path equal to those bytes catches it too). Its hash isn't recorded, so it is tried again on every run, and a changed file keeps its old documents until then
- In the Docker image, `startup_check.py` runs it on every container start (never with `--force`: the indexer decides), and its whole output, including its mode (incremental update or rebuild by swap, and why), each file left out and the cause of a failed run, goes to `/data/logs/startup-check.log`

## Requirements

- Python 3.11+ or Docker (the Docker image uses 3.11)
- Python 3.12+ to scrape, as the scheduled scrape workflow does: the MLX scraper needs wafer-py (`pip install -r requirements.txt -r requirements-scrape.txt`)
- 1.5GB RAM (4GB+ recommended for indexing)
- ~13GB disk space: the Docker image (~2.5GB, the 1.4GB documentation included) and the Meilisearch index (~5GB on disk for the full corpus, which `/stats` reports as ~3GB), which a rebuild needs room for twice: the new index is built beside the live one until the swap. With less, the indexer doesn't start the rebuild and keeps updating the live index (see Re-indexing)

## License

**Code**: MIT License
**Documentation Content**: © Apple Inc. - For development use only

## Links

- **Website**: [xdocs.dev](https://xdocs.dev)
- **GitHub**: [github.com/Averyy/apple-dev-docs](https://github.com/Averyy/apple-dev-docs)
- **Contact**: info@xdocs.dev
