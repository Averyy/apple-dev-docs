#!/usr/bin/env python3
"""Debug scraper hanging with timeout and stack trace"""

import asyncio
import sys
import threading
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from scraper.json_scraper import AppleJSONDocumentationScraper
from scraper.utils.logger import get_logger

logger = get_logger(__name__)

# Global to store the scraper task
scraper_task = None

def print_stack_traces():
    """Print stack traces of all threads"""
    print("\n" + "="*80)
    print("TIMEOUT: Printing stack traces of all threads")
    print("="*80)
    
    for thread_id, frame in sys._current_frames().items():
        print(f"\nThread {thread_id}:")
        traceback.print_stack(frame)

async def test_with_timeout(framework_id: str, timeout_seconds: int = 300):
    """Test scraping with a timeout"""
    global scraper_task
    
    print(f"🧪 Testing {framework_id} scraping with {timeout_seconds}s timeout")
    
    # Set up a timer to print stack traces
    timer = threading.Timer(timeout_seconds, print_stack_traces)
    timer.start()
    
    try:
        async with AppleJSONDocumentationScraper(framework_id) as scraper:
            # Create the scraping task
            scraper_task = asyncio.create_task(scraper.discover_and_scrape_streaming())
            
            # Wait for it with timeout
            await asyncio.wait_for(scraper_task, timeout=timeout_seconds)
            
            # Cancel timer if we finished
            timer.cancel()
            
            print(f"\n✅ Completed successfully!")
            print(f"Pages scraped: {scraper.stats.get('pages_scraped', 0)}")
            print(f"Pages skipped: {scraper.stats.get('pages_skipped', 0)}")
            print(f"Pages failed: {scraper.stats.get('pages_failed', 0)}")
            
    except asyncio.TimeoutError:
        print(f"\n⏰ Timeout after {timeout_seconds} seconds!")
        # The timer will print stack traces
        # Cancel the scraping task
        if scraper_task and not scraper_task.done():
            scraper_task.cancel()
            try:
                await scraper_task
            except asyncio.CancelledError:
                pass
    except Exception as e:
        timer.cancel()
        print(f"\n❌ Exception: {e}")
        traceback.print_exc()

async def main():
    if len(sys.argv) < 2:
        print("Usage: python debug_hang_with_timeout.py <framework_id> [timeout_seconds]")
        print("Example: python debug_hang_with_timeout.py accelerate 60")
        sys.exit(1)
    
    framework_id = sys.argv[1]
    timeout = int(sys.argv[2]) if len(sys.argv) > 2 else 300
    
    await test_with_timeout(framework_id, timeout)

if __name__ == "__main__":
    asyncio.run(main())