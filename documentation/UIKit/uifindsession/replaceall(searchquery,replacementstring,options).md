# replaceAll(searchQuery:replacementString:options:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Replaces all matching instances of the query string with the replacement string you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)
```

```objc
- (void) replaceAllInstancesOfSearchQuery:(NSString *) searchQuery withReplacementString:(NSString *) replacementString options:(UITextSearchOptions *) options;
```

## Parameters

- `searchQuery`: The string to search for and replace, the user provides through the search text field of the system find panel.
- `replacementString`: The replacement string, the user provides through the replace text field of the system find panel.
- `options`: The object containing all the configurable options for the search.

## See Also

### Managing session interactions
- [func performSearch(query: String, options: UITextSearchOptions?)](./performsearch%28query,options%29.md)
  Initiates a search for the query string you provide.
- [func performSingleReplacement(query: String, replacementString: String, options: UITextSearchOptions?)](./performsinglereplacement%28query,replacementstring,options%29.md)
  Replaces a single instance of the query string with the replacement string you provide.
- [func highlightNextResult(in: UITextStorageDirection)](./highlightnextresult%28in%29.md)
  Updates the highlighted result to the next or previous match.
- [func invalidateFoundResults()](./invalidatefoundresults%28%29.md)
  Invalidates the found ranges and updates the system find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/replaceall(searchquery:replacementstring:options:))*