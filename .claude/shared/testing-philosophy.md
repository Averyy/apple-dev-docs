# Testing Philosophy

## Core Principles

1. **Test Critical Functionality Only**
   - Focus on tests that prevent data loss
   - Test features that could cause incorrect scraping
   - Avoid slow integration tests unless absolutely necessary

2. **Fast Feedback**
   - Tests should run in seconds, not minutes
   - Use mocking for external API calls
   - No actual network requests in unit tests

3. **Prevent Regressions**
   - Test bugs we've already fixed
   - Test edge cases that broke production

## Critical Tests We Maintain

### 1. Path Generation Tests (`test_critical_sync.py`)
- **No Double Nesting**: Prevents `watchkit/foo/foo.md` bug
- **Case Insensitive Parsing**: Handles `WatchKit` vs `watchkit`
- **Cross-Framework References**: Prevents UIKit files in WatchKit folder

### 2. URL Conversion Tests
- **JSON URL Generation**: Ensures we can fetch Apple's data
- **Filename Safety**: Prevents filesystem-breaking characters
- **Recursive Discovery**: Tests framework traversal logic

### 3. ETag Optimization Tests (Built into critical sync tests)
- **ETag Storage**: Verifies ETags are saved and retrieved
- **Change Detection**: Ensures unchanged content is skipped
- **Hash Fallback**: Tests backup mechanism when ETags fail

## What We DON'T Test

1. **Full Scraping Runs**: Too slow, test components instead
2. **Network Requests**: Mock them or test separately
3. **UI/Presentation**: Focus on data correctness
4. **Performance**: Manual testing is sufficient

## Running Tests

### Standalone Tests (Recommended)
```bash
# Run critical tests without external dependencies
python3 tests/test_critical_sync.py

# Or use the test runner for better output
python3 tests/run_critical_tests.py
```

> **Note**: We've removed pytest-based tests to eliminate dependency issues and focus on reliable standalone testing.

## Adding New Tests

Before adding a test, ask:
1. Does this prevent data loss or incorrect scraping?
2. Is this a regression we've seen in production?
3. Can this test run in <1 second?

If no to any of these, reconsider if the test is necessary.