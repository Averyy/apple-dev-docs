# setSelectionIndexes(_:byExtendingSelection:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Selects cells at the specified indexes.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setSelectionIndexes(_ indexes: IndexSet!, byExtendingSelection extendSelection: Bool)
```

```objc
- (void) setSelectionIndexes:(NSIndexSet *) indexes byExtendingSelection:(BOOL) extendSelection;
```

## Parameters

- `indexes`: The indexes of the cells you want to select.
- `extendSelection`: A `BOOL` value that specifies whether to extend the current selection. Pass [`true`](../../Swift/true.md) to extends the selection; [`false`](../../Swift/false.md) replaces the current selection.

## See Also

### Reordering and Groups Items
- [func selectionIndexes() -> IndexSet!](./selectionindexes%28%29.md)
  Returns the indexes of the selected cells.
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
- [func allowsReordering() -> Bool](./allowsreordering%28%29.md)
  Returns whether the user can reorder items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/ikimagebrowserview/setselectionindexes(_:byextendingselection:))*