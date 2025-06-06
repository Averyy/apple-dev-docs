# deselectRow(_:)

**Framework**: AppKit  
**Kind**: method

Deselects the row at the specified index if it’s selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func deselectRow(_ row: Int)
```

#### Discussion

Deselects the row at `rowIndex` if it’s selected, regardless of whether empty selection is allowed.

If the selection does in fact change, posts [`selectionDidChangeNotification`](nstableview/selectiondidchangenotification.md) to the default notification center.

If the indicated row was the last row selected by the user, the row nearest it effectively becomes the last selected row. In case of a tie, priority is given to the row above.

This method doesn’t check with the delegate before changing the selection.

## Parameters

- `row`: The index of the row to deselect.

## See Also

- [var allowsEmptySelection: Bool](nstableview/allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [func selectColumnIndexes(IndexSet, byExtendingSelection: Bool)](nstableview/selectcolumnindexes(_:byextendingselection:).md)
  Sets the column selection using `indexes` possibly extending the selection.
- [var selectedColumn: Int](nstableview/selectedcolumn.md)
  The index of the last selected column (or the last column added to the selection).
- [var selectedColumnIndexes: IndexSet](nstableview/selectedcolumnindexes.md)
  An index set containing the indexes of the selected columns.
- [func deselectColumn(Int)](nstableview/deselectcolumn(_:).md)
  Deselects the column at the specified index if it’s selected.
- [var numberOfSelectedColumns: Int](nstableview/numberofselectedcolumns.md)
  The number of selected columns.
- [func isColumnSelected(Int) -> Bool](nstableview/iscolumnselected(_:).md)
  Returns a Boolean value that indicates whether the column at the specified index is selected.
- [func selectRowIndexes(IndexSet, byExtendingSelection: Bool)](nstableview/selectrowindexes(_:byextendingselection:).md)
  Sets the row selection using `indexes` extending the selection if specified.
- [var selectedRow: Int](nstableview/selectedrow.md)
  The index of the last selected row (or the last row added to the selection).
- [var selectedRowIndexes: IndexSet](nstableview/selectedrowindexes.md)
  An index set containing the indexes of the selected rows.
- [var numberOfSelectedRows: Int](nstableview/numberofselectedrows.md)
  The number of selected rows.
- [func isRowSelected(Int) -> Bool](nstableview/isrowselected(_:).md)
  Returns a Boolean value that indicates whether the row at the specified index is selected.
- [func selectAll(Any?)](nstableview/selectall(_:).md)
  Selects all rows or all columns, according to whether rows or columns were most recently selected.
- [func deselectAll(Any?)](nstableview/deselectall(_:).md)
  Deselects all selected rows or columns if empty selection is allowed; otherwise does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/deselectrow(_:))*