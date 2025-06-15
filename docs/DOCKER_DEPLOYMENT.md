# Docker Deployment Guide

This guide covers deploying the Apple Docs MCP Server using Docker.

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose installed
- OpenAI API key
- MCP API key (generate with `openssl rand -hex 32`)

### 1. Clone and Configure

```bash
git clone https://github.com/Averyy/apple-dev-docs.git
cd apple-developer-docs

# Create .env file
cat > .env << EOF
OPENAI_API_KEY=your-openai-api-key
MCP_API_KEY=$(openssl rand -hex 32)
EOF
```

### 2. Deploy with Quick Start Script

```bash
cd mcp-server/deploy
./quick-start.sh
```

This script will:
- ✅ Check prerequisites
- 📦 Create Docker volumes
- 🏗️ Build the Docker image
- 🚀 Start all services
- ⏳ Wait for health checks
- 📊 Show connection information

## 📋 Manual Deployment

If you prefer manual deployment:

```bash
cd mcp-server

# Create volumes
docker volume create apple-docs-vectorstore
docker volume create apple-docs-hashes
docker volume create apple-docs-documentation
docker volume create apple-docs-logs

# Build and start
docker-compose up -d --build

# Check health
curl http://localhost:8080/health
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | OpenAI API key for embeddings | - | ✅ |
| `MCP_API_KEY` | Bearer token for MCP authentication | - | ✅ |
| `MCP_PORT` | Port for MCP server | 8080 | ❌ |
| `KEEP_MARKDOWN_FILES` | Keep scraped markdown files | true | ❌ |

#### Setting Environment Variables

**Option 1: .env File (Recommended)**
```bash
# Create .env file in project root
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
MCP_API_KEY=e04dbb19b7a482bd7bd42af1048b3f0d5b2a458e5af450ce4b1f2a833f9f3ff8
KEEP_MARKDOWN_FILES=false
```

**Option 2: Docker Run Command**
```bash
docker run -d \
  -e OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx \
  -e MCP_API_KEY=e04dbb19b7a482bd7bd42af1048b3f0d5b2a458e5af450ce4b1f2a833f9f3ff8 \
  -e KEEP_MARKDOWN_FILES=false \
  apple-docs-mcp
```

**Option 3: Docker Compose**
The `docker-compose.yml` automatically reads from `.env` file:
```yaml
environment:
  - OPENAI_API_KEY=${OPENAI_API_KEY}
  - MCP_API_KEY=${MCP_API_KEY}
  - KEEP_MARKDOWN_FILES=${KEEP_MARKDOWN_FILES:-true}
```

#### Security Notes
- **Never commit .env file** - It's already in .gitignore
- **Rotate API keys regularly** - Especially MCP_API_KEY
- **Use secrets management** in production (AWS Secrets Manager, etc.)

### Production vs Development

**Development (keep markdown for debugging):**
```yaml
environment:
  - KEEP_MARKDOWN_FILES=true  # ~2GB disk usage
```

**Production (save disk space):**
```yaml
environment:
  - KEEP_MARKDOWN_FILES=false  # ~100MB disk usage
```

## 📅 Automatic Updates

The container includes an automatic rescraping scheduler that runs:
- **Every Sunday at 1:00 AM**
- Uses ETags for efficient updates
- Only re-embeds changed documents
- Costs ~$0.10-0.25 per update

### Manual Update

Force an immediate update:

```bash
docker exec apple-docs-mcp python /app/scraper/auto_scrape_and_embed.py --embed --yes
```

## 🔍 Monitoring

### Check Service Status

```bash
# View all processes
docker exec apple-docs-mcp supervisorctl status

# Expected output:
# mcp-server    RUNNING   pid 123, uptime 1:23:45
# scheduler     RUNNING   pid 124, uptime 1:23:45
```

### View Logs

```bash
# All logs
docker logs -f apple-docs-mcp

# MCP server logs only
docker exec apple-docs-mcp tail -f /data/logs/mcp-server.log

# Scheduler logs only
docker exec apple-docs-mcp tail -f /data/logs/scheduler.log
```

### Check Last Update

```bash
docker exec apple-docs-mcp cat /data/hashes/last_update.txt
```

## 🏥 Health Checks

The container includes automatic health checks:

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
  interval: 30s
  timeout: 10s
  retries: 3
```

Docker will automatically restart unhealthy containers.

## 📦 Volume Management

### Backup Volumes

```bash
# Backup vectorstore (most important)
docker run --rm -v apple-docs-vectorstore:/data \
  -v $(pwd):/backup alpine \
  tar czf /backup/vectorstore-backup.tar.gz -C /data .

# Backup hashes
docker run --rm -v apple-docs-hashes:/data \
  -v $(pwd):/backup alpine \
  tar czf /backup/hashes-backup.tar.gz -C /data .
```

### Restore Volumes

```bash
# Restore vectorstore
docker run --rm -v apple-docs-vectorstore:/data \
  -v $(pwd):/backup alpine \
  tar xzf /backup/vectorstore-backup.tar.gz -C /data
```

## 🔒 Security Best Practices

1. **Never expose port 8080 publicly** - Use a reverse proxy with HTTPS
2. **Rotate API keys regularly** - Update MCP_API_KEY periodically
3. **Run as non-root user** - Container uses `mcpuser` (UID 1000)
4. **Keep base image updated** - Rebuild monthly for security patches

## 🐛 Troubleshooting

### Container won't start

```bash
# Check logs
docker logs apple-docs-mcp

# Common issues:
# - Missing OPENAI_API_KEY
# - Missing MCP_API_KEY
# - Port 8080 already in use
```

### MCP server unhealthy

```bash
# Check detailed health
docker exec apple-docs-mcp curl -v http://localhost:8080/health

# Restart services
docker exec apple-docs-mcp supervisorctl restart all
```

### Disk space issues

```bash
# Check volume sizes
docker system df -v

# Clean up if KEEP_MARKDOWN_FILES=false
docker exec apple-docs-mcp find /data/documentation -name "*.md" -delete
```

## 🚢 Production Deployment

For production deployments:

1. **Use a reverse proxy** (nginx, Caddy) with HTTPS
2. **Set resource limits** in docker-compose.yml
3. **Enable log rotation** for long-running containers
4. **Monitor with Prometheus/Grafana** (metrics endpoint planned)
5. **Use external volume backups** (cloud storage)

Example production compose override:

```yaml
services:
  apple-docs-mcp:
    deploy:
      resources:
        limits:
          memory: 2G
          cpus: '1.0'
        reservations:
          memory: 1G
          cpus: '0.5'
    logging:
      driver: "json-file"
      options:
        max-size: "50m"
        max-file: "10"
```

## 📊 Metrics

The container tracks:
- Total documents: 341,207 (deployed)
- Vector embeddings: 323,118 (deployed)
- Update frequency: Weekly (Sundays 1 AM)
- Average update cost: $0.10-0.25
- Disk usage: 2-3GB (with vectorstore)
- Production deployment: 192.168.2.5

## 📤 Deploying with Pre-built Data

If you have pre-built data from a previous deployment, you can upload it to avoid the initial 4-6 hour build time.

### Directory Structure

1. **Vectorstore** (ChromaDB)
   ```
   mcp-server/vectorstore/
   ├── chroma.sqlite3
   └── f37d385c-7440-4910-8750-dd16e49bbf24/  # UUID folder
       ├── data_level0.bin            # ~1.9GB
       ├── header.bin
       ├── index_metadata.pickle
       ├── length.bin
       └── link_lists.bin
   ```
   **YES, upload the ENTIRE structure**, including the UUID folder!

2. **Hashes** (ETags & Content Hashes)
   ```
   .hashes/
   ├── content_hashes.json      # SHA-256 hashes of all documents
   ├── embedding_hashes.json    # Hashes of embedded content
   ├── etag_cache.json         # Apple server ETags for change detection
   └── url_content_map.json    # URL to file mapping
   ```

3. **Documentation** (Optional - only if `KEEP_MARKDOWN_FILES=true`)
   ```
   documentation/
   ├── SwiftUI/
   ├── UIKit/
   ├── Foundation/
   └── ... (300+ framework folders)
   ```

### Complete Upload Process

```bash
# 1. Start the container first
cd mcp-server
docker-compose up -d

# 2. Wait for it to initialize (check logs)
docker logs -f apple-docs-mcp
# Press Ctrl+C when you see "Starting services with supervisor..."

# 3. Upload vectorstore (includes UUID folder)
docker cp vectorstore/. apple-docs-mcp:/data/vectorstore/

# 4. Upload hashes
docker cp ../.hashes/. apple-docs-mcp:/data/hashes/

# 5. (Optional) Upload documentation if KEEP_MARKDOWN_FILES=true
docker cp ../documentation/. apple-docs-mcp:/data/documentation/

# 6. Restart container to recognize data
docker-compose restart

# 7. Verify everything loaded
curl -H "Authorization: Bearer $MCP_API_KEY" http://localhost:8080/health
```

### Directory Mapping

| Local Path | Docker Path | Purpose |
|------------|-------------|---------|
| `.env` | (read by docker-compose) | API keys and settings |
| `mcp-server/vectorstore/` | `/data/vectorstore/` | ChromaDB embeddings |
| `.hashes/` | `/data/hashes/` | ETags, content hashes |
| `documentation/` | `/data/documentation/` | Markdown files (optional) |
| N/A | `/data/logs/` | Container logs |

### Verification After Upload

```bash
# Check vectorstore
docker exec apple-docs-mcp ls -la /data/vectorstore/
# Should show: chroma.sqlite3 and UUID folder

# Check UUID folder contents
docker exec apple-docs-mcp ls -la /data/vectorstore/f*/
# Should show: data_level0.bin, header.bin, etc.

# Check hashes
docker exec apple-docs-mcp ls -la /data/hashes/
# Should show: content_hashes.json, etag_cache.json, etc.

# Test search
curl -X POST http://localhost:8080/mcp/tools/call \
  -H "Authorization: Bearer $MCP_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "search_apple_docs",
    "arguments": {
      "query": "SwiftUI Button",
      "platform": "ios",
      "limit": 2
    }
  }'
```

### Important Notes

1. **UUID Folder**: The vectorstore UUID folder (like `f37d385c-7440-4910-8750-dd16e49bbf24`) MUST be uploaded completely
2. **File Ownership**: Docker will automatically fix permissions
3. **Space Requirements**: 
   - Vectorstore: ~2GB
   - Hashes: ~100MB
   - Documentation: ~2GB (optional)
4. **First Run**: If no data is uploaded, container will offer to build everything (~4-6 hours)

### Troubleshooting Upload Issues

If search returns no results after upload:

```bash
# Check ChromaDB recognized the data
docker exec apple-docs-mcp python -c "
import chromadb
client = chromadb.PersistentClient('/data/vectorstore')
collection = client.get_collection('apple_docs')
print(f'Documents in collection: {collection.count()}')
"

# Should show ~323,118 documents
```

If count is 0, the vectorstore upload was incomplete. Re-upload ensuring the UUID folder is included.

## 🆘 Support

- Check container health: `docker exec apple-docs-mcp curl http://localhost:8080/health`
- View recent logs: `docker logs --tail 100 apple-docs-mcp`
- Force restart: `docker-compose restart`
- Full reset: `docker-compose down -v && docker-compose up -d`