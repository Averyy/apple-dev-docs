# performSearch(query:options:)

**Framework**: UIKit  
**Kind**: method

Initiates a search for the query string you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performSearch(query: String, options: UITextSearchOptions?)
```

#### Discussion

The system calls this method when the user initiates a search for a string in your app’s text content.

## Parameters

- `query`: The string to search, the user provides through the search text field of the system find panel.
- `options`: The object containing all the configurable options for the search.

## See Also

- [func performSingleReplacement(query: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/performsinglereplacement(query:replacementstring:options:).md)
  Replaces a single instance of the query string with the replacement string you provide.
- [func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/replaceall(searchquery:replacementstring:options:).md)
  Replaces all matching instances of the query string with the replacement string you provide.
- [func highlightNextResult(in: UITextStorageDirection)](uifindsession/highlightnextresult(in:).md)
  Updates the highlighted result to the next or previous match.
- [func invalidateFoundResults()](uifindsession/invalidatefoundresults.md)
  Invalidates the found ranges and updates the system find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/performsearch(query:options:))*