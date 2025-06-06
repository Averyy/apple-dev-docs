# highlightNextResult(in:)

**Framework**: UIKit  
**Kind**: method

Updates the highlighted result to the next or previous match.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func highlightNextResult(in direction: UITextStorageDirection)
```

#### Discussion

The system calls this method when a person taps the next or previous button, or enters `Return` or `Shift+Return` on a hardware keyboard while the search field has focus.

## Parameters

- `direction`: The direction, either forward or backward, to move through the search results.

## See Also

- [func performSearch(query: String, options: UITextSearchOptions?)](uifindsession/performsearch(query:options:).md)
  Initiates a search for the query string you provide.
- [func performSingleReplacement(query: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/performsinglereplacement(query:replacementstring:options:).md)
  Replaces a single instance of the query string with the replacement string you provide.
- [func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/replaceall(searchquery:replacementstring:options:).md)
  Replaces all matching instances of the query string with the replacement string you provide.
- [func invalidateFoundResults()](uifindsession/invalidatefoundresults.md)
  Invalidates the found ranges and updates the system find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/highlightnextresult(in:))*