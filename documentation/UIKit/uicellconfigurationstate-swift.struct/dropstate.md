# UICellConfigurationState.DropState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the cell’s drop state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
enum DropState
```

## Topics

### Drop states
- [UICellConfigurationState.DropState.none](./dropstate/none.md)
  The system hasn’t associated the cell with a drag session.
- [UICellConfigurationState.DropState.notTargeted](./dropstate/nottargeted.md)
  A drag session is active and can perform a drop in the cell’s container, but the cell itself isn’t the drop target.
- [UICellConfigurationState.DropState.targeted](./dropstate/targeted.md)
  The cell is the drop target for a drag session.

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
- [UICellConfigurationState.DragState](./dragstate.md)
  Constants that describe the cell’s drag state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellconfigurationstate-swift.struct/dropstate)*