# userInterfaceLayoutDirection

**Framework**: AppKit  
**Kind**: property

The layout direction of the user interface.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection { get set }
```

#### Discussion

The default value of this property is [`NSUserInterfaceLayoutDirection.leftToRight`](nsuserinterfacelayoutdirection/lefttoright.md). When the property is set to [`NSUserInterfaceLayoutDirection.rightToLeft`](nsuserinterfacelayoutdirection/righttoleft.md), the table view flips the visual order of the table columns, but the logical order remains unchanged. Although this property was introduced in macOS 10.12, in earlier versions the property always returned [`NSUserInterfaceLayoutDirection.leftToRight`](nsuserinterfacelayoutdirection/lefttoright.md).

## See Also

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
- [func noteHeightOfRows(withIndexesChanged: IndexSet)](nstableview/noteheightofrows(withindexeschanged:).md)
  Informs the table view that the rows specified in `indexSet` have changed height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/userinterfacelayoutdirection)*