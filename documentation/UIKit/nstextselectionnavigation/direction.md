# NSTextSelectionNavigation.Direction

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSTextSelectionNavigationDirection : NSInteger;
```

## Topics

### Navigation directions
- [NSTextSelectionNavigation.Direction.forward](./direction/forward.md)
  The value that represents a logical forward selection based on the flow of text stored in the document.
- [NSTextSelectionNavigation.Direction.backward](./direction/backward.md)
  The value that represents a backward selection based on the flow of text stored in the document.
- [NSTextSelectionNavigation.Direction.left](./direction/left.md)
  The value that represents a selection in the left direction along the current line.
- [NSTextSelectionNavigation.Direction.right](./direction/right.md)
  The value that represents a selection in the right direction along the current line.
- [NSTextSelectionNavigation.Direction.up](./direction/up.md)
  The value that represents a selection in the up direction, above the current line.
- [NSTextSelectionNavigation.Direction.down](./direction/down.md)
  The value that represents a selection in the down direction, below the current line.
### Initializers
- [init?(rawValue: Int)](./direction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Selection characteristics
- [var allowsNonContiguousRanges: Bool](./allowsnoncontiguousranges.md)
  Determines if the instance could produce selections with multiple noncontiguous selections.
- [var rotatesCoordinateSystemForLayoutOrientation: Bool](./rotatescoordinatesystemforlayoutorientation.md)
  Determines if the framework rotates the coordinate system to match the layout orientation.
- [NSTextSelectionNavigation.Modifier](./modifier.md)
  Values that describe how the framework handles different kinds of selection modifiers.
- [NSTextSelectionNavigation.Destination](./destination.md)
  Values that affect how the framework handles navigation across different textual boundaries during a selection.
- [func textSelection(for: NSTextSelection.Granularity, enclosing: CGPoint, inContainerAt: any NSTextLocation) -> NSTextSelection?](./textselection%28for,enclosing,incontainerat%29.md)
  Returns a text selection that expands to the nearest boundaries for selection granularity and an enclosing point you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextselectionnavigation/direction)*