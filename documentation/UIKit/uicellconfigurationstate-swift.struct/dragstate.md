# UICellConfigurationState.DragState

**Framework**: UIKit  
**Kind**: enum

Constants that describe the cell’s drag state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
enum DragState
```

## Topics

### Drag states
- [UICellConfigurationState.DragState.none](uicellconfigurationstate-swift.struct/dragstate/none.md)
  The system hasn’t associated the cell with a drag session.
- [UICellConfigurationState.DragState.lifting](uicellconfigurationstate-swift.struct/dragstate/lifting.md)
  A user interaction is lifting the cell, but it isn’t yet part of an active drag session.
- [UICellConfigurationState.DragState.dragging](uicellconfigurationstate-swift.struct/dragstate/dragging.md)
  The cell is part of an active drag session.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var isEditing: Bool](uicellconfigurationstate-swift.struct/isediting.md)
  A Boolean value that indicates whether the cell is in editing mode.
- [var isSwiped: Bool](uicellconfigurationstate-swift.struct/isswiped.md)
  A Boolean value that indicates whether the cell is in a swiped state.
- [var isExpanded: Bool](uicellconfigurationstate-swift.struct/isexpanded.md)
  A Boolean value that indicates whether the cell is in an expanded state, such as in an outline.
- [var isReordering: Bool](uicellconfigurationstate-swift.struct/isreordering.md)
  A Boolean value that indicates whether the cell is reordering.
- [var cellDragState: UICellConfigurationState.DragState](uicellconfigurationstate-swift.struct/celldragstate.md)
  The cell’s drag state.
- [var cellDropState: UICellConfigurationState.DropState](uicellconfigurationstate-swift.struct/celldropstate.md)
  The cell’s drop state.
- [UICellConfigurationState.DropState](uicellconfigurationstate-swift.struct/dropstate.md)
  Constants that describe the cell’s drop state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellconfigurationstate-swift.struct/dragstate)*