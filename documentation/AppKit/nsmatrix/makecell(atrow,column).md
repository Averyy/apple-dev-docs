# makeCell(atRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a new cell at the location specified by the given row and column in the receiver.

**Availability**:
- macOS

## Declaration

```swift
func makeCell(atRow row: Int, column col: Int) -> NSCell
```

```objc
- (NSCell *) makeCellAtRow:(NSInteger) row column:(NSInteger) col;
```

#### Return Value

The newly created cell.

#### Discussion

If the receiver has a prototype cell, it’s copied to create the new cell. If not, and if the receiver has a cell class set, it allocates and initializes (with `init`) an instance of that class. If the receiver hasn’t had either a prototype cell or a cell class set, [`NSMatrix`](../nsmatrix.md) creates an [`NSActionCell`](../nsactioncell.md).

Your code should never invoke this method directly; it’s used by [`addRow()`](./addrow%28%29.md) and other methods when a cell must be created. It may be overridden to provide more specific initialization of cells.

## Parameters

- `row`: The row in which to create the new cell.
- `col`: The column in which to create the new cell.

## See Also

### Related Documentation
- [var prototype: NSCell?](./prototype.md)
  The prototype cell that’s copied whenever the matrix creates a new cell.
- [var cellClass: AnyClass](./cellclass.md)
  The subclass of [`NSCell`](../nscell.md) that the matrix uses when creating new (empty) cells.
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
- [var numberOfColumns: Int](./numberofcolumns.md)
  The number of columns in the matrix.
- [var numberOfRows: Int](./numberofrows.md)
  The number of rows in the matrix.
- [func putCell(NSCell, atRow: Int, column: Int)](./putcell%28_,atrow,column%29.md)
  Replaces the cell at the specified row and column with the new cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/makecell(atrow:column:))*