# isColumnSelected(_:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the column at the specified index is selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func isColumnSelected(_ column: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the column at `columnIndex` is selected, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `column`: The index into the   array that represents the column to test.

## See Also

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
- [func selectRowIndexes(IndexSet, byExtendingSelection: Bool)](nstableview/selectrowindexes(_:byextendingselection:).md)
  Sets the row selection using `indexes` extending the selection if specified.
- [var selectedRow: Int](nstableview/selectedrow.md)
  The index of the last selected row (or the last row added to the selection).
- [var selectedRowIndexes: IndexSet](nstableview/selectedrowindexes.md)
  An index set containing the indexes of the selected rows.
- [func deselectRow(Int)](nstableview/deselectrow(_:).md)
  Deselects the row at the specified index if it’s selected.
- [var numberOfSelectedRows: Int](nstableview/numberofselectedrows.md)
  The number of selected rows.
- [func isRowSelected(Int) -> Bool](nstableview/isrowselected(_:).md)
  Returns a Boolean value that indicates whether the row at the specified index is selected.
- [func selectAll(Any?)](nstableview/selectall(_:).md)
  Selects all rows or all columns, according to whether rows or columns were most recently selected.
- [func deselectAll(Any?)](nstableview/deselectall(_:).md)
  Deselects all selected rows or columns if empty selection is allowed; otherwise does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/iscolumnselected(_:))*