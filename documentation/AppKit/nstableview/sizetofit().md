# sizeToFit()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sizes the  table view based on a uniform column autoresizing style.

**Availability**:
- macOS

## Declaration

```swift
func sizeToFit()
```

```objc
- (void) sizeToFit;
```

## Discussion

All columns are resized to the same size, up to a column’s maximum size. This method then invokes [`tile()`](./tile%28%29.md).

## See Also

### Layout Support
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](./userinterfacelayoutdirection.md)
  The layout direction of the user interface.
- [func rect(ofColumn: Int) -> NSRect](./rect%28ofcolumn%29.md)
  Returns the rectangle containing the column at the specified index.
- [func rect(ofRow: Int) -> NSRect](./rect%28ofrow%29.md)
  Returns the rectangle containing the row at the specified index.
- [func rows(in: NSRect) -> NSRange](./rows%28in%29.md)
  Returns a range of indexes for the rows that lie wholly or partially within the vertical boundaries of the specified rectangle.
- [func columnIndexes(in: NSRect) -> IndexSet](./columnindexes%28in%29.md)
  Returns the indexes of the table view’s columns that intersect the specified rectangle.
- [func column(at: NSPoint) -> Int](./column%28at%29.md)
  Returns the index of the column the specified point lies in.
- [func row(at: NSPoint) -> Int](./row%28at%29.md)
  Returns the index of the row the specified point lies in.
- [func frameOfCell(atColumn: Int, row: Int) -> NSRect](./frameofcell%28atcolumn,row%29.md)
  Returns a rectangle locating the cell that lies at the intersection of the specified column and row.
- [var columnAutoresizingStyle: NSTableView.ColumnAutoresizingStyle](./columnautoresizingstyle-swift.property.md)
  The table view’s column autoresizing style.
- [func sizeLastColumnToFit()](./sizelastcolumntofit%28%29.md)
  Resizes the last column so the table view fits exactly within its enclosing clip view.
- [func noteNumberOfRowsChanged()](./notenumberofrowschanged%28%29.md)
  Informs the table view that the number of records in its data source has changed.
- [func tile()](./tile%28%29.md)
  Properly sizes the table view and its header view and marks it as needing display.
- [func noteHeightOfRows(withIndexesChanged: IndexSet)](./noteheightofrows%28withindexeschanged%29.md)
  Informs the table view that the rows specified in `indexSet` have changed height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/sizetofit())*