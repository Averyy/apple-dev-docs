# reloadData()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Marks the table view as needing redisplay, so it will reload the data for visible cells and draw the new values.

**Availability**:
- macOS

## Declaration

```swift
func reloadData()
```

```objc
- (void) reloadData;
```

#### Discussion

This method forces a redraw of all the visible cells in the table view. If you want to update the value in a single cell, column, or row, it is more efficient to use [`frameOfCell(atColumn:row:)`](./frameofcell%28atcolumn,row%29.md), [`rect(ofColumn:)`](./rect%28ofcolumn%29.md), or [`rect(ofRow:)`](./rect%28ofrow%29.md) in conjunction with the [`setNeedsDisplay(_:)`](../nsview/setneedsdisplay%28_%29.md) method of [`NSView`](../nsview.md). If you just want to update the scroller, use [`noteNumberOfRowsChanged()`](./notenumberofrowschanged%28%29.md); if the height of a set of rows changes, use [`noteHeightOfRows(withIndexesChanged:)`](./noteheightofrows%28withindexeschanged%29.md).

> **Note**:  For [`NSView`](../nsview.md)-based table views, this method drops all the visible row views and cell views, and re-acquires them all.

## See Also

### Related Documentation
- [func noteHeightOfRows(withIndexesChanged: IndexSet)](./noteheightofrows%28withindexeschanged%29.md)
  Informs the table view that the rows specified in `indexSet` have changed height.
- [func frameOfCell(atColumn: Int, row: Int) -> NSRect](./frameofcell%28atcolumn,row%29.md)
  Returns a rectangle locating the cell that lies at the intersection of the specified column and row.
- [func noteNumberOfRowsChanged()](./notenumberofrowschanged%28%29.md)
  Informs the table view that the number of records in its data source has changed.
- [func rect(ofColumn: Int) -> NSRect](./rect%28ofcolumn%29.md)
  Returns the rectangle containing the column at the specified index.
- [func rect(ofRow: Int) -> NSRect](./rect%28ofrow%29.md)
  Returns the rectangle containing the row at the specified index.
### Managing the Table’s Data
- [var dataSource: (any NSTableViewDataSource)?](./datasource.md)
  The object that provides the data displayed by the table view.
- [var usesStaticContents: Bool](./usesstaticcontents.md)
  A Boolean value indicating whether the table uses static data.
- [func reloadData(forRowIndexes: IndexSet, columnIndexes: IndexSet)](./reloaddata%28forrowindexes,columnindexes%29.md)
  Reloads the data for only the specified rows and columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/reloaddata())*