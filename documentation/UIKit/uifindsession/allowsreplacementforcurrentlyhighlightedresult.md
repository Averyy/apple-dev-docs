# allowsReplacementForCurrentlyHighlightedResult

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsReplacementForCurrentlyHighlightedResult: Bool { get }
```

#### Discussion

This property determines whether the find panel supports replacement for the currently highlighted item. If [`true`](https://developer.apple.com/documentation/swift/true), the system enables the Replace button in the find panel and the hardware keyboard shortcuts for replacement.

The default value is [`true`](https://developer.apple.com/documentation/swift/true) if [`supportsReplacement`](uifindsession/supportsreplacement.md) is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var resultCount: Int](uifindsession/resultcount.md)
  The total number of results the search matches.
- [var highlightedResultIndex: Int](uifindsession/highlightedresultindex.md)
  The index of the result the find panel highlights.
- [var supportsReplacement: Bool](uifindsession/supportsreplacement.md)
  A Boolean value that indicates whether to allow replacing find panel results.
- [var searchResultDisplayStyle: UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.property.md)
  The information the find panel includes in the summary of found results.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/allowsreplacementforcurrentlyhighlightedresult)*