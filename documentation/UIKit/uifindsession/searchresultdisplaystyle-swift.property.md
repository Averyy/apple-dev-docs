# searchResultDisplayStyle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The information the find panel includes in the summary of found results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var searchResultDisplayStyle: UIFindSession.SearchResultDisplayStyle { get set }
```

```objc
@property (nonatomic, readwrite) UIFindSessionSearchResultDisplayStyle searchResultDisplayStyle;
```

## See Also

### Getting session information
- [var resultCount: Int](./resultcount.md)
  The total number of results the search matches.
- [var highlightedResultIndex: Int](./highlightedresultindex.md)
  The index of the result the find panel highlights.
- [var supportsReplacement: Bool](./supportsreplacement.md)
  A Boolean value that indicates whether to allow replacing find panel results.
- [var allowsReplacementForCurrentlyHighlightedResult: Bool](./allowsreplacementforcurrentlyhighlightedresult.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.
- [UIFindSession.SearchResultDisplayStyle](./searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.
- [var allowsReplacement: Bool](./allowsreplacement.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/searchresultdisplaystyle-swift.property)*