# supportsReplacement

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to allow replacing find panel results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var supportsReplacement: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL supportsReplacement;
```

#### Discussion

This property determines whether the find panel shows the replacement UI.

The default value is [`false`](../../Swift/false.md).

## See Also

### Getting session information
- [var resultCount: Int](./resultcount.md)
  The total number of results the search matches.
- [var highlightedResultIndex: Int](./highlightedresultindex.md)
  The index of the result the find panel highlights.
- [var allowsReplacementForCurrentlyHighlightedResult: Bool](./allowsreplacementforcurrentlyhighlightedresult.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.
- [var searchResultDisplayStyle: UIFindSession.SearchResultDisplayStyle](./searchresultdisplaystyle-swift.property.md)
  The information the find panel includes in the summary of found results.
- [UIFindSession.SearchResultDisplayStyle](./searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.
- [var allowsReplacement: Bool](./allowsreplacement.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/supportsreplacement)*