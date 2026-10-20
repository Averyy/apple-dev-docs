# NSTextSelection.Granularity

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Values that describe the different granularities available to make a selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Granularity
```

```c
enum NSTextSelectionGranularity : NSInteger;
```

## Topics

### Degrees of granularity
- [NSTextSelection.Granularity.character](./granularity-swift.enum/character.md)
  A value that represents selection by character.
- [NSTextSelection.Granularity.word](./granularity-swift.enum/word.md)
  A value that represents selection by word.
- [NSTextSelection.Granularity.paragraph](./granularity-swift.enum/paragraph.md)
  A value that represents selection by paragraph.
- [NSTextSelection.Granularity.line](./granularity-swift.enum/line.md)
  A value that represents selection by line.
- [NSTextSelection.Granularity.sentence](./granularity-swift.enum/sentence.md)
  A value that represents selection by sentence.
### Initializers
- [init?(rawValue: Int)](./granularity-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Characteristics of a selection
- [var affinity: NSTextSelection.Affinity](./affinity-swift.property.md)
  Returns the selection affinity of the text selection.
- [NSTextSelection.Affinity](./affinity-swift.enum.md)
  Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [var anchorPositionOffset: CGFloat](./anchorpositionoffset.md)
  Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
- [var granularity: NSTextSelection.Granularity](./granularity-swift.property.md)
  The granularity of the selection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection/granularity-swift.enum)*