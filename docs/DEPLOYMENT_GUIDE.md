# 🚀 Apple Docs MCP Server Deployment Guide

This comprehensive guide covers deploying the Apple Docs MCP Server using Docker, integrating all deployment steps and verification procedures.

## 📊 System Overview

- **Total Documents**: 341,207 across 341 frameworks
- **Vector Embeddings**: 323,118 in ChromaDB
- **Update Frequency**: Automatic weekly updates (Sundays 1 AM)
- **Average Update Cost**: $0.10-0.25 per update
- **Search Performance**: Sub-500ms with platform filtering

## ✅ Pre-Deployment Checklist

### 1. Prerequisites
- [ ] Docker and Docker Compose installed
- [ ] Git installed
- [ ] OpenAI API key (for embeddings)
- [ ] 4GB+ available disk space
- [ ] Port 8080 available (or configure alternative)

### 2. Environment Setup
- [ ] Clone the repository
- [ ] Generate MCP API key with `openssl rand -hex 32`
- [ ] Create `.env` file with required variables
- [ ] Decide on `KEEP_MARKDOWN_FILES` setting (true for dev, false for prod)

### 3. Data Preparation (Choose One)
- [ ] **Option A**: Start fresh (4-6 hour initial build)
- [ ] **Option B**: Upload pre-built data (see section below)

## 🚀 Quick Start Deployment

### Step 1: Clone and Configure

```bash
# Clone repository
git clone https://github.com/Averyy/apple-dev-docs.git
cd apple-developer-docs

# Create .env file
cat > .env << EOF
OPENAI_API_KEY=your-openai-api-key
MCP_API_KEY=$(openssl rand -hex 32)
MCP_SERVER_URL=http://localhost:8080  # Or your deployment URL
KEEP_MARKDOWN_FILES=false  # Set to true for development
EOF

# Save the MCP_API_KEY for later use
echo "Save this MCP_API_KEY: $(grep MCP_API_KEY .env | cut -d= -f2)"
```

### Step 2: Deploy with Quick Start Script

```bash
cd mcp-server/deploy
./quick-start.sh
```

This script will:
- ✅ Check all prerequisites
- 📦 Create required Docker volumes
- 🏗️ Build the Docker image
- 🚀 Start all services
- ⏳ Wait for health checks to pass
- 📊 Display connection information
- 🧪 Run self-tests

### Step 3: Verify Deployment

```bash
# Check health endpoint
curl -H "Authorization: Bearer $MCP_API_KEY" $MCP_SERVER_URL/health

# Expected response:
# {
#   "status": "healthy",
#   "vectorstore": {
#     "collection": "apple_docs",
#     "document_count": 323118
#   }
# }

# Test search functionality
curl -X POST $MCP_SERVER_URL/mcp/tools/call \
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

## 📋 Manual Deployment Steps

If you prefer manual deployment or need to customize:

```bash
cd mcp-server

# Create persistent volumes
docker volume create apple-docs-vectorstore
docker volume create apple-docs-hashes
docker volume create apple-docs-documentation
docker volume create apple-docs-logs

# Build and start services
docker-compose up -d --build

# Monitor startup
docker logs -f apple-docs-mcp

# Wait for "MCP server started successfully" message
```

## 🔧 Configuration Reference

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | OpenAI API key for embeddings | - | ✅ |
| `MCP_API_KEY` | Bearer token for MCP authentication | - | ✅ |
| `MCP_SERVER_URL` | Server URL for testing | http://localhost:8080 | ❌ |
| `MCP_PORT` | Port for MCP server | 8080 | ❌ |
| `KEEP_MARKDOWN_FILES` | Keep scraped markdown files | true | ❌ |

### Security Configuration

1. **API Key Security**
   - ✅ Store in `.env` file (gitignored)
   - ✅ Use environment variables only
   - ❌ Never hardcode in source
   - ✅ Rotate MCP_API_KEY regularly

2. **Network Security**
   - Run behind reverse proxy with HTTPS in production
   - Use bearer token authentication for all requests
   - Container runs as non-root user (mcpuser, UID 1000)

### Resource Settings

**Development:**
```yaml
environment:
  - KEEP_MARKDOWN_FILES=true  # ~4GB total disk usage
```

**Production:**
```yaml
environment:
  - KEEP_MARKDOWN_FILES=false  # ~2GB total disk usage
deploy:
  resources:
    limits:
      memory: 2G
      cpus: '1.0'
    reservations:
      memory: 1G
      cpus: '0.5'
```

## 📤 Deploying with Pre-built Data

To avoid the initial 4-6 hour build time, upload pre-built data:

### Required Directory Structure

```
mcp-server/vectorstore/
├── chroma.sqlite3
└── f37d385c-7440-4910-8750-dd16e49bbf24/  # UUID folder (exact name varies)
    ├── data_level0.bin            # ~1.9GB
    ├── header.bin
    ├── index_metadata.pickle
    ├── length.bin
    └── link_lists.bin

.hashes/
├── content_hashes.json      # SHA-256 hashes
├── embedding_hashes.json    # Embedding hashes
├── etag_cache.json         # Apple server ETags
└── url_content_map.json    # URL mappings

documentation/              # Optional (only if KEEP_MARKDOWN_FILES=true)
├── SwiftUI/
├── UIKit/
├── Foundation/
└── ... (300+ framework folders)
```

### Upload Process

```bash
# 1. Start container first
cd mcp-server
docker-compose up -d

# 2. Wait for initialization
docker logs -f apple-docs-mcp
# Ctrl+C when you see "Starting services with supervisor..."

# 3. Upload vectorstore (MUST include UUID folder)
docker cp vectorstore/. apple-docs-mcp:/data/vectorstore/

# 4. Upload hashes
docker cp ../.hashes/. apple-docs-mcp:/data/hashes/

# 5. (Optional) Upload documentation
docker cp ../documentation/. apple-docs-mcp:/data/documentation/

# 6. Restart to recognize data
docker-compose restart

# 7. Verify data loaded
docker exec apple-docs-mcp python -c "
import chromadb
client = chromadb.PersistentClient('/data/vectorstore')
collection = client.get_collection('apple_docs')
print(f'Documents in collection: {collection.count()}')
"
# Should show: Documents in collection: 323118
```

## 📅 Automatic Updates

The container automatically rescrapes Apple's documentation:
- **Schedule**: Every Sunday at 1:00 AM
- **Method**: Uses ETags for efficient change detection
- **Cost**: ~$0.10-0.25 per update (only changed docs)
- **Duration**: 30-60 minutes typically

### Manual Update

```bash
# Force immediate update
docker exec apple-docs-mcp python /app/scraper/auto_scrape_and_embed.py --embed --yes

# Check last update time
docker exec apple-docs-mcp cat /data/hashes/last_update.txt
```

## 🔍 Monitoring & Maintenance

### Service Status

```bash
# View all services
docker exec apple-docs-mcp supervisorctl status

# Expected output:
# mcp-server    RUNNING   pid 123, uptime 1:23:45
# scheduler     RUNNING   pid 124, uptime 1:23:45
```

### Log Management

```bash
# View all logs
docker logs -f apple-docs-mcp

# MCP server logs only
docker exec apple-docs-mcp tail -f /data/logs/mcp-server.log

# Scheduler logs only
docker exec apple-docs-mcp tail -f /data/logs/scheduler.log

# Search logs for errors
docker exec apple-docs-mcp grep ERROR /data/logs/*.log
```

### Health Monitoring

```bash
# Detailed health check
curl -v -H "Authorization: Bearer $MCP_API_KEY" $MCP_SERVER_URL/health

# Self-test suite
docker exec apple-docs-mcp python /app/scripts/self_test.py

# Check container health
docker ps --filter name=apple-docs-mcp --format "table {{.Names}}\t{{.Status}}"
```

## 📦 Backup & Recovery

### Create Backups

```bash
# Backup vectorstore (most critical)
docker run --rm -v apple-docs-vectorstore:/data \
  -v $(pwd):/backup alpine \
  tar czf /backup/vectorstore-$(date +%Y%m%d).tar.gz -C /data .

# Backup hashes
docker run --rm -v apple-docs-hashes:/data \
  -v $(pwd):/backup alpine \
  tar czf /backup/hashes-$(date +%Y%m%d).tar.gz -C /data .

# Backup logs (optional)
docker run --rm -v apple-docs-logs:/data \
  -v $(pwd):/backup alpine \
  tar czf /backup/logs-$(date +%Y%m%d).tar.gz -C /data .
```

### Restore from Backup

```bash
# Stop container first
docker-compose down

# Restore vectorstore
docker run --rm -v apple-docs-vectorstore:/data \
  -v $(pwd):/backup alpine \
  tar xzf /backup/vectorstore-20240115.tar.gz -C /data

# Restore hashes
docker run --rm -v apple-docs-hashes:/data \
  -v $(pwd):/backup alpine \
  tar xzf /backup/hashes-20240115.tar.gz -C /data

# Restart container
docker-compose up -d
```

## 🐛 Troubleshooting

### Container Won't Start

```bash
# Check logs
docker logs apple-docs-mcp

# Common issues:
# - Missing OPENAI_API_KEY: Add to .env file
# - Missing MCP_API_KEY: Add to .env file
# - Port 8080 in use: Change MCP_PORT in .env
# - Invalid .env format: Check for quotes and spaces
```

### Search Returns No Results

```bash
# Verify document count
curl -H "Authorization: Bearer $MCP_API_KEY" $MCP_SERVER_URL/health

# If count is 0, rebuild index:
docker exec apple-docs-mcp python /app/scripts/build_index.py --force

# Check for search errors
docker exec apple-docs-mcp tail -n 50 /data/logs/mcp-server.log | grep ERROR
```

### High Memory Usage

```bash
# Check memory usage
docker stats apple-docs-mcp

# Restart to clear memory
docker-compose restart

# Set memory limits in docker-compose.yml:
deploy:
  resources:
    limits:
      memory: 2G
```

### Disk Space Issues

```bash
# Check volume sizes
docker system df -v | grep apple-docs

# Clean up if KEEP_MARKDOWN_FILES=false
docker exec apple-docs-mcp find /data/documentation -name "*.md" -delete

# Prune unused Docker resources
docker system prune -a --volumes
```

## 🚢 Production Deployment

### 1. Reverse Proxy Setup (Nginx Example)

```nginx
server {
    listen 443 ssl http2;
    server_name docs-api.yourdomain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # SSE support
        proxy_set_header Connection '';
        proxy_http_version 1.1;
        chunked_transfer_encoding off;
        proxy_buffering off;
        proxy_cache off;
    }
}
```

### 2. Production Docker Compose Override

Create `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  apple-docs-mcp:
    restart: always
    environment:
      - KEEP_MARKDOWN_FILES=false
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

Deploy with: `docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d`

### 3. Monitoring Setup

```bash
# Create monitoring script
cat > monitor.sh << 'EOF'
#!/bin/bash
HEALTH_URL="${MCP_SERVER_URL}/health"
SLACK_WEBHOOK="your-slack-webhook-url"

# Check health
RESPONSE=$(curl -s -H "Authorization: Bearer $MCP_API_KEY" $HEALTH_URL)
STATUS=$(echo $RESPONSE | jq -r .status)

if [ "$STATUS" != "healthy" ]; then
    curl -X POST $SLACK_WEBHOOK -H 'Content-type: application/json' \
        --data "{\"text\":\"⚠️ Apple Docs MCP Server is unhealthy: $RESPONSE\"}"
fi
EOF

# Add to crontab
*/5 * * * * /path/to/monitor.sh
```

## 📊 Success Metrics

Your deployment is successful when:

- ✅ Health endpoint returns `{"status": "healthy", "vectorstore": {"document_count": 323118}}`
- ✅ Search queries return relevant results in <500ms
- ✅ Self-tests pass: `All tests passed!`
- ✅ Weekly updates complete without errors
- ✅ No ERROR entries in logs
- ✅ Memory usage stays under 2GB
- ✅ CPU usage stays under 50% during normal operation

## 🆘 Support & Debugging

### Quick Diagnostics

```bash
# Run full diagnostic suite
docker exec apple-docs-mcp bash -c '
echo "=== Service Status ==="
supervisorctl status
echo -e "\n=== Health Check ==="
curl -s http://localhost:8080/health | jq .
echo -e "\n=== Document Count ==="
python -c "import chromadb; c=chromadb.PersistentClient(\"/data/vectorstore\"); print(f\"Documents: {c.get_collection(\"apple_docs\").count()}\")"
echo -e "\n=== Recent Errors ==="
grep ERROR /data/logs/*.log | tail -5 || echo "No errors found"
echo -e "\n=== Disk Usage ==="
df -h /data
'
```

### Common Solutions

1. **"No module named X" errors**: Rebuild container
2. **"Collection not found" errors**: Vectorstore not uploaded correctly
3. **"Unauthorized" errors**: Check MCP_API_KEY in requests
4. **Slow searches**: Restart container to clear cache
5. **Update failures**: Check OPENAI_API_KEY is valid

### Advanced Debugging

```bash
# Interactive shell
docker exec -it apple-docs-mcp /bin/bash

# Python REPL with imports
docker exec -it apple-docs-mcp python

# Test specific components
docker exec apple-docs-mcp python -m pytest /app/tests/test_rag.py -v
```

---

**Deployment complete! Your Apple Docs MCP Server is ready for production use.** 🎉

For updates and issues, check the [GitHub repository](https://github.com/Averyy/apple-dev-docs).