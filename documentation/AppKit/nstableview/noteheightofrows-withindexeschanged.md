# noteHeightOfRows(withIndexesChanged:)

**Framework**: AppKit  
**Kind**: method

Informs the table view that the rows specified in `indexSet` have changed height.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func noteHeightOfRows(withIndexesChanged indexSet: IndexSet)
```

#### Discussion

If the delegate implements [`tableView(_:heightOfRow:)`](nstableviewdelegate/tableview(_:heightofrow:).md) this method immediately retiles the table view using the row heights the delegate provides.

For [`NSView`](nsview.md)-based tables, this method will animate. To turn off the animation, create an [`NSAnimationContext`](nsanimationcontext.md) grouping and set the [`duration`](nsanimationcontext/duration.md) to 0. Then call this method and end the grouping.

For [`NSCell`](nscell.md)-based tables, this method normally doesn’t animate. However, it will animate if you call it inside a [`beginUpdates()`](nstableview/beginupdates().md)/[`endUpdates()`](nstableview/endupdates().md) block.

## Parameters

- `indexSet`: Index set of rows that have changed their height.

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
- [func frameOfCell(atColumn: Int, row: Int) -> NSRect](nstableview/frameofcell(atcolumn:row:).md)
  Returns a rectangle locating the cell that lies at the intersection of the specified column and row.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/noteheightofrows(withindexeschanged:))*