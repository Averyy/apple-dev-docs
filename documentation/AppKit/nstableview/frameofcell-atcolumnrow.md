# frameOfCell(atColumn:row:)

**Framework**: AppKit  
**Kind**: method

Returns a rectangle locating the cell that lies at the intersection of the specified column and row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func frameOfCell(atColumn column: Int, row: Int) -> NSRect
```

#### Return Value

A rectangle locating the cell that lies at the intersection of `columnIndex` and `rowIndex`. This method returns `NSZeroRect` if `columnIndex` or `rowIndex` is greater than the number of columns or rows in the table view.

#### Discussion

You can use this method to update a single cell more efficiently than sending the table view a [`reloadData()`](nstableview/reloaddata().md) message using [`reloadData(forRowIndexes:columnIndexes:)`](nstableview/reloaddata(forrowindexes:columnindexes:).md)

The result of this method is used in a [`draw(withFrame:in:)`](nscell/draw(withframe:in:).md) message to the table column’s data cell. You can subclass and override this method to customize the frame of a particular cell. However, never return a frame larger than the default implementation returns.

The default frame is computed to have a height equal to the [`rect(ofRow:)`](nstableview/rect(ofrow:).md) for `rowIndex`, minus the half [`intercellSpacing`](nstableview/intercellspacing.md) height on the top and half on the bottom.  The width of frame is equal to the with of the table column minus half the [`intercellSpacing`](nstableview/intercellspacing.md) width on the left, and half on the right.

## Parameters

- `column`: The index in the   array of the column containing the cell whose rectangle you want.
- `row`: The index of the row containing the cell whose rectangle you want.

## See Also

- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](nstableview/userinterfacelayoutdirection.md)
  The layout direction of the user interface.
- [func rect(ofColumn: Int) -> NSRect](nstableview/rect(ofcolumn:).md)
  Returns the rectangle containing the column at the specified index.
- [func rect(ofRow: Int) -> NSRect](nstableview/rect(ofrow:).md)
  Returns the rectangle containing the row at the specified index.
- [func rows(in: NSRect) -> NSRange](nstableview/rows(in:).md)
  Returns a range of indexes for the rows that lie wholly or partially within the vertical boundaries of the specified rectangle.
- [func columnIndexes(in: NSRect) -> IndexSet](nstableview/columnindexes(in:).md)
  Returns the indexes of the table view’s columns that intersect the specified rectangle.
- [func column(at: NSPoint) -> Int](nstableview/column(at:).md)
  Returns the index of the column the specified point lies in.
- [func row(at: NSPoint) -> Int](nstableview/row(at:).md)
  Returns the index of the row the specified point lies in.
- [var columnAutoresizingStyle: NSTableView.ColumnAutoresizingStyle](nstableview/columnautoresizingstyle-swift.property.md)
  The table view’s column autoresizing style.
- [func sizeLastColumnToFit()](nstableview/sizelastcolumntofit.md)
  Resizes the last column so the table view fits exactly within its enclosing clip view.
- [func noteNumberOfRowsChanged()](nstableview/notenumberofrowschanged.md)
  Informs the table view that the number of records in its data source has changed.
- [func tile()](nstableview/tile.md)
  Properly sizes the table view and its header view and marks it as needing display.
- [func sizeToFit()](nstableview/sizetofit.md)
  Sizes the  table view based on a uniform column autoresizing style.
- [func noteHeightOfRows(withIndexesChanged: IndexSet)](nstableview/noteheightofrows(withindexeschanged:).md)
  Informs the table view that the rows specified in `indexSet` have changed height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/frameofcell(atcolumn:row:))*