# Unraid Installation Guide

This guide covers installing the Apple Docs MCP Server on Unraid using the provided Docker template.

## Prerequisites

- Unraid 6.9.0 or newer
- Community Applications plugin installed (recommended)
- OpenAI API key for embeddings
- 3-5GB free disk space

## Installation Methods

### Method 1: Template Repository (Recommended)

1. In Unraid, navigate to **Docker** tab
2. Scroll to the bottom of the page
3. In **Template repositories**, add:
   ```
   https://github.com/Averyy/apple-dev-docs/tree/main/unraid
   ```
4. Click **Save**
5. Click **Add Container**
6. Select **apple-docs-mcp** from the dropdown
7. Configure settings (see below)
8. Click **Apply**

### Method 2: Manual XML Import

1. Download the template:
   ```bash
   wget https://raw.githubusercontent.com/Averyy/apple-dev-docs/main/unraid/apple-docs-mcp.xml
   ```
2. In Unraid Docker tab, click **Add Container**
3. Toggle to **Advanced View**
4. Import or paste the XML content
5. Configure and apply

## Configuration

### Required Settings

#### OpenAI API Key
- Get from: https://platform.openai.com/api-keys
- Required for generating embeddings
- Restricted to text-embedding-3-small model only

#### MCP API Key
- Generate using: `openssl rand -hex 32`
- Save this key for Claude Desktop configuration
- Used for API authentication

### Optional Settings

#### Keep Markdown Files
- **false** (recommended): Saves ~2GB disk space
- **true**: Keeps all scraped documentation files

#### Timezone
- Default: America/New_York
- Affects weekly update schedule (Sundays 1 AM)

### Port Configuration
- Default: 8080
- Change if port conflicts exist

### Storage Paths
All paths are customizable, defaults:
- **Vectorstore**: `/mnt/cache/appdata/apple-docs-mcp/vectorstore`
- **Hashes**: `/mnt/cache/appdata/apple-docs-mcp/hashes`
- **Documentation**: `/mnt/cache/appdata/apple-docs-mcp/documentation`
- **Logs**: `/mnt/cache/appdata/apple-docs-mcp/logs`

## First Run

### Initial Setup (4-6 hours)

On first start without existing data:
1. Container performs self-tests
2. Prompts to build vector index
3. Scrapes all Apple documentation
4. Generates embeddings
5. Starts MCP server

Monitor progress:
```bash
docker logs -f apple-docs-mcp
```

### Using Pre-built Data (Recommended)

To skip the initial build, copy existing data:

```bash
# From a machine with built data
scp -r mcp-server/vectorstore/ root@UNRAID_IP:/mnt/cache/appdata/apple-docs-mcp/
scp -r .hashes/ root@UNRAID_IP:/mnt/cache/appdata/apple-docs-mcp/
```

## Client Configuration

### Claude Desktop Setup

1. Edit Claude's config file:
   ```bash
   # macOS
   ~/Library/Application Support/Claude/claude_desktop_config.json
   
   # Windows
   %APPDATA%\Claude\claude_desktop_config.json
   
   # Linux
   ~/.config/Claude/claude_desktop_config.json
   ```

2. Add the MCP server:
   ```json
   {
     "mcpServers": {
       "apple-docs": {
         "type": "sse",
         "url": "http://UNRAID_IP:8080/mcp",
         "headers": {
           "Authorization": "Bearer YOUR_MCP_API_KEY"
         }
       }
     }
   }
   ```
   
   For deployed instance at 192.168.2.5:
   ```json
   {
     "mcpServers": {
       "apple-docs": {
         "type": "sse",
         "url": "http://192.168.2.5:8080/mcp",
         "headers": {
           "Authorization": "Bearer YOUR_MCP_API_KEY"
         }
       }
     }
   }
   ```

3. Restart Claude Desktop

## Testing

### Health Check
```bash
curl http://UNRAID_IP:8080/health
```

### Test Authentication
```bash
curl -H "Authorization: Bearer YOUR_MCP_API_KEY" \
     http://UNRAID_IP:8080/health
```

### Test Search
```bash
curl -X POST http://UNRAID_IP:8080/mcp/tools/call \
  -H "Authorization: Bearer YOUR_MCP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "search_apple_docs",
    "arguments": {
      "query": "SwiftUI Button",
      "platform": "ios",
      "limit": 5
    }
  }'
```

## Monitoring

### View Logs
- Unraid UI: Click container → Logs
- Terminal: `docker logs -f apple-docs-mcp`

### Check Services
```bash
docker exec apple-docs-mcp supervisorctl status
```

Expected output:
```
mcp-server    RUNNING   pid 123, uptime 1:23:45
scheduler     RUNNING   pid 124, uptime 1:23:45
```

### Monitor Resources
- CPU: Low usage except during indexing
- RAM: ~200MB normal, 2GB during indexing
- Disk I/O: High during initial scraping

## Maintenance

### Automatic Updates
- Runs weekly: Sundays at 1 AM (timezone configured)
- Uses ETags for efficient incremental updates
- Cost: ~$0.10-0.25 per update

### Manual Update
```bash
docker exec apple-docs-mcp \
  python /app/scraper/auto_scrape_and_embed.py --embed --yes
```

### Backup
```bash
# Backup vectorstore (most important)
cd /mnt/cache/appdata
tar -czf apple-docs-mcp-backup.tar.gz apple-docs-mcp/

# Restore
tar -xzf apple-docs-mcp-backup.tar.gz
```

## Troubleshooting

### Container Won't Start
1. Check logs: `docker logs apple-docs-mcp`
2. Verify API keys are set
3. Ensure port 8080 is available
4. Check disk space

### No Search Results
1. Verify index is built (check vectorstore size)
2. Confirm OpenAI API key is valid
3. Check MCP authentication
4. Wait for initial indexing to complete

### High Resource Usage
- Normal during initial indexing
- Indexing uses 2-4 CPU cores
- After indexing: minimal resources

### Connection Issues
1. Check firewall rules
2. Verify container is running
3. Test from Unraid terminal first
4. Ensure correct IP and port

## Network Considerations

### Remote Access
For access outside your network:
1. Use VPN (recommended)
2. Or reverse proxy with HTTPS
3. Never expose port 8080 directly to internet

### Example Nginx Reverse Proxy
```nginx
location /apple-docs/ {
    proxy_pass http://UNRAID_IP:8080/;
    proxy_set_header Authorization $http_authorization;
    proxy_set_header X-Real-IP $remote_addr;
}
```

## Support

- GitHub Issues: https://github.com/Averyy/apple-dev-docs/issues
- Unraid Forum: Search for "Apple Docs MCP"
- Documentation: Check `/docs` folder in repository
- Production deployment example: 192.168.2.5 with 341,207 documents indexed