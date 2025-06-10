# highlightedResultIndex

**Framework**: UIKit  
**Kind**: property

The index of the result the find panel highlights.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var highlightedResultIndex: Int { get }
```

#### Discussion

To indicate no highlighted result, return `nil` (Swift) or [`NSNotFound`](https://developer.apple.com/documentation/Foundation/NSNotFound-9t5v2) (Objective-C).

## See Also

- [var resultCount: Int](uifindsession/resultcount.md)
  The total number of results the search matches.
- [var supportsReplacement: Bool](uifindsession/supportsreplacement.md)
  A Boolean value that indicates whether to allow replacing find panel results.
- [var allowsReplacementForCurrentlyHighlightedResult: Bool](uifindsession/allowsreplacementforcurrentlyhighlightedresult.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.
- [var searchResultDisplayStyle: UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.property.md)
  The information the find panel includes in the summary of found results.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/highlightedresultindex)*