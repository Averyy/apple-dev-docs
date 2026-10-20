# invalidateFoundResults()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Invalidates the found ranges and updates the system find panel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func invalidateFoundResults()
```

```objc
- (void) invalidateFoundResults;
```

#### Discussion

If the [`searchText`](../uifindinteraction/searchtext.md) for the find interaction is non-empty, a call to this method this triggers a call to [`performSearch(query:options:)`](./performsearch%28query,options%29.md) immediately after to begin a new search.

## See Also

### Managing session interactions
- [func performSearch(query: String, options: UITextSearchOptions?)](./performsearch%28query,options%29.md)
  Initiates a search for the query string you provide.
- [func performSingleReplacement(query: String, replacementString: String, options: UITextSearchOptions?)](./performsinglereplacement%28query,replacementstring,options%29.md)
  Replaces a single instance of the query string with the replacement string you provide.
- [func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)](./replaceall%28searchquery,replacementstring,options%29.md)
  Replaces all matching instances of the query string with the replacement string you provide.
- [func highlightNextResult(in: UITextStorageDirection)](./highlightnextresult%28in%29.md)
  Updates the highlighted result to the next or previous match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/invalidatefoundresults())*