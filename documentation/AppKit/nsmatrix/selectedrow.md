# selectedRow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The row number of the selected cell.

**Availability**:
- macOS

## Declaration

```swift
var selectedRow: Int { get }
```

```objc
@property (readonly) NSInteger selectedRow;
```

## Discussion

When the value of this property is `–1`, no cells are selected. If cells in multiple rows are selected, the value of this property is the number of the last row containing a selected cell.

## See Also

### Finding Cells
- [var selectedCells: [NSCell]](./selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](./selectedcolumn.md)
  The column number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](./cell%28atrow,column%29.md)
  Returns the cell at the specified row and column.
- [func cell(withTag: Int) -> NSCell?](./cell%28withtag%29.md)
  Searches the receiver and returns the last cell matching the specified tag.
- [var cells: [NSCell]](./cells.md)
  An array containing the cells of the matrix.
- [selectedCell](./selectedcell.md)
  The most recently selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectedrow)*