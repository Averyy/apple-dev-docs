# First, make sure MCPs are installed (run these individually as needed)

claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem
claude mcp add puppeteer -- npx -y @modelcontextprotocol/server-puppeteer

# Configure global Claude settings (run as needed)

claude config set -g theme dark
claude config set -g preferredNotifChannel iterm2
claude config set -g autoUpdaterStatus enabled