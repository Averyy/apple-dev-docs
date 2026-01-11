# Automated Doc Scraping Plan

## Current State
- Documentation is **pre-baked into Docker image** at build time
- A `schedule_rescrape_v2.py` script **already exists** but isn't active
- Scraper runs locally, then you commit + push to trigger a rebuild/deploy

## Three Options

### Option 1: GitHub Actions Scheduled Workflow (Recommended)
**How it works:** GitHub runs the scraper on a schedule, commits changes, triggers rebuild.

```yaml
# .github/workflows/scheduled-scrape.yml
on:
  schedule:
    - cron: '0 5 * * 0'  # Every Sunday at midnight EST
  workflow_dispatch:      # Manual trigger button

jobs:
  scrape-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - checkout repo
      - setup python, install deps
      - run scraper (scrape.py --all --yes)
      - run swift docs scraper
      - commit if changes exist
      - trigger docker-build workflow
```

**Pros:**
- Fully automated end-to-end
- Logs visible in GitHub Actions UI
- No VPS access needed
- Free (within GitHub Actions limits)
- Manual trigger button for on-demand updates

**Cons:**
- Scraping takes 3-6 hours (may hit Actions time limits - 6hr max)
- Adds ~500MB to repo if committing scraped docs
- More complex workflow

---

### Option 2: VPS Cron Job (Simplest)
**How it works:** Cron on your VPS runs docker exec to trigger scraping inside container.

```bash
# Add to VPS crontab
0 2 * * 0 docker exec apple-docs-mcp python /app/scripts/schedule_rescrape_v2.py >> /var/log/apple-docs-scrape.log 2>&1
```

**Pros:**
- Dead simple - one line
- Uses existing script
- No image rebuild needed (scrapes + reindexes live)
- Fast to implement

**Cons:**
- Requires scraper to be included in Docker image (currently it's not)
- Tied to VPS - if you migrate, need to reconfigure
- Logs on VPS, not centralized

---

### Option 3: Supervisor Process in Docker
**How it works:** Add scheduler as a supervised process that runs inside the container.

```ini
# Add to supervisord.conf
[program:rescrape-scheduler]
command=python /app/scripts/schedule_rescrape_v2.py
autostart=true
autorestart=true
stdout_logfile=/data/logs/scheduler.log
```

**Pros:**
- Self-contained - container manages everything
- Survives container restarts
- Already has scheduling logic (Sundays 1 AM)

**Cons:**
- Requires scraper dependencies in image (bloats it)
- Harder to debug
- Less visibility into when things run

---

## Decision

**Going with Option 1 (GitHub Actions)** because:
- Repo is public → unlimited free minutes
- Auto-commits changes to repo (keeps git as source of truth)
- Triggers existing deploy pipeline automatically
- Manual trigger button for on-demand updates
- Full visibility in Actions UI

**Pending:** Confirm scrape time is under 6 hours

---

## Implementation

### Files to create/modify:
- `.github/workflows/scheduled-scrape.yml` - New workflow (full content below)
- `mcp-server/scripts/startup_check.py` - Change `FORCE_REBUILD_DAYS = 30` to `7` (line 19)
- `requirements.txt` - Add `aiohttp>=3.9.0` (missing dependency for Swift docs scraper)
- `scripts/utilities/cleanup_removed_frameworks.py` - New script to clean up frameworks Apple has removed

### Complete Workflow File

```yaml
name: Scheduled Documentation Scrape

on:
  schedule:
    # Every Sunday at 5:00 AM UTC (midnight EST)
    - cron: '0 5 * * 0'
  workflow_dispatch:  # Manual trigger button

# Prevent multiple scrape runs from overlapping
concurrency:
  group: scrape-docs
  cancel-in-progress: false  # Let running scrape finish

jobs:
  scrape-docs:
    runs-on: ubuntu-latest
    timeout-minutes: 360  # 6 hour limit

    permissions:
      contents: write  # Needed to push commits

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Clean up removed frameworks
        run: python scripts/utilities/cleanup_removed_frameworks.py

      - name: Run Apple frameworks scraper
        run: python scrape.py --all --yes --cleanup-orphans --auto-cleanup

      - name: Run Swift language docs scraper
        run: python scripts/scrape_swift_docs.py

      - name: Check for changes
        id: changes
        run: |
          git add -A
          if git diff --staged --quiet; then
            echo "has_changes=false" >> $GITHUB_OUTPUT
            echo "No documentation changes detected"
          else
            echo "has_changes=true" >> $GITHUB_OUTPUT
            echo "Documentation changes detected:"
            git diff --staged --stat | tail -20
          fi

      - name: Update landing page and sitemap dates
        if: steps.changes.outputs.has_changes == 'true'
        run: |
          # Update landing page "Updated Weekly" date
          MONTH_DAY=$(date +"%-b %-d")  # e.g., "Jan 11"
          sed -i "s|<div class=\"stat-value\">[A-Za-z]\{3\} [0-9]\{1,2\}</div>|<div class=\"stat-value\">${MONTH_DAY}</div>|" landing/index.html

          # Update sitemap lastmod
          TODAY=$(date +"%Y-%m-%d")  # e.g., "2026-01-11"
          sed -i "s|<lastmod>[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}</lastmod>|<lastmod>${TODAY}</lastmod>|" landing/sitemap.xml

          git add landing/index.html landing/sitemap.xml

      - name: Commit and push changes
        if: steps.changes.outputs.has_changes == 'true'
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git commit -m "Automated docs update $(date +'%Y-%m-%d')"
          git push

      - name: Summary
        run: |
          echo "## Documentation Scrape Complete" >> $GITHUB_STEP_SUMMARY
          echo "" >> $GITHUB_STEP_SUMMARY
          if [ "${{ steps.changes.outputs.has_changes }}" == "true" ]; then
            echo "Changes detected and committed. Docker build will trigger automatically." >> $GITHUB_STEP_SUMMARY
          else
            echo "No changes detected. Documentation is up to date." >> $GITHUB_STEP_SUMMARY
          fi
```

### How it works:
1. Runs every Sunday at midnight EST (5 AM UTC) (or manual trigger)
2. Checks out repo, installs Python deps
3. Runs both scrapers (Apple frameworks + Swift docs)
4. If files changed → commits and pushes to main
5. Push to main triggers existing `docker-build.yml` → rebuild → deploy

### No changes needed to docker-build.yml
The existing workflow already triggers on push to main, so the scrape workflow just needs to push and the deploy happens automatically.

### Hash files (already tracked)
The `.hashes/` directory stores ETags and content hashes for incremental scraping. These are already tracked in git (only `meilisearch_hashes.json` is gitignored). This means subsequent GitHub Actions runs will use the existing hashes and only re-scrape changed docs.

---

## Notes

### How Meilisearch gets updated
1. Scraper updates `documentation/` folder → committed to repo
2. Docker build bakes `documentation/` into image (Dockerfile line 69)
3. VPS pulls new image → container restarts
4. `startup_check.py` runs → calls `index_to_meilisearch.py`
5. With `FORCE_REBUILD_DAYS = 7`, weekly deploys trigger full rebuild
6. Deleted docs get cleaned up from Meilisearch automatically

### Error handling
If scraping fails partway through, the workflow fails and no commit happens. GitHub sends email notifications for failed workflows by default.

### Fallback if >6 hours
If timing is tight, could split into two separate workflows. But try single workflow first - incremental scraping should be much faster than initial run since ETags skip unchanged docs.

### Concurrent scrapers
Default is 20 concurrent. This is already aggressive for Apple's API - don't increase without testing.

### Branch protection
If `main` branch has protection rules requiring PR reviews, the automated push will fail. Verify no PR requirement is set, or add a bypass for github-actions[bot].

### Orphan cleanup (pages within frameworks)
The `--cleanup-orphans --auto-cleanup` flags enable automatic deletion of pages that Apple has removed from active frameworks. Safety check prevents deleting >50% of a framework's files.

### Removed frameworks cleanup
**Problem:** When Apple removes an entire framework from `technologies.json`, the existing orphan cleanup doesn't catch it because:
- The framework's hash file has an old session_id
- All files appear "touched" based on that old session
- Neither the hash file nor documentation folder gets cleaned up

**Solution:** Add a pre-scrape step that compares existing hash files against Apple's current framework list and removes orphaned frameworks.

See "Implementation Checklist → 4. Create removed frameworks cleanup script" below.

### New frameworks
New frameworks are automatically discovered - the scraper fetches the framework list from Apple's `technologies.json` API each run.

### Swift docs
The Swift language docs scraper now automatically cleans up orphaned files (pages removed from swift-book).

### Health endpoint metadata ✅ DONE

Added `last_checked` and `last_updated` timestamps to the health endpoint:

```json
{
  "status": "healthy",
  "service": "apple-docs-mcp",
  "version": "2.0.0",
  "meilisearch": "connected",
  "frameworks": 373,
  "documents": 334813,
  "last_checked": "2026-01-18T12:00:00.000000Z",
  "last_updated": "2026-01-11T16:54:32.123456Z"
}
```

- **`last_checked`**: Updates every time the indexer runs (even if no changes) - verifies scraper is running on schedule
- **`last_updated`**: Only updates when actual content was indexed

**Files modified:**
- `scripts/index_to_meilisearch.py` - Added `update_metadata()` method, stores in `apple-docs-meta` index
- `mcp-server/apple_docs_mcp.py` - Added `get_index_metadata()` function and updated health endpoint

---

## Verification

After implementation:
1. Manually trigger the workflow via Actions UI → "Run workflow" button
2. Watch the logs for ~4-5 hours
3. Check if commit appears in repo history
4. Verify docker-build triggered and deployed
5. Check https://xdocs.dev/health for updated document count
6. Verify landing page shows new "Last Updated" date

---

## Implementation Checklist

When ready to implement, make these changes:

### 1. Add missing dependency to requirements.txt (CRITICAL)
```
aiohttp>=3.9.0
```
The Swift docs scraper imports aiohttp but it's not in requirements.txt. GitHub Actions will fail without this.

### 2. Update FORCE_REBUILD_DAYS in startup_check.py
File: `mcp-server/scripts/startup_check.py` line 19
```python
# Change from:
FORCE_REBUILD_DAYS = 30

# To:
FORCE_REBUILD_DAYS = 7
```

### 3. Create the workflow file
Create `.github/workflows/scheduled-scrape.yml` with the YAML from the "Complete Workflow File" section above.

**Note:** The workflow includes `--cleanup-orphans --auto-cleanup` to remove pages that Apple has deleted.

### 4. Create removed frameworks cleanup script ✅ DONE

Created `scripts/utilities/cleanup_removed_frameworks.py` with improvements over original plan:

**Key features:**
- Fetches Apple's `technologies.json` to find candidates not in list
- **HTTP verification** (404/redirect check) before deletion - prevents false positives
- Protects `Swift-Book` (ours, not from Apple)
- Excludes non-framework hash files (`meilisearch_hashes.json`, `swift_docs_hashes.json`)
- Case-insensitive matching with correct path handling
- `--dry-run` for preview, `--yes` for automation, `--verbose` for details

**Usage:**
```bash
python scripts/utilities/cleanup_removed_frameworks.py --dry-run  # Preview
python scripts/utilities/cleanup_removed_frameworks.py            # Interactive (y/N prompt)
python scripts/utilities/cleanup_removed_frameworks.py --yes      # Automated (no prompt)
```

**Safety:** Only deletes frameworks that:
1. Are NOT in Apple's technologies.json, AND
2. Return 404 or redirect from Apple's website

This prevents accidental deletion of docs that exist but aren't listed in technologies.json (e.g., `touchcontrols`).

### 5. Add cleanup step to workflow
Update the workflow to run the cleanup script before scraping:

```yaml
      - name: Clean up removed frameworks
        run: python scripts/utilities/cleanup_removed_frameworks.py --yes
```

Add this step **before** "Run Apple frameworks scraper" in the workflow YAML.
