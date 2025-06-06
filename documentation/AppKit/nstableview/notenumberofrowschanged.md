# noteNumberOfRowsChanged()

**Framework**: Appkit  
**Kind**: method

Informs the table view that the number of records in its data source has changed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func noteNumberOfRowsChanged()
```

#### Discussion

This method allows the table view to update the scrollers in its scroll view without actually reloading data into the table view. It’s useful for a data source that continually receives data in the background over a period of time, in which case the table view can remain responsive to the user while the data is received.

See the [`NSTableViewDataSource`](nstableviewdatasource.md) protocol specification for information on the messages an `NSTableView` object sends to its data source.

> **Note**:  When using [`NSView`](nsview.md)-based table views this method should be avoided. The table will query the data source for the new number of rows, and properly insert (or remove) rows at the end of the table as necessary with an animation. When using [`NSCell`](nscell.md)-based table views this method tells the table that there may be more (or less) rows available and to reload state based on that information. This method does not work for [`NSOutlineView`](nsoutlineview.md), and should not be called.

## See Also

- [func reloadData()](nstableview/reloaddata.md)
  Marks the table view as needing redisplay, so it will reload the data for visible cells and draw the new values.
- [func numberOfRows(in: NSTableView) -> Int](nstableviewdatasource/numberofrows(in:).md)
  Returns the number of records managed for `aTableView` by the data source object.
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
- [func tile()](nstableview/tile.md)
  Properly sizes the table view and its header view and marks it as needing display.
- [func sizeToFit()](nstableview/sizetofit.md)
  Sizes the  table view based on a uniform column autoresizing style.
- [func noteHeightOfRows(withIndexesChanged: IndexSet)](nstableview/noteheightofrows(withindexeschanged:).md)
  Informs the table view that the rows specified in `indexSet` have changed height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/notenumberofrowschanged())*