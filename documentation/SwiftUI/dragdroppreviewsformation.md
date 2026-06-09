# DragDropPreviewsFormation

**Framework**: SwiftUI  
**Kind**: struct

On macOS, describes the way the dragged previews are visually composed. Both drag sources and drop destination can specify their desired preview formation.

**Availability**:
- macOS 26.0+

## Declaration

```swift
struct DragDropPreviewsFormation
```

## Topics

### Type Properties
- [static let `default`: DragDropPreviewsFormation](dragdroppreviewsformation/default.md)
  System-determined composition.
- [static let list: DragDropPreviewsFormation](dragdroppreviewsformation/list.md)
  Drag images are laid out vertically, non-overlapping, and the left edges are aligned.
- [static let none: DragDropPreviewsFormation](dragdroppreviewsformation/none.md)
  Drag images maintain their set positions relative to each other.
- [static let pile: DragDropPreviewsFormation](dragdroppreviewsformation/pile.md)
  Drag images are placed on top of each other with random rotations.
- [static let stack: DragDropPreviewsFormation](dragdroppreviewsformation/stack.md)
  Drag images are laid out overlapping diagonally.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func dragPreviewsFormation(DragDropPreviewsFormation) -> some View](view/dragpreviewsformation(_:).md)
  Describes the way dragged previews are visually composed.
- [func dropPreviewsFormation(DragDropPreviewsFormation) -> some View](view/droppreviewsformation(_:).md)
  Describes the way previews for a drop are composed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragdroppreviewsformation)*