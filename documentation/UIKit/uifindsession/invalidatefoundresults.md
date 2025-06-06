# invalidateFoundResults()

**Framework**: UIKit  
**Kind**: method

Invalidates the found ranges and updates the system find panel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func invalidateFoundResults()
```

#### Discussion

If the [`searchText`](uifindinteraction/searchtext.md) for the find interaction is non-empty, a call to this method this triggers a call to [`performSearch(query:options:)`](uifindsession/performsearch(query:options:).md) immediately after to begin a new search.

## See Also

- [func performSearch(query: String, options: UITextSearchOptions?)](uifindsession/performsearch(query:options:).md)
  Initiates a search for the query string you provide.
- [func performSingleReplacement(query: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/performsinglereplacement(query:replacementstring:options:).md)
  Replaces a single instance of the query string with the replacement string you provide.
- [func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/replaceall(searchquery:replacementstring:options:).md)
  Replaces all matching instances of the query string with the replacement string you provide.
- [func highlightNextResult(in: UITextStorageDirection)](uifindsession/highlightnextresult(in:).md)
  Updates the highlighted result to the next or previous match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/invalidatefoundresults())*