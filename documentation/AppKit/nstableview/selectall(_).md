# selectAll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects all rows or all columns, according to whether rows or columns were most recently selected.

**Availability**:
- macOS

## Declaration

```swift
func selectAll(_ sender: Any?)
```

```objc
- (void) selectAll:(id) sender;
```

#### Discussion

If the table allows multiple selection, this action method selects all rows or all columns, according to whether rows or columns were most recently selected. If nothing has been recently selected, this method selects all rows. If this table doesn’t allow multiple selection, this method does nothing.

If the selection does change, this method posts [`selectionDidChangeNotification`](./selectiondidchangenotification.md) to the default notification center.

As a target-action method, [`selectAll(_:)`](./selectall%28_%29.md) checks with the delegate before changing the selection.

## Parameters

- `sender`: Typically the object that sent the message.

## See Also

### Related Documentation
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.
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
- [func deselectAll(Any?)](./deselectall%28_%29.md)
  Deselects all selected rows or columns if empty selection is allowed; otherwise does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/selectall(_:))*