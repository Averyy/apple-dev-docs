# selectedCell

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The most recently selected cell.

**Availability**:
- macOS

## Declaration

```objc
@property (strong, readonly, nullable) NSCell * selectedCell;
```

## Discussion

When the value of this property is `nil`, no cell is selected. If more than one cell is selected, the value of this property is the cell that is lowest and farthest to the right in the matrix.

## See Also

### Finding Cells
- [var selectedCells: [NSCell]](./selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](./selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](./selectedrow.md)
  The row number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](./cell%28atrow,column%29.md)
  Returns the cell at the specified row and column.
- [func cell(withTag: Int) -> NSCell?](./cell%28withtag%29.md)
  Searches the receiver and returns the last cell matching the specified tag.
- [var cells: [NSCell]](./cells.md)
  An array containing the cells of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectedcell)*