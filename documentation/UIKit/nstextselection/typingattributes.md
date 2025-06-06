# typingAttributes

**Framework**: UIKit  
**Kind**: property

The template attributes the framework uses for characters that replace the contents of this selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var typingAttributes: [NSAttributedString.Key : Any] { get set }
```

## See Also

- [var affinity: NSTextSelection.Affinity](nstextselection/affinity-swift.property.md)
  Returns the selection affinity of the text selection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection/typingattributes)*