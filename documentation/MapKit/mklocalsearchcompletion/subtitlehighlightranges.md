# subtitleHighlightRanges

**Framework**: MapKit  
**Kind**: property

The ranges of characters to highlight in the subtitle string.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var subtitleHighlightRanges: [NSValue] { get }
```

#### Discussion

This property contains an array of [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) objects, each of which contains an [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct) type defining a range of characters in the [`subtitle`](mklocalsearchcompletion/subtitle.md) string. Use this property to identify the ranges of characters in the subtitle string that you want to highlight. Highlighting the matching text of a search completion is optional, but it’s a best practice for providing helpful information to the user.

## See Also

- [var title: String](mklocalsearchcompletion/title.md)
  The title string associated with the point of interest.
- [var subtitle: String](mklocalsearchcompletion/subtitle.md)
  The subtitle (if any) associated with the point of interest.
- [var titleHighlightRanges: [NSValue]](mklocalsearchcompletion/titlehighlightranges.md)
  The ranges of characters to highlight in the title string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion/subtitlehighlightranges)*