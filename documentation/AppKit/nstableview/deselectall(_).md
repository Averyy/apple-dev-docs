# deselectAll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deselects all selected rows or columns if empty selection is allowed; otherwise does nothing.

**Availability**:
- macOS

## Declaration

```swift
func deselectAll(_ sender: Any?)
```

```objc
- (void) deselectAll:(id) sender;
```

## Discussion

Posts [`selectionDidChangeNotification`](./selectiondidchangenotification.md) to the default notification center if the selection does in fact change.

As a target-action method, [`deselectAll(_:)`](./deselectall%28_%29.md) checks with the delegate before changing the selection, using [`selectionShouldChange(in:)`](../nstableviewdelegate/selectionshouldchange%28in%29.md).

## Parameters

- `sender`: Typically the object that sent the message.

## See Also

### Related Documentation
- [func selectionShouldChange(in: NSTableView) -> Bool](../nstableviewdelegate/selectionshouldchange%28in%29.md)
  Asks the delegate if the user is allowed to change the selection.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [- selectColumn:byExtendingSelection:](./selectcolumn_byextendingselection_.md)
  Selects the column at the specified index, optionally extending any existing selection.
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
- [func selectRowIndexes(IndexSet, byExtendingSelection: Bool)](./selectrowindexes%28_,byextendingselection%29.md)
  Sets the row selection using `indexes` extending the selection if specified.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/deselectall(_:))*