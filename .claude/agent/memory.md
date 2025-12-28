# Project Memory

## xdocs.dev - Apple Documentation MCP Server

### Production Status (December 2025)

**Live URL:** https://xdocs.dev/mcp

| Metric | Value |
|--------|-------|
| Frameworks | 370+ |
| Documents | 334,636 |
| Search Latency | <3ms |
| Server Version | 2.0.0 |

### Technical Stack

- **Search Engine**: Meilisearch v1.9
- **MCP Server**: FastMCP (standalone package) with Streamable HTTP transport
- **Scraper**: Python + Apple's JSON API
- **Deployment**: Docker + GitHub Actions (auto-deploy on push to main)
- **Hosting**: VPS with Caddy reverse proxy
- **Landing Page**: Static HTML at xdocs.dev

### Key Features

- Native HTTP transport (Streamable HTTP)
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
- `MEILI_SEARCH_KEY` - Meilisearch search key (defaults to master key)
- `MCP_API_KEY` - Rate limit bypass
- `HTTP_PORT` - Server port (default: 8000)
- `RATE_LIMIT_REQUESTS` - Requests per minute (default: 30)

### VPS Configuration

- Caddy config: `~/caddy/Caddyfile`
- Caddy docker-compose: `~/caddy/docker-compose.yml`
- MCP server: `~/apple-dev-docs/mcp-server/`
- Landing page served from: `/var/www/xdocs/`
- Caddy needs volume mount: `/var/www/xdocs:/var/www/xdocs:ro`

### Session Log (Dec 28, 2025)

**Deployed to production:**
- Fixed critical FastMCP import (`from fastmcp import FastMCP` not `from mcp.server.fastmcp`)
- Removed obsolete `version: '3.8'` from docker-compose files
- Removed GHCR login from workflow (public repo doesn't need it)
- Fixed Caddy 404 by adding volume mount for landing page
- Successfully indexed 334,636 documents to Meilisearch
- Added Apple disclaimer to README
- Fixed GitHub links to open in new tab

**GitHub Secrets Required:**
- `VPS_HOST` - VPS IP address
- `VPS_USERNAME` - SSH username (root)
- `VPS_SSH_KEY` - SSH private key
