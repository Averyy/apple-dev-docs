# NSTextSelectionNavigation.Direction

**Framework**: UIKit  
**Kind**: enum

Values that describe the direction of a selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Direction
```

## Topics

### Navigation directions
- [NSTextSelectionNavigation.Direction.forward](nstextselectionnavigation/direction/forward.md)
  The value that represents a logical forward selection based on the flow of text stored in the document.
- [NSTextSelectionNavigation.Direction.backward](nstextselectionnavigation/direction/backward.md)
  The value that represents a backward selection based on the flow of text stored in the document.
- [NSTextSelectionNavigation.Direction.left](nstextselectionnavigation/direction/left.md)
  The value that represents a selection in the left direction along the current line.
- [NSTextSelectionNavigation.Direction.right](nstextselectionnavigation/direction/right.md)
  The value that represents a selection in the right direction along the current line.
- [NSTextSelectionNavigation.Direction.up](nstextselectionnavigation/direction/up.md)
  The value that represents a selection in the up direction, above the current line.
- [NSTextSelectionNavigation.Direction.down](nstextselectionnavigation/direction/down.md)
  The value that represents a selection in the down direction, below the current line.
### Initializers
- [init?(rawValue: Int)](nstextselectionnavigation/direction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var allowsNonContiguousRanges: Bool](nstextselectionnavigation/allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](nstextselectionnavigation/rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Modifier](nstextselectionnavigation/modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Destination](nstextselectionnavigation/destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](nstextselectionnavigation/textselection(for:enclosing:incontainerat:).md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/direction)*