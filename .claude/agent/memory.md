# Project Memory

## xdocs.dev - Apple Documentation MCP Server

### Production Status (December 2025)

**Live URL:** https://xdocs.dev/mcp

| Metric | Value |
|--------|-------|
| Frameworks | 370+ |
| Documents | 334K+ |
| Search Latency | <3ms |
| Server Version | 2.0.0 |

### Technical Stack

- **Search Engine**: Meilisearch
- **MCP Server**: FastMCP (Python) with Streamable HTTP transport
- **Scraper**: Python + Apple's JSON API
- **Deployment**: Docker + GitHub Actions
- **Hosting**: VPS with Caddy
- **Landing Page**: Static HTML at xdocs.dev

### Key Features

- Native HTTP transport (no STDIO wrapper)
- Rate limiting (30 req/min, bypassed with API key)
- Wildcard search (`*View`, `UI*`)
- Platform filtering (ios, macos, visionos, etc.)
- Framework scoping
- Token budget management (1K-25K)

### URLs

- Website: https://xdocs.dev
- MCP Endpoint: https://xdocs.dev/mcp
- Health Check: https://xdocs.dev/health
- GitHub: https://github.com/Averyy/apple-dev-docs
- Contact: info@xdocs.dev

### Environment Variables

Required:
- `MEILI_MASTER_KEY` - Meilisearch auth

Optional:
- `MCP_API_KEY` - Rate limit bypass
- `HTTP_PORT` - Server port (default: 8000)
