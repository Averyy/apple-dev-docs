# performSingleReplacement(query:replacementString:options:)

**Framework**: UIKit  
**Kind**: method

Replaces a single instance of the query string with the replacement string you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performSingleReplacement(query searchQuery: String, replacementString: String, options: UITextSearchOptions?)
```

#### Discussion

The system calls this method when the user initiates the replacement the text for a single match of a string in your app’s text content with the replacement string.

## Parameters

- `searchQuery`: The string to search for and replace, the user provides through the search text field of the system find panel.
- `replacementString`: The replacement string, the user provides through the replace text field of the system find panel.
- `options`: The object containing all the configurable options for the search.

## See Also

- [func performSearch(query: String, options: UITextSearchOptions?)](uifindsession/performsearch(query:options:).md)
  Initiates a search for the query string you provide.
- [func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)](uifindsession/replaceall(searchquery:replacementstring:options:).md)
  Replaces all matching instances of the query string with the replacement string you provide.
- [func highlightNextResult(in: UITextStorageDirection)](uifindsession/highlightnextresult(in:).md)
  Updates the highlighted result to the next or previous match.
- [func invalidateFoundResults()](uifindsession/invalidatefoundresults.md)
  Invalidates the found ranges and updates the system find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/performsinglereplacement(query:replacementstring:options:))*