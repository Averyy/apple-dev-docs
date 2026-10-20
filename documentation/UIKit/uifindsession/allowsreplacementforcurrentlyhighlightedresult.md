# allowsReplacementForCurrentlyHighlightedResult

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var allowsReplacementForCurrentlyHighlightedResult: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL allowsReplacementForCurrentlyHighlightedResult;
```

#### Discussion

This property determines whether the find panel supports replacement for the currently highlighted item. If [`true`](../../Swift/true.md), the system enables the Replace button in the find panel and the hardware keyboard shortcuts for replacement.

The default value is [`true`](../../Swift/true.md) if [`supportsReplacement`](./supportsreplacement.md) is [`true`](../../Swift/true.md).

## See Also

### Getting session information
- [var resultCount: Int](./resultcount.md)
  The total number of results the search matches.
- [var highlightedResultIndex: Int](./highlightedresultindex.md)
  The index of the result the find panel highlights.
- [var supportsReplacement: Bool](./supportsreplacement.md)
  A Boolean value that indicates whether to allow replacing find panel results.
- [var searchResultDisplayStyle: UIFindSession.SearchResultDisplayStyle](./searchresultdisplaystyle-swift.property.md)
  The information the find panel includes in the summary of found results.
- [UIFindSession.SearchResultDisplayStyle](./searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.
- [var allowsReplacement: Bool](./allowsreplacement.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/allowsreplacementforcurrentlyhighlightedresult)*