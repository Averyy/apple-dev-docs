# makeCell(atRow:column:)

**Framework**: AppKit  
**Kind**: method

Creates a new cell at the location specified by the given row and column in the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func makeCell(atRow row: Int, column col: Int) -> NSCell
```

#### Return Value

The newly created cell.

#### Discussion

If the receiver has a prototype cell, it’s copied to create the new cell. If not, and if the receiver has a cell class set, it allocates and initializes (with `init`) an instance of that class. If the receiver hasn’t had either a prototype cell or a cell class set, [`NSMatrix`](nsmatrix.md) creates an [`NSActionCell`](nsactioncell.md).

Your code should never invoke this method directly; it’s used by [`addRow()`](nsmatrix/addrow().md) and other methods when a cell must be created. It may be overridden to provide more specific initialization of cells.

## Parameters

- `row`: The row in which to create the new cell.
- `col`: The column in which to create the new cell.

## See Also

- [var prototype: NSCell?](nsmatrix/prototype.md)
  The prototype cell that’s copied whenever the matrix creates a new cell.
- [var cellClass: AnyClass](nsmatrix/cellclass.md)
  The subclass of [`NSCell`](nscell.md) that the matrix uses when creating new (empty) cells.
- [func addColumn()](nsmatrix/addcolumn.md)
  Adds a new column of cells to the right of the last column.
- [func addColumn(with: [NSCell])](nsmatrix/addcolumn(with:).md)
  Adds a new column of cells to the right of the last column, using the given cells.
- [func addRow()](nsmatrix/addrow.md)
  Adds a new row of cells below the last row.
- [func addRow(with: [NSCell])](nsmatrix/addrow(with:).md)
  Adds a new row of cells below the last row, using the specified cells.
- [func cellFrame(atRow: Int, column: Int) -> NSRect](nsmatrix/cellframe(atrow:column:).md)
  Returns the frame rectangle of the cell that would be drawn at the specified location.
- [var cellSize: NSSize](nsmatrix/cellsize.md)
  The size of each cell in the matrix.
- [func getNumberOfRows(UnsafeMutablePointer<Int>?, columns: UnsafeMutablePointer<Int>?)](nsmatrix/getnumberofrows(_:columns:).md)
  Obtains the number of rows and columns in the receiver.
- [func insertColumn(Int)](nsmatrix/insertcolumn(_:).md)
  Inserts a new column of cells at the specified location.
- [func insertColumn(Int, with: [NSCell]?)](nsmatrix/insertcolumn(_:with:).md)
  Inserts a new column of cells before the specified column, using the given cells.
- [func insertRow(Int)](nsmatrix/insertrow(_:).md)
  Inserts a new row of cells before the specified row.
- [func insertRow(Int, with: [NSCell]?)](nsmatrix/insertrow(_:with:).md)
  Inserts a new row of cells before the specified row, using the given cells.
- [var intercellSpacing: NSSize](nsmatrix/intercellspacing.md)
  The vertical and horizontal spacing between cells in the matrix.
- [var numberOfColumns: Int](nsmatrix/numberofcolumns.md)
  The number of columns in the matrix.
- [var numberOfRows: Int](nsmatrix/numberofrows.md)
  The number of rows in the matrix.
- [func putCell(NSCell, atRow: Int, column: Int)](nsmatrix/putcell(_:atrow:column:).md)
  Replaces the cell at the specified row and column with the new cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/makecell(atrow:column:))*