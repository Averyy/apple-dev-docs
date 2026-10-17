# xdocs - Apple Developer Documentation MCP Server

> **Note:** This is an independent project not affiliated with, endorsed by, or sponsored by Apple Inc. Documentation content is © Apple Inc. and provided for development use only.

An MCP server that gives Claude and other AI assistants instant access to Apple's complete developer documentation. 390+ frameworks, 322K+ documents, sub-3ms search.

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
- **Human Interface Guidelines** - Apple's design documentation for all platforms
- **Swift Language Guide** - The Swift Programming Language book, API Design Guidelines, C++ Interop
- **MLX & CoreML Tools** - Apple's ML framework documentation
- **Sub-3ms search** - Powered by Meilisearch
- **Platform filtering** - iOS, macOS, tvOS, watchOS, visionOS
- **Wildcard search** - `UIView*`, `NS*Button`, `Button?` (patterns filter the top matches, so start with a literal prefix)
- **Token management** - 1K-25K token budgets
- **Native HTTP** - Streamable HTTP transport (no wrappers needed)

## Available Tools

### `search_apple_docs`
Search documentation with natural language queries.

```
query: "SwiftUI Button custom style"
framework: "SwiftUI" (optional)
platform: "ios" (optional)
limit: 10 (1-20)
```

### `expand_result`
Get full documentation for a symbol.

```
file_path: "Button" or "documentation/SwiftUI/view.md"
framework: "SwiftUI" (optional, for symbol names found in several frameworks)
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

# Scrape MLX & CoreML Tools documentation (Python 3.12, with requirements-scrape.txt installed too)
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

## Requirements

- Python 3.11+ or Docker (the Docker image uses 3.11)
- Python 3.12+ to scrape, as the scheduled scrape workflow does: the MLX scraper needs wafer-py (`pip install -r requirements.txt -r requirements-scrape.txt`)
- 1.5GB RAM (4GB+ recommended for indexing)
- ~5GB disk space (1.5GB documentation + Meilisearch index + Docker image)

## License

**Code**: MIT License
**Documentation Content**: © Apple Inc. - For development use only

## Links

- **Website**: [xdocs.dev](https://xdocs.dev)
- **GitHub**: [github.com/Averyy/apple-dev-docs](https://github.com/Averyy/apple-dev-docs)
- **Contact**: info@xdocs.dev
