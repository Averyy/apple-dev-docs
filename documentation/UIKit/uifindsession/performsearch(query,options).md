# performSearch(query:options:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Initiates a search for the query string you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func performSearch(query: String, options: UITextSearchOptions?)
```

```objc
- (void) performSearchWithQuery:(NSString *) query options:(UITextSearchOptions *) options;
```

## Discussion

The system calls this method when the user initiates a search for a string in your app’s text content.

## Parameters

- `query`: The string to search, the user provides through the search text field of the system find panel.
- `options`: The object containing all the configurable options for the search.

## See Also

### Managing session interactions
- [func performSingleReplacement(query: String, replacementString: String, options: UITextSearchOptions?)](./performsinglereplacement%28query,replacementstring,options%29.md)
  Replaces a single instance of the query string with the replacement string you provide.
- [func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)](./replaceall%28searchquery,replacementstring,options%29.md)
  Replaces all matching instances of the query string with the replacement string you provide.
- [func highlightNextResult(in: UITextStorageDirection)](./highlightnextresult%28in%29.md)
  Updates the highlighted result to the next or previous match.
- [func invalidateFoundResults()](./invalidatefoundresults%28%29.md)
  Invalidates the found ranges and updates the system find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/performsearch(query:options:))*