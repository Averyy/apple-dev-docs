# reloadData()

**Framework**: AppKit  
**Kind**: method

Marks the table view as needing redisplay, so it will reload the data for visible cells and draw the new values.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reloadData()
```

#### Discussion

This method forces a redraw of all the visible cells in the table view. If you want to update the value in a single cell, column, or row, it is more efficient to use [`frameOfCell(atColumn:row:)`](nstableview/frameofcell(atcolumn:row:).md), [`rect(ofColumn:)`](nstableview/rect(ofcolumn:).md), or [`rect(ofRow:)`](nstableview/rect(ofrow:).md) in conjunction with the [`setNeedsDisplay(_:)`](nsview/setneedsdisplay(_:).md) method of [`NSView`](nsview.md). If you just want to update the scroller, use [`noteNumberOfRowsChanged()`](nstableview/notenumberofrowschanged().md); if the height of a set of rows changes, use [`noteHeightOfRows(withIndexesChanged:)`](nstableview/noteheightofrows(withindexeschanged:).md).

> **Note**:  For [`NSView`](nsview.md)-based table views, this method drops all the visible row views and cell views, and re-acquires them all.

 For [`NSView`](nsview.md)-based table views, this method drops all the visible row views and cell views, and re-acquires them all.

## See Also

- [func noteHeightOfRows(withIndexesChanged: IndexSet)](nstableview/noteheightofrows(withindexeschanged:).md)
  Informs the table view that the rows specified in `indexSet` have changed height.
- [func frameOfCell(atColumn: Int, row: Int) -> NSRect](nstableview/frameofcell(atcolumn:row:).md)
  Returns a rectangle locating the cell that lies at the intersection of the specified column and row.
- [func noteNumberOfRowsChanged()](nstableview/notenumberofrowschanged.md)
  Informs the table view that the number of records in its data source has changed.
- [func rect(ofColumn: Int) -> NSRect](nstableview/rect(ofcolumn:).md)
  Returns the rectangle containing the column at the specified index.
- [func rect(ofRow: Int) -> NSRect](nstableview/rect(ofrow:).md)
  Returns the rectangle containing the row at the specified index.
- [var dataSource: (any NSTableViewDataSource)?](nstableview/datasource.md)
  The object that provides the data displayed by the table view.
- [var usesStaticContents: Bool](nstableview/usesstaticcontents.md)
  A Boolean value indicating whether the table uses static data.
- [func reloadData(forRowIndexes: IndexSet, columnIndexes: IndexSet)](nstableview/reloaddata(forrowindexes:columnindexes:).md)
  Reloads the data for only the specified rows and columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/reloaddata())*