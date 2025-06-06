# UICellConfigurationState

**Framework**: UIKit  
**Kind**: struct

A structure that encapsulates a cell’s state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct UICellConfigurationState
```

#### Overview

A cell configuration state encompasses a trait collection along with all of the common states that affect a cell’s appearance — view states like selected, focused, or disabled, and cell states like editing or swiped. A cell configuration state encapsulates the inputs that configure a cell for any possible state or combination of states. You use a cell configuration state with background and content configurations to obtain the default appearance for a specific state.

Typically, you don’t create a configuration state yourself. To obtain a configuration state, override the [`updateConfiguration(using:)`](uicollectionviewcell/updateconfiguration(using:).md) method in your cell subclass and use the state parameter. Outside of this method, you can get a cell’s configuration state by using its [`configurationState`](uicollectionviewcell/configurationstate-4u37h.md) property.

You can create your own custom states to add to a cell configuration state by defining a custom state key using [`UIConfigurationStateCustomKey`](uiconfigurationstatecustomkey.md).

## Topics

### Managing view configuration states
- [var isSelected: Bool](uicellconfigurationstate-swift.struct/isselected.md)
  A Boolean value that indicates whether the cell is in a selected state.
- [var isHighlighted: Bool](uicellconfigurationstate-swift.struct/ishighlighted.md)
  A Boolean value that indicates whether the cell is in a highlighted state.
- [var isFocused: Bool](uicellconfigurationstate-swift.struct/isfocused.md)
  A Boolean value that indicates whether the cell is in a focused state.
- [var isDisabled: Bool](uicellconfigurationstate-swift.struct/isdisabled.md)
  A Boolean value that indicates whether the cell is in a disabled state.
- [var isPinned: Bool](uicellconfigurationstate-swift.struct/ispinned.md)
  A Boolean value that indicates whether the view is in a pinned state.
### Managing cell configuration states
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
- [UICellConfigurationState.DropState](uicellconfigurationstate-swift.struct/dropstate.md)
  Constants that describe the cell’s drop state.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [UIConfigurationState](uiconfigurationstate-8d7pd.md)

## See Also

- [struct UIViewConfigurationState](uiviewconfigurationstate-swift.struct.md)
  A structure that encapsulates a view’s state.
- [protocol UIConfigurationState](uiconfigurationstate-8d7pd.md)
  The requirements for an object that encapsulates a view’s state.
- [struct UIConfigurationStateCustomKey](uiconfigurationstatecustomkey.md)
  A key that defines a custom state for a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellconfigurationstate-swift.struct)*