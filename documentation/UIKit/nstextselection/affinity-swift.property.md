# affinity

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the selection affinity of the text selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var affinity: NSTextSelection.Affinity { get }
```

```objc
@property (readonly) NSTextSelectionAffinity affinity;
```

#### Discussion

The affinity is [`NSTextSelection.Affinity.downstream`](./affinity-swift.enum/downstream.md) by default. For a zero-length selection, it describes the visual location of the text cursor between the head of line containing the selection location (downstream) or tail of the previous line (upstream). For a selection with contents, it describes the logical direction of non-anchored edge of the selection.

## See Also

### Characteristics of a selection
- [NSTextSelection.Affinity](./affinity-swift.enum.md)
  Values that describe the visual location of the text cursor, or the direction of the non-anchored edge of the selection.
- [var anchorPositionOffset: CGFloat](./anchorpositionoffset.md)
  Represents the anchor position offset from the beginning of a line fragment in the visual order for the initial tap or click location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselection/affinity-swift.property)*