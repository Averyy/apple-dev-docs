# granularity

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The granularity of the selection.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var granularity: NSTextSelection.Granularity { get }
```

```objc
@property (readonly) NSTextSelectionGranularity granularity;
```

## Discussion

The default is [`NSTextSelection.Granularity.character`](./granularity-swift.enum/character.md). Selection extending operations modify the selection by `granularity`.

## See Also

### Characteristics of a selection
- [var affinity: NSTextSelection.Affinity](./affinity-swift.property.md)
  Returns the selection affinity of the text selection.
- [NSTextSelection.Affinity](./affinity-swift.enum.md)
  Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [var anchorPositionOffset: CGFloat](./anchorpositionoffset.md)
  Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [NSTextSelection.Granularity](./granularity-swift.enum.md)
  Values that describe the different granularities available to make a selection.
- [var isLogical: Bool](./islogical.md)
  A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [var isTransient: Bool](./istransient.md)
  A Boolean value that indicates transient text selection during drag handling.
- [var secondarySelectionLocation: (any NSTextLocation)?](./secondaryselectionlocation.md)
  Specifies the secondary character location when user taps or clicks at a directional boundary.
- [protocol NSTextLocation](../nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.
- [var textRanges: [NSTextRange]](./textranges.md)
  Represents an array of noncontiguous logical ranges in the selection.
- [var typingAttributes: [NSAttributedString.Key : Any]](./typingattributes.md)
  The template attributes the framework uses for characters that replace the contents of this selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/granularity-swift.property)*