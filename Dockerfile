# Multi-stage build for smaller final image
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Also install scraper requirements
COPY scraper/requirements.txt ./scraper-requirements.txt
RUN pip install --user --no-cache-dir -r scraper-requirements.txt

# Install MCP and scheduling dependencies
RUN pip install --user schedule fastmcp fastapi uvicorn[standard]

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Install supervisor to run multiple processes
RUN apt-get update && apt-get install -y \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local

# Make sure scripts are in PATH
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY server/ ./server/
COPY scripts/ ./scripts/
COPY scraper/ ./scraper/

# Create directories for persistent data
RUN mkdir -p /data/vectorstore /data/metadata /data/scraped /var/log/supervisor

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV VECTORSTORE_PATH=/data/vectorstore
ENV METADATA_PATH=/data/metadata
ENV DOCS_PATH=/data/scraped
ENV MCP_PORT=8080

# Expose HTTP port for remote access
EXPOSE 8080

# Health check for HTTP server
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || pgrep -f "mcp_server" > /dev/null || exit 1

# Create supervisor config
COPY <<EOF /etc/supervisor/conf.d/supervisord.conf
[supervisord]
nodaemon=true
user=root

[program:mcp-server]
command=python /app/server/mcp_server.py
directory=/app
autostart=true
autorestart=true
stderr_logfile=/var/log/supervisor/mcp-server.err.log
stdout_logfile=/var/log/supervisor/mcp-server.out.log

[program:scheduler]
command=python /app/scripts/schedule_rescrape.py
directory=/app
autostart=true
autorestart=true
stderr_logfile=/var/log/supervisor/scheduler.err.log
stdout_logfile=/var/log/supervisor/scheduler.out.log
EOF

# Copy pre-built data if available (optional - built during CI/CD)
# This gets copied to image but extracted to volume on first run
COPY build/vectorstore.tar.gz /app/prebuilt/vectorstore.tar.gz || true

# Add startup script with smart data handling
COPY <<EOF /app/start.sh
#!/bin/bash
set -e

echo "=== Apple Docs MCP Server Starting ==="

# Function to extract pre-built data
extract_prebuilt_data() {
    echo "Extracting pre-built vectorstore to volume..."
    cd /data
    tar -xzf /app/prebuilt/vectorstore.tar.gz
    echo "✓ Pre-built data extracted successfully"
    
    # Mark extraction complete
    touch /data/.initialized
}

# Check if this is first run (no data in volume)
if [ ! -f "/data/.initialized" ]; then
    echo "First run detected - checking for pre-built data..."
    
    if [ -f "/app/prebuilt/vectorstore.tar.gz" ]; then
        extract_prebuilt_data
    else
        echo "⚠️  No pre-built data found in image"
        echo "The scheduler will build the index at midnight or you can run:"
        echo "  docker exec apple-docs-mcp python /app/scripts/auto_rescrape_and_embed.py"
    fi
else
    echo "✓ Using existing data from Docker volume"
fi

# Show data statistics
if [ -d "/data/vectorstore" ]; then
    echo "Data volume stats:"
    echo "  Vectorstore: $(du -sh /data/vectorstore 2>/dev/null | cut -f1 || echo 'N/A')"
    echo "  Metadata: $(du -sh /data/metadata 2>/dev/null | cut -f1 || echo 'N/A')"
    echo "  Scraped docs: $(du -sh /data/scraped 2>/dev/null | cut -f1 || echo 'N/A')"
fi

# Check last update time
if [ -f "/data/metadata/last_update.txt" ]; then
    echo "Last update: $(cat /data/metadata/last_update.txt)"
else
    echo "No previous updates found"
fi

echo "Starting services..."
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
EOF

RUN chmod +x /app/start.sh

# Run supervisor to manage both MCP server and scheduler
CMD ["/app/start.sh"]