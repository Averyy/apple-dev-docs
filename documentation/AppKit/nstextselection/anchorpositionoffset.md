# anchorPositionOffset

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var anchorPositionOffset: CGFloat { get set }
```

```objc
@property CGFloat anchorPositionOffset;
```

## Discussion

That starts from the left for a horizontal line fragment, and from the top for a vertical. Navigating between lines uses this point when the current line fragment associated with the selection is shorter than the next line visited. Defaults to `0.0`.

## See Also

### Characteristics of a selection
- [var affinity: NSTextSelection.Affinity](./affinity-swift.property.md)
  Returns the selection affinity of the text selection.
- [NSTextSelection.Affinity](./affinity-swift.enum.md)
  Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [var granularity: NSTextSelection.Granularity](./granularity-swift.property.md)
  The granularity of the selection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/anchorpositionoffset)*