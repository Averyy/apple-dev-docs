# selectRowIndexes(_:byExtendingSelection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the row selection using `indexes` extending the selection if specified.

**Availability**:
- macOS

## Declaration

```swift
func selectRowIndexes(_ indexes: IndexSet, byExtendingSelection extend: Bool)
```

```objc
- (void) selectRowIndexes:(NSIndexSet *) indexes byExtendingSelection:(BOOL) extend;
```

## Discussion

Replaces the deprecated [`selectRow:byExtendingSelection:`](./selectrow_byextendingselection_.md) method.

## Parameters

- `indexes`: The indexes to select.
- `extend`: [`true`](../../Swift/true.md) if the selection should be extended, [`false`](../../Swift/false.md) if the current selection should be changed.

## See Also

### Selecting Columns and Rows
- [func selectColumnIndexes(IndexSet, byExtendingSelection: Bool)](./selectcolumnindexes%28_,byextendingselection%29.md)
  Sets the column selection using `indexes` possibly extending the selection.
- [var selectedColumn: Int](./selectedcolumn.md)
  The index of the last selected column (or the last column added to the selection).
- [var selectedColumnIndexes: IndexSet](./selectedcolumnindexes.md)
  An index set containing the indexes of the selected columns.
- [func deselectColumn(Int)](./deselectcolumn%28_%29.md)
  Deselects the column at the specified index if it’s selected.
- [var numberOfSelectedColumns: Int](./numberofselectedcolumns.md)
  The number of selected columns.
- [func isColumnSelected(Int) -> Bool](./iscolumnselected%28_%29.md)
  Returns a Boolean value that indicates whether the column at the specified index is selected.
- [var selectedRow: Int](./selectedrow.md)
  The index of the last selected row (or the last row added to the selection).
- [var selectedRowIndexes: IndexSet](./selectedrowindexes.md)
  An index set containing the indexes of the selected rows.
- [func deselectRow(Int)](./deselectrow%28_%29.md)
  Deselects the row at the specified index if it’s selected.
- [var numberOfSelectedRows: Int](./numberofselectedrows.md)
  The number of selected rows.
- [func isRowSelected(Int) -> Bool](./isrowselected%28_%29.md)
  Returns a Boolean value that indicates whether the row at the specified index is selected.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects all rows or all columns, according to whether rows or columns were most recently selected.
- [func deselectAll(Any?)](./deselectall%28_%29.md)
  Deselects all selected rows or columns if empty selection is allowed; otherwise does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/selectrowindexes(_:byextendingselection:))*