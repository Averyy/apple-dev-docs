# cell(withTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Searches the receiver and returns the last cell matching the specified tag.

**Availability**:
- macOS

## Declaration

```swift
func cell(withTag tag: Int) -> NSCell?
```

```objc
- (NSCell *) cellWithTag:(NSInteger) tag;
```

## Return Value

The last (when viewing the matrix as a row-ordered array) [`NSCell`](../nscell.md) object that has a tag matching `anInt`, or `nil` if no such cell exists

## Parameters

- `tag`: The tag of the cell to return.

## See Also

### Related Documentation
- [func selectCell(withTag: Int) -> Bool](./selectcell%28withtag%29.md)
  Selects the last cell with the given tag.
- [var tag: Int](../nsactioncell/tag.md)
  Returns the receiver’s tag.
### Finding Cells
- [var selectedCells: [NSCell]](./selectedcells.md)
  An array containing all of the matrix’s highlighted cells plus its selected cell.
- [var selectedColumn: Int](./selectedcolumn.md)
  The column number of the selected cell.
- [var selectedRow: Int](./selectedrow.md)
  The row number of the selected cell.
- [func cell(atRow: Int, column: Int) -> NSCell?](./cell%28atrow,column%29.md)
  Returns the cell at the specified row and column.
- [var cells: [NSCell]](./cells.md)
  An array containing the cells of the matrix.
- [selectedCell](./selectedcell.md)
  The most recently selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/cell(withtag:))*