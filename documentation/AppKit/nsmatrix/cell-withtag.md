# cell(withTag:)

**Framework**: AppKit  
**Kind**: method

Searches the receiver and returns the last cell matching the specified tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func cell(withTag tag: Int) -> NSCell?
```

#### Return Value

The last (when viewing the matrix as a row-ordered array) [`NSCell`](nscell.md) object that has a tag matching `anInt`, or `nil` if no such cell exists

## Parameters

- `tag`: The tag of the cell to return.

## See Also

- [func selectCell(withTag: Int) -> Bool](nsmatrix/selectcell(withtag:).md)
  Selects the last cell with the given tag.
- [var tag: Int](nsactioncell/tag.md)
  Returns the receiver’s tag.
- [var selectedCells: [NSCell]](nsmatrix/selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](nsmatrix/selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](nsmatrix/selectedrow.md)
  The row number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](nsmatrix/cell(atrow:column:).md)
  Returns the cell at the specified row and column.
- [var cells: [NSCell]](nsmatrix/cells.md)
  An array containing the cells of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/cell(withtag:))*