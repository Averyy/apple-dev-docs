# selectedCells

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing all of the matrix’s highlighted cells plus its selected cell.

**Availability**:
- macOS

## Declaration

```swift
var selectedCells: [NSCell] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSCell *> * selectedCells;
```

#### Discussion

See the class description for a discussion of the selected cell.

As an alternative to using [`setSelectionFrom(_:to:anchor:highlight:)`](./setselectionfrom%28_,to,anchor,highlight%29.md) for programmatically making discontiguous selections of cells in a matrix, you could first set the single selected cell and then set subsequent cells to be highlighted; afterwards you can access [`selectedCells`](./selectedcells.md) to obtain the selection of cells.

## See Also

### Related Documentation
- [var isHighlighted: Bool](../nscell/ishighlighted.md)
  A Boolean value indicating whether the cell has a highlighted appearance.
### Finding Cells
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selectedcells)*