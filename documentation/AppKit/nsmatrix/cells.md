# cells

**Framework**: AppKit  
**Kind**: property

An array containing the cells of the matrix.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var cells: [NSCell] { get }
```

#### Discussion

The cells in the array are row-ordered; that is, the first row of cells appears first in the array, followed by the second row, and so forth.

## See Also

- [var selectedCells: [NSCell]](nsmatrix/selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](nsmatrix/selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](nsmatrix/selectedrow.md)
  The row number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](nsmatrix/cell(atrow:column:).md)
  Returns the cell at the specified row and column.
- [func cell(withTag: Int) -> NSCell?](nsmatrix/cell(withtag:).md)
  Searches the receiver and returns the last cell matching the specified tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/cells)*