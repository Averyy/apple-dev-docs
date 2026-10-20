# UICellConfigurationState.DragState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the cell’s drag state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
enum DragState
```

## Topics

### Drag states
- [UICellConfigurationState.DragState.none](./dragstate/none.md)
  The system hasn’t associated the cell with a drag session.
- [UICellConfigurationState.DragState.lifting](./dragstate/lifting.md)
  A user interaction is lifting the cell, but it isn’t yet part of an active drag session.
- [UICellConfigurationState.DragState.dragging](./dragstate/dragging.md)
  The cell is part of an active drag session.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Managing cell configuration states
- [var isEditing: Bool](./isediting.md)
  A Boolean value that indicates whether the cell is in editing mode.
- [var isSwiped: Bool](./isswiped.md)
  A Boolean value that indicates whether the cell is in a swiped state.
- [var isExpanded: Bool](./isexpanded.md)
  A Boolean value that indicates whether the cell is in an expanded state, such as in an outline.
- [var isReordering: Bool](./isreordering.md)
  A Boolean value that indicates whether the cell is reordering.
- [var cellDragState: UICellConfigurationState.DragState](./celldragstate.md)
  The cell’s drag state.
- [var cellDropState: UICellConfigurationState.DropState](./celldropstate.md)
  The cell’s drop state.
- [UICellConfigurationState.DropState](./dropstate.md)
  Constants that describe the cell’s drop state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellconfigurationstate-swift.struct/dragstate)*