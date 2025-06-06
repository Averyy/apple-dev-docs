# setAllowsMultipleSelection(_:)

**Framework**: Quartz  
**Kind**: method

Controls whether the user can select more than one cell at a time.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setAllowsMultipleSelection(_ flag: Bool)
```

## Parameters

- `flag`: A   value that specifies whether to allow multiple selections.

## See Also

- [func selectionIndexes() -> IndexSet!](ikimagebrowserview/selectionindexes.md)
  Returns the indexes of the selected cells.
- [func setSelectionIndexes(IndexSet!, byExtendingSelection: Bool)](ikimagebrowserview/setselectionindexes(_:byextendingselection:).md)
  Selects cells at the specified indexes.
- [func allowsMultipleSelection() -> Bool](ikimagebrowserview/allowsmultipleselection.md)
  Returns whether multiple selections are allowed.
- [func setAllowsEmptySelection(Bool)](ikimagebrowserview/setallowsemptyselection(_:).md)
  Controls whether an empty selection is allowed.
- [func allowsEmptySelection() -> Bool](ikimagebrowserview/allowsemptyselection.md)
  Returns whether an empty selection is allowed.
- [func setAllowsReordering(Bool)](ikimagebrowserview/setallowsreordering(_:).md)
  Controls whether the user can reorder items.
- [func allowsReordering() -> Bool](ikimagebrowserview/allowsreordering.md)
  Returns whether the user can reorder items.
- [func setAnimates(Bool)](ikimagebrowserview/setanimates(_:).md)
  Controls whether the receiver animates reordering and changes of the data source.
- [func animates() -> Bool](ikimagebrowserview/animates.md)
  Returns whether the receiver animates reordering and changes of the data source.
- [func expandGroup(at: Int)](ikimagebrowserview/expandgroup(at:).md)
  Expands a group at the specified index.
- [func collapseGroup(at: Int)](ikimagebrowserview/collapsegroup(at:).md)
  Collapses a group at the specified index.
- [func isGroupExpanded(at: Int) -> Bool](ikimagebrowserview/isgroupexpanded(at:).md)
  Returns whether the group at the provided index is expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setallowsmultipleselection(_:))*