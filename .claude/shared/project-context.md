# xdocs.dev - Project Context

## Overview

MCP server providing Apple Developer Documentation search. Live at https://xdocs.dev/mcp

## Stats (December 2025)

- **Frameworks**: 370+
- **Documents**: 334K+
- **Search Latency**: <3ms
- **Server Version**: 2.0.0

## Technical Architecture

### Stack
- **Language**: Python 3.11+
- **Search**: Meilisearch
- **MCP Framework**: FastMCP with Streamable HTTP transport
- **Scraping**: httpx + Apple's JSON API
- **Deployment**: Docker + GitHub Actions
- **Hosting**: VPS with Caddy reverse proxy

### Repository Structure
```
apple-dev-docs/
├── README.md
├── CLAUDE.md
├── scrape.py                    # Documentation scraper
├── documentation/               # Scraped markdown files (334K+)
├── scripts/
│   └── index_to_meilisearch.py  # Indexer
├── mcp-server/
│   ├── apple_docs_mcp.py        # Native HTTP MCP server
│   ├── docker-compose.yml       # Docker config
│   ├── Dockerfile
│   └── docker/
│       ├── startup.sh           # Container entrypoint
│       └── supervisord.conf     # Process manager
└── landing/
    └── index.html               # xdocs.dev website
```

## MCP Server Features

### Tools
| Tool | Description |
|------|-------------|
| `search_apple_docs` | Full-text search with wildcard support |
| `expand_result` | Get full content for a symbol |
| `list_frameworks` | Browse frameworks with filtering |
| `choose_framework` | Set active framework scope |
| `current_framework` | Show current selection |
| `get_version` | Server status info |

### Features
- Native HTTP transport (Streamable HTTP)
- Rate limiting (30 req/min, bypassed with API key)
- Wildcard search (`*View`, `UI*`)
- Platform filtering (ios, macos, visionos, etc.)
- Token budget management (1K-25K)
- CORS enabled

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `MEILI_MASTER_KEY` | Yes | Meilisearch auth key |
| `MCP_API_KEY` | No | API key for rate limit bypass |
| `HTTP_PORT` | No | Server port (default: 8000) |

## Key Commands

```bash
# Scrape all frameworks
python scrape.py --all --yes

# Index to Meilisearch (~4 min)
cd scripts && python index_to_meilisearch.py

# Run MCP server
cd mcp-server && python apple_docs_mcp.py

# Docker deployment
cd mcp-server && docker-compose up -d
```

## URLs

- Website: https://xdocs.dev
- MCP Endpoint: https://xdocs.dev/mcp
- Health: https://xdocs.dev/health
- GitHub: https://github.com/Averyy/apple-dev-docs
- Contact: info@xdocs.dev
