# isGroupExpanded(at:)

**Framework**: Quartz  
**Kind**: method

Returns whether the group at the provided index is expanded.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func isGroupExpanded(at index: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the group is expanded; [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

This method is declared in OS X v10.5, but an implementation was not provided until OS X v10.6. Avoid using this method in OS X v10.5.

## Parameters

- `index`: The index you want to check.

## See Also

- [func selectionIndexes() -> IndexSet!](ikimagebrowserview/selectionindexes.md)
  Returns the indexes of the selected cells.
- [func setSelectionIndexes(IndexSet!, byExtendingSelection: Bool)](ikimagebrowserview/setselectionindexes(_:byextendingselection:).md)
  Selects cells at the specified indexes.
- [func setAllowsMultipleSelection(Bool)](ikimagebrowserview/setallowsmultipleselection(_:).md)
  Controls whether the user can select more than one cell at a time.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/isgroupexpanded(at:))*