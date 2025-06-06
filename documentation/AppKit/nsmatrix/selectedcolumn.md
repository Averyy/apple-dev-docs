# selectedColumn

**Framework**: AppKit  
**Kind**: property

The column number of the selected cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectedColumn: Int { get }
```

#### Discussion

When the value of this property is `–1`, no cells are selected. If cells in multiple columns are selected,  the value of this property is the number of the last (rightmost) column containing a selected cell.

## See Also

- [var selectedCells: [NSCell]](nsmatrix/selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedRow: Int](nsmatrix/selectedrow.md)
  The row number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](nsmatrix/cell(atrow:column:).md)
  Returns the cell at the specified row and column.
- [func cell(withTag: Int) -> NSCell?](nsmatrix/cell(withtag:).md)
  Searches the receiver and returns the last cell matching the specified tag.
- [var cells: [NSCell]](nsmatrix/cells.md)
  An array containing the cells of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectedcolumn)*