#!/bin/bash
# Quick deployment script for Apple Docs MCP Server
# Run this on your server after setting up GitHub Actions

set -e

# Configuration
GITHUB_USERNAME="yourusername"
REPO_NAME="apple-developer-docs"
DATA_DIR="/opt/apple-docs-mcp/data"
GITHUB_TOKEN="${GITHUB_TOKEN}"
OPENAI_API_KEY="${OPENAI_API_KEY}"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}Apple Docs MCP Server - Quick Deploy${NC}"
echo "======================================"

# Check prerequisites
echo -e "\n${BLUE}Checking prerequisites...${NC}"

if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed${NC}"
    exit 1
fi

if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${RED}❌ GITHUB_TOKEN environment variable not set${NC}"
    echo "Please set: export GITHUB_TOKEN=your-token"
    exit 1
fi

if [ -z "$OPENAI_API_KEY" ]; then
    echo -e "${RED}❌ OPENAI_API_KEY environment variable not set${NC}"
    echo "Please set: export OPENAI_API_KEY=your-key"
    exit 1
fi

if [ -z "$MCP_API_KEY" ]; then
    echo -e "${RED}❌ MCP_API_KEY environment variable not set${NC}"
    echo "Generate one with: openssl rand -hex 32"
    echo "Then set: export MCP_API_KEY=your-generated-key"
    exit 1
fi

echo -e "${GREEN}✓ All prerequisites met${NC}"

# Create Docker volumes for persistence
echo -e "\n${BLUE}Setting up Docker volumes...${NC}"
docker volume create apple-docs-vectorstore
docker volume create apple-docs-metadata
docker volume create apple-docs-scraped
docker volume create apple-docs-logs
echo -e "${GREEN}✓ Created persistent Docker volumes${NC}"

# Login to GitHub Container Registry
echo -e "\n${BLUE}Logging in to GitHub Container Registry...${NC}"
echo $GITHUB_TOKEN | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin
echo -e "${GREEN}✓ Logged in successfully${NC}"

# Pull latest image
echo -e "\n${BLUE}Pulling latest Docker image...${NC}"
docker pull ghcr.io/$GITHUB_USERNAME/$REPO_NAME-mcp:latest

# Stop existing container if running
if [ "$(docker ps -q -f name=apple-docs-mcp)" ]; then
    echo -e "\n${BLUE}Stopping existing container...${NC}"
    docker stop apple-docs-mcp
    docker rm apple-docs-mcp
    echo -e "${GREEN}✓ Stopped existing container${NC}"
fi

# Run MCP server with persistent volumes (no ports needed - STDIO communication)
echo -e "\n${BLUE}Starting MCP server...${NC}"
docker run -d \
  --name apple-docs-mcp \
  -v apple-docs-vectorstore:/data/vectorstore \
  -v apple-docs-metadata:/data/metadata \
  -v apple-docs-scraped:/data/scraped \
  -v apple-docs-logs:/var/log/supervisor \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  -e MCP_API_KEY=$MCP_API_KEY \
  --restart unless-stopped \
  ghcr.io/$GITHUB_USERNAME/$REPO_NAME-mcp:latest

echo -e "${GREEN}✓ MCP server started${NC}"


# Check if vector database exists in volume
echo -e "\n${BLUE}Checking vector database...${NC}"

# Give container a moment to extract pre-built data if needed
sleep 5

# Check container logs to see initialization status
echo -e "${BLUE}Container initialization:${NC}"
docker logs apple-docs-mcp | tail -20

# Check if vectorstore exists now
VECTOR_EXISTS=$(docker exec apple-docs-mcp test -d /data/vectorstore && echo "true" || echo "false")

if [ "$VECTOR_EXISTS" = "true" ]; then
    # Try to get document count
    DOC_COUNT=$(docker exec apple-docs-mcp python -c "
import chromadb
try:
    db = chromadb.PersistentClient('/data/vectorstore')
    collection = db.get_collection('apple_docs')
    print(collection.count())
except:
    print('0')
    " 2>/dev/null || echo "0")
    
    if [ "$DOC_COUNT" -gt 0 ]; then
        echo -e "${GREEN}✓ Vector database ready with $DOC_COUNT documents${NC}"
    else
        echo -e "${BLUE}Vector database exists but is empty${NC}"
        echo -e "${BLUE}The scheduler will build it at midnight or run:${NC}"
        echo -e "${BLUE}  docker exec apple-docs-mcp python /app/scripts/auto_rescrape_and_embed.py${NC}"
    fi
else
    echo -e "${BLUE}No vector database found yet${NC}"
    echo -e "${BLUE}If the image has pre-built data, it's still extracting...${NC}"
    echo -e "${BLUE}Otherwise, run: docker exec apple-docs-mcp python /app/scripts/auto_rescrape_and_embed.py${NC}"
fi

# Test MCP server health
echo -e "\n${BLUE}Testing MCP server health...${NC}"
sleep 3
if docker exec apple-docs-mcp pgrep -f "mcp_server" > /dev/null; then
    echo -e "${GREEN}✓ MCP server is running${NC}"
    
    # Show process info
    echo -e "\n${BLUE}Server Processes:${NC}"
    docker exec apple-docs-mcp supervisorctl status
else
    echo -e "${RED}❌ MCP server not running${NC}"
    echo "Check logs with: docker logs apple-docs-mcp"
fi

# Show connection info
echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}✅ Deployment Complete!${NC}"
echo -e "${GREEN}========================================${NC}"
echo
echo "To use with any MCP client, add to config:"
echo "Examples:"
echo
echo "Claude Desktop: ~/Library/Application Support/Claude/claude_desktop_config.json"
echo "Cursor: Check Cursor's MCP documentation"
echo "Claude Code: Via MCP configuration"
echo
echo '{'
echo '  "mcpServers": {'
echo '    "apple-docs": {'
echo '      "type": "sse",'
echo '      "url": "http://192.168.2.99:8080/mcp",'
echo '      "headers": {'
echo '        "Authorization": "Bearer your-mcp-api-key-here"'
echo '      }'
echo '    }'
echo '  }'
echo '}'
echo
echo "Note: API keys are configured on the server via environment variables"
echo "Use the same MCP_API_KEY in your client config above"
echo
echo "Useful commands:"
echo "  View logs:         docker logs -f apple-docs-mcp"
echo "  Manual update:     docker exec apple-docs-mcp python scripts/incremental_update.py"
echo "  Force rebuild:     docker exec apple-docs-mcp python /app/scripts/auto_rescrape_and_embed.py"
echo "  Stop server:       docker stop apple-docs-mcp"
echo "  Start server:      docker start apple-docs-mcp"
echo
echo -e "${BLUE}Updates: Pull new image and restart container manually${NC}"