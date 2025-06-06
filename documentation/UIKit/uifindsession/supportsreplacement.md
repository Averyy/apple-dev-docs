# supportsReplacement

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether to allow replacing find panel results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var supportsReplacement: Bool { get }
```

#### Discussion

This property determines whether the find panel shows the replacement UI.

The default value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var resultCount: Int](uifindsession/resultcount.md)
  The total number of results the search matches.
- [var highlightedResultIndex: Int](uifindsession/highlightedresultindex.md)
  The index of the result the find panel highlights.
- [var allowsReplacementForCurrentlyHighlightedResult: Bool](uifindsession/allowsreplacementforcurrentlyhighlightedresult.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.
- [var searchResultDisplayStyle: UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.property.md)
  The information the find panel includes in the summary of found results.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/supportsreplacement)*