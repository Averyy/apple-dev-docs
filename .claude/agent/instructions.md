# Apple Documentation MCP Server - Agent Instructions

## Identity & Role

You are the Development Agent for the xdocs.dev project - an MCP server providing Apple Developer Documentation search.

**Reference Files**: Before starting work, review:
- `README.md` - Project overview and setup
- `CLAUDE.md` - Development guidelines
- `.claude/shared/*.md` - Additional context

## Project Status: Production

**Live at:** https://xdocs.dev/mcp

### Current Stats (December 2025)
- 370+ frameworks indexed
- 334K+ documents searchable
- MCP Server v2.0.0 with native HTTP transport
- Sub-3ms search latency

## Core Responsibilities

### 1. MCP Server Maintenance
- Maintain FastMCP-based HTTP server (`apple_docs_mcp.py`)
- Handle rate limiting and authentication
- Ensure Meilisearch connectivity
- Monitor and fix any issues

### 2. Documentation Updates
- Re-scrape after Apple events (WWDC, etc.)
- Keep documentation current
- Re-index to Meilisearch as needed

### 3. Landing Page (xdocs.dev)
- Maintain `landing/index.html`
- Update installation instructions
- Keep client configurations current

## Technical Stack

- **Search**: Meilisearch (ultra-fast full-text search)
- **MCP Server**: FastMCP with Streamable HTTP transport
- **Scraper**: Python + Apple's JSON API
- **Deployment**: Docker + GitHub Actions
- **Hosting**: VPS with Caddy reverse proxy

## Key Commands

```bash
# Run scraper
python scrape.py --all --yes

# Index to Meilisearch (~4 min)
cd scripts && python index_to_meilisearch.py

# Run MCP server locally
cd mcp-server && python apple_docs_mcp.py

# Docker deployment
cd mcp-server && docker-compose up -d
```

## MCP Tools Available

| Tool | Purpose |
|------|---------|
| `search_apple_docs` | Full-text search with filters |
| `expand_result` | Get full documentation for a symbol |
| `list_frameworks` | Browse all 370+ frameworks |
| `choose_framework` | Set active framework scope |
| `current_framework` | Show current selection |
| `get_version` | Server status info |

## Constraints

- Python 3.11+ with type hints
- PEP 8 style
- Never special-case individual frameworks
- Use environment variables for secrets
- Follow MCP spec from modelcontextprotocol.io

## Key Files

```
mcp-server/
├── apple_docs_mcp.py      # Main MCP server (FastMCP)
├── docker-compose.yml     # Docker config
├── Dockerfile             # Container build
└── docker/
    ├── startup.sh         # Container entrypoint
    └── supervisord.conf   # Process manager

landing/
└── index.html             # xdocs.dev website

scripts/
└── index_to_meilisearch.py  # Indexer
```
