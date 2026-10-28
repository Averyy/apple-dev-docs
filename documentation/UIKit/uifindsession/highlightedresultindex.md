# highlightedResultIndex

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The index of the result the find panel highlights.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var highlightedResultIndex: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger highlightedResultIndex;
```

## Discussion

To indicate no highlighted result, return `nil` (Swift) or [`NSNotFound`](../../Foundation/nsnotfound-9t5v2.md) (Objective-C).

## See Also

### Getting session information
- [var resultCount: Int](./resultcount.md)
  The total number of results the search matches.
- [var supportsReplacement: Bool](./supportsreplacement.md)
  A Boolean value that indicates whether to allow replacing find panel results.
- [var allowsReplacementForCurrentlyHighlightedResult: Bool](./allowsreplacementforcurrentlyhighlightedresult.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.
- [var searchResultDisplayStyle: UIFindSession.SearchResultDisplayStyle](./searchresultdisplaystyle-swift.property.md)
  The information the find panel includes in the summary of found results.
- [UIFindSession.SearchResultDisplayStyle](./searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.
- [var allowsReplacement: Bool](./allowsreplacement.md)
  A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindsession/highlightedresultindex)*