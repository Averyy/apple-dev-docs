# sort(using:context:)

**Framework**: AppKit  
**Kind**: method

Sorts the receiver’s cells in ascending order as defined by the specified comparison function.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func sort(using compare: (Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)
```

## Parameters

- `compare`: The function to use when comparing cells. The comparison function is used to compare two elements at a time and should return   if the first element is smaller than the second,   if the first element is larger than the second, and   if the elements are equal.
- `context`: Context passed to the comparison function as its third argument, each time its called. This allows the comparison to be based on some outside parameter, such as whether character sorting is case-sensitive or case-insensitive.

## See Also

- [func sort(_ compare: (Any, Any, UnsafeMutableRawPointer?) -> Int, context: UnsafeMutableRawPointer?)](../Foundation/NSMutableArray/sort(_:context:).md)
  Sorts the receiver in ascending order as defined by the comparison function `compare`.
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
  Inserts a new column of cells at the specified location. .
- [func insertColumn(Int, with: [NSCell]?)](nsmatrix/insertcolumn(_:with:).md)
  Inserts a new column of cells before the specified column, using the given cells.
- [func insertRow(Int)](nsmatrix/insertrow(_:).md)
  Inserts a new row of cells before the specified row.
- [func insertRow(Int, with: [NSCell]?)](nsmatrix/insertrow(_:with:).md)
  Inserts a new row of cells before the specified row, using the given cells.
- [var intercellSpacing: NSSize](nsmatrix/intercellspacing.md)
  The vertical and horizontal spacing between cells in the matrix.
- [func makeCell(atRow: Int, column: Int) -> NSCell](nsmatrix/makecell(atrow:column:).md)
  Creates a new cell at the location specified by the given row and column in the receiver.
- [var numberOfColumns: Int](nsmatrix/numberofcolumns.md)
  The number of columns in the matrix.
- [var numberOfRows: Int](nsmatrix/numberofrows.md)
  The number of rows in the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/sort(using:context:))*