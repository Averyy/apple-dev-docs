# allowsReordering()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns whether the user can reorder items.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func allowsReordering() -> Bool
```

```objc
- (BOOL) allowsReordering;
```

## Return Value

[`true`](../../Swift/true.md) if the user can reorder items; [`false`](../../Swift/false.md) otherwise.

## See Also

### Reordering and Groups Items
- [func selectionIndexes() -> IndexSet!](./selectionindexes%28%29.md)
  Returns the indexes of the selected cells.
- [func setSelectionIndexes(IndexSet!, byExtendingSelection: Bool)](./setselectionindexes%28_,byextendingselection%29.md)
  Selects cells at the specified indexes.
- [func setAllowsMultipleSelection(Bool)](./setallowsmultipleselection%28_%29.md)
  Controls whether the user can select more than one cell at a time.
- [func allowsMultipleSelection() -> Bool](./allowsmultipleselection%28%29.md)
  Returns whether multiple selections are allowed.
- [func setAllowsEmptySelection(Bool)](./setallowsemptyselection%28_%29.md)
  Controls whether an empty selection is allowed.
- [func allowsEmptySelection() -> Bool](./allowsemptyselection%28%29.md)
  Returns whether an empty selection is allowed.
- [func setAllowsReordering(Bool)](./setallowsreordering%28_%29.md)
  Controls whether the user can reorder items.
- [func setAnimates(Bool)](./setanimates%28_%29.md)
  Controls whether the receiver animates reordering and changes of the data source.
- [func animates() -> Bool](./animates%28%29.md)
  Returns whether the receiver animates reordering and changes of the data source.
- [func expandGroup(at: Int)](./expandgroup%28at%29.md)
  Expands a group at the specified index.
- [func collapseGroup(at: Int)](./collapsegroup%28at%29.md)
  Collapses a group at the specified index.
- [func isGroupExpanded(at: Int) -> Bool](./isgroupexpanded%28at%29.md)
  Returns whether the group at the provided index is expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/allowsreordering())*