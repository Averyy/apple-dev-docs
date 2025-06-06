# affinity

**Framework**: AppKit  
**Kind**: property

Returns the selection affinity of the text selection.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var affinity: NSTextSelection.Affinity { get }
```

#### Discussion

The affinity is [`NSTextSelection.Affinity.downstream`](nstextselection/affinity-swift.enum/downstream.md) by default. For a zero-length selection, it describes the visual location of the text cursor between the head of line containing the selection location (downstream) or tail of the previous line (upstream). For a selection with contents, it describes the logical direction of non-anchored edge of the selection.

## See Also

- [NSTextSelection.Affinity](nstextselection/affinity-swift.enum.md)
  Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [var anchorPositionOffset: CGFloat](nstextselection/anchorpositionoffset.md)
  Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [var granularity: NSTextSelection.Granularity](nstextselection/granularity-swift.property.md)
  The granularity of the selection.
- [NSTextSelection.Granularity](nstextselection/granularity-swift.enum.md)
  Values that describe the different granularities available to make a selection.
- [var isLogical: Bool](nstextselection/islogical.md)
  A Boolean value that indicates whether the framework interprets the selection as logical or visual.
- [var isTransient: Bool](nstextselection/istransient.md)
  A Boolean value that indicates transient text selection during drag handling.
- [var secondarySelectionLocation: (any NSTextLocation)?](nstextselection/secondaryselectionlocation.md)
  Specifies the secondary character location when user taps or clicks at a directional boundary.
- [protocol NSTextLocation](nstextlocation.md)
  An interface you implement that represents an abstract location inside your document’s content.
- [var textRanges: [NSTextRange]](nstextselection/textranges.md)
  Represents an array of noncontiguous logical ranges in the selection.
- [var typingAttributes: [NSAttributedString.Key : Any]](nstextselection/typingattributes.md)
  The template attributes the framework uses for characters that replace the contents of this selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/affinity-swift.property)*