# deselectColumn(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deselects the column at the specified index if it’s selected.

**Availability**:
- macOS

## Declaration

```swift
func deselectColumn(_ column: Int)
```

```objc
- (void) deselectColumn:(NSInteger) column;
```

## Discussion

Deselects the column at `columnIndex` if it’s selected, regardless of whether empty selection is allowed.

If the selection does in fact change, this method posts [`selectionDidChangeNotification`](./selectiondidchangenotification.md) to the default notification center.

If the indicated column was the last column selected by the user, the column nearest it effectively becomes the last selected column. In case of a tie, priority is given to the column on the left.

This method doesn’t check with the delegate before changing the selection.

## Parameters

- `column`: The index in the [`tableColumns`](./tablecolumns.md) array of the column to deselect.

## See Also

### Related Documentation
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [- selectRow:byExtendingSelection:](./selectrow_byextendingselection_.md)
  Selects a row at the specified index, optionally extending any existing selection.
### Selecting Columns and Rows
- [func selectColumnIndexes(IndexSet, byExtendingSelection: Bool)](./selectcolumnindexes%28_,byextendingselection%29.md)
  Sets the column selection using `indexes` possibly extending the selection.
- [var selectedColumn: Int](./selectedcolumn.md)
  The index of the last selected column (or the last column added to the selection).
- [var selectedColumnIndexes: IndexSet](./selectedcolumnindexes.md)
  An index set containing the indexes of the selected columns.
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
- [func deselectAll(Any?)](./deselectall%28_%29.md)
  Deselects all selected rows or columns if empty selection is allowed; otherwise does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/deselectcolumn(_:))*