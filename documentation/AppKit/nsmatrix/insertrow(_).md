# insertRow(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts a new row of cells before the specified row.

**Availability**:
- macOS

## Declaration

```swift
func insertRow(_ row: Int)
```

```objc
- (void) insertRow:(NSInteger) row;
```

## Discussion

New cells are created if needed with [`makeCell(atRow:column:)`](./makecell%28atrow,column%29.md). This method redraws the receiver. Your code may need to send [`sizeToCells()`](./sizetocells%28%29.md) after sending this method to resize the receiver to fit the newly added cells.

If the number of rows or columns in the receiver has been changed with [`renewRows(_:columns:)`](./renewrows%28_,columns%29.md), then new cells are created only if they’re needed. This fact allows you to grow and shrink an [`NSMatrix`](../nsmatrix.md) without repeatedly creating and freeing the cells.

## Parameters

- `row`: The location at which to insert the new row. If this is greater than the number of rows in the receiver, enough rows are created to expand the receiver to be `row` rows high.

## See Also

### Laying Out the Cells of the Matrix
- [func addColumn()](./addcolumn%28%29.md)
  Adds a new column of cells to the right of the last column.
- [func addColumn(with: [NSCell])](./addcolumn%28with%29.md)
  Adds a new column of cells to the right of the last column, using the given cells.
- [func addRow()](./addrow%28%29.md)
  Adds a new row of cells below the last row.
- [func addRow(with: [NSCell])](./addrow%28with%29.md)
  Adds a new row of cells below the last row, using the specified cells.
- [func cellFrame(atRow: Int, column: Int) -> NSRect](./cellframe%28atrow,column%29.md)
  Returns the frame rectangle of the cell that would be drawn at the specified location.
- [var cellSize: NSSize](./cellsize.md)
  The size of each cell in the matrix.
- [func getNumberOfRows(UnsafeMutablePointer<Int>?, columns: UnsafeMutablePointer<Int>?)](./getnumberofrows%28_,columns%29.md)
  Obtains the number of rows and columns in the receiver.
- [func insertColumn(Int)](./insertcolumn%28_%29.md)
  Inserts a new column of cells at the specified location.
- [func insertColumn(Int, with: [NSCell]?)](./insertcolumn%28_,with%29.md)
  Inserts a new column of cells before the specified column, using the given cells.
- [func insertRow(Int, with: [NSCell]?)](./insertrow%28_,with%29.md)
  Inserts a new row of cells before the specified row, using the given cells.
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The vertical and horizontal spacing between cells in the matrix.
- [func makeCell(atRow: Int, column: Int) -> NSCell](./makecell%28atrow,column%29.md)
  Creates a new cell at the location specified by the given row and column in the receiver.
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns in the matrix.
- [var numberOfRows: Int](./numberofrows.md)
  The number of rows in the matrix.
- [func putCell(NSCell, atRow: Int, column: Int)](./putcell%28_,atrow,column%29.md)
  Replaces the cell at the specified row and column with the new cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/insertrow(_:))*