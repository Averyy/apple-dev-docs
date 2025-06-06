# NSTextSelection.Granularity

**Framework**: AppKit  
**Kind**: enum

Values that describe the different granularities available to make a selection.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum Granularity
```

## Topics

### Degrees of granularity
- [NSTextSelection.Granularity.character](nstextselection/granularity-swift.enum/character.md)
  A value that represents selection by character.
- [NSTextSelection.Granularity.word](nstextselection/granularity-swift.enum/word.md)
  A value that represents selection by word.
- [NSTextSelection.Granularity.paragraph](nstextselection/granularity-swift.enum/paragraph.md)
  A value that represents selection by paragraph.
- [NSTextSelection.Granularity.line](nstextselection/granularity-swift.enum/line.md)
  A value that represents selection by line.
- [NSTextSelection.Granularity.sentence](nstextselection/granularity-swift.enum/sentence.md)
  A value that represents selection by sentence.
### Initializers
- [init?(rawValue: Int)](nstextselection/granularity-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var affinity: NSTextSelection.Affinity](nstextselection/affinity-swift.property.md)
  Returns the selection affinity of the text selection.
- [NSTextSelection.Affinity](nstextselection/affinity-swift.enum.md)
  Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [var anchorPositionOffset: CGFloat](nstextselection/anchorpositionoffset.md)
  Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [var granularity: NSTextSelection.Granularity](nstextselection/granularity-swift.property.md)
  The granularity of the selection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselection/granularity-swift.enum)*