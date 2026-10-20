# DragDropPreviewsFormation

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

On macOS, describes the way the dragged previews are visually composed. Both drag sources and drop destination can specify their desired preview formation.

**Availability**:
- macOS 26.0+

## Declaration

```swift
struct DragDropPreviewsFormation
```

## Topics

### Type Properties
- [static let `default`: DragDropPreviewsFormation](./dragdroppreviewsformation/default.md)
  System-determined composition.
- [static let list: DragDropPreviewsFormation](./dragdroppreviewsformation/list.md)
  Drag images are laid out vertically, non-overlapping, and the left edges are aligned.
- [static let none: DragDropPreviewsFormation](./dragdroppreviewsformation/none.md)
  Drag images maintain their set positions relative to each other.
- [static let pile: DragDropPreviewsFormation](./dragdroppreviewsformation/pile.md)
  Drag images are placed on top of each other with random rotations.
- [static let stack: DragDropPreviewsFormation](./dragdroppreviewsformation/stack.md)
  Drag images are laid out overlapping diagonally.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Describing preview formations
- [func dragPreviewsFormation(DragDropPreviewsFormation) -> some View](./view/dragpreviewsformation%28_%29.md)
  Describes the way dragged previews are visually composed.
- [func dropPreviewsFormation(DragDropPreviewsFormation) -> some View](./view/droppreviewsformation%28_%29.md)
  Describes the way previews for a drop are composed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragdroppreviewsformation)*