# renewRows(_:columns:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Changes the number of rows and columns in the receiver.

**Availability**:
- macOS

## Declaration

```swift
func renewRows(_ newRows: Int, columns newCols: Int)
```

```objc
- (void) renewRows:(NSInteger) newRows columns:(NSInteger) newCols;
```

#### Discussion

This method uses the same cells as before, creating new cells only if the new size is larger; it never frees cells. It doesn’t redisplay the receiver. Your code should normally send [`sizeToCells()`](./sizetocells%28%29.md) after invoking this method to resize the receiver so it fits the changed cell arrangement. This method deselects all cells in the receiver.

## Parameters

- `newRows`: The new number of rows in the matrix.
- `newCols`: The new number of columns in the matrix.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/renewrows(_:columns:))*