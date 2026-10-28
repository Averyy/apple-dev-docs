# insertColumn(_:with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts a new column of cells before the specified column, using the given cells.

**Availability**:
- macOS

## Declaration

```swift
func insertColumn(_ column: Int, with newCells: [NSCell]?)
```

```objc
- (void) insertColumn:(NSInteger) column withCells:(NSArray<NSCell *> *) newCells;
```

## Discussion

If `column` is greater than the number of columns in the receiver, enough columns are created to expand the receiver to be `column` columns wide. `newCells` should either be empty or contain a sufficient number of cells to fill each new column. If `newCells` is `nil` or an array with no elements, the call is equivalent to calling [`insertColumn(_:)`](./insertcolumn%28_%29.md). Extra cells are ignored, unless the matrix is empty. In that case, a matrix is created with one column and enough rows for all the elements of `newCells`.

This method redraws the receiver. Your code may need to send [`sizeToCells()`](./sizetocells%28%29.md) after sending this method to resize the receiver to fit the newly added cells.

## Parameters

- `column`: The column at which to insert the new cells.
- `newCells`: An array of objects to use to fill the new column, starting with the object at index 0. Each object should be an instance of [`NSCell`](../nscell.md) or one of its subclasses (usually [`NSActionCell`](../nsactioncell.md)).

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
- [func insertRow(Int)](./insertrow%28_%29.md)
  Inserts a new row of cells before the specified row.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/insertcolumn(_:with:))*