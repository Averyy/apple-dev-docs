# UICellConfigurationState.DropState

**Framework**: UIKit  
**Kind**: enum

Constants that describe the cell’s drop state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
enum DropState
```

## Topics

### Drop states
- [UICellConfigurationState.DropState.none](uicellconfigurationstate-swift.struct/dropstate/none.md)
  The system hasn’t associated the cell with a drag session.
- [UICellConfigurationState.DropState.notTargeted](uicellconfigurationstate-swift.struct/dropstate/nottargeted.md)
  A drag session is active and can perform a drop in the cell’s container, but the cell itself isn’t the drop target.
- [UICellConfigurationState.DropState.targeted](uicellconfigurationstate-swift.struct/dropstate/targeted.md)
  The cell is the drop target for a drag session.

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
- [UICellConfigurationState.DragState](uicellconfigurationstate-swift.struct/dragstate.md)
  Constants that describe the cell’s drag state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellconfigurationstate-swift.struct/dropstate)*