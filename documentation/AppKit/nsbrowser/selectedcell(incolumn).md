# selectedCell(inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the last (lowest) cell selected in the given column.

**Availability**:
- macOS

## Declaration

```swift
func selectedCell(inColumn column: Int) -> Any?
```

```objc
- (id) selectedCellInColumn:(NSInteger) column;
```

## Return Value

The last (or lowest) selected cell. Returns `nil` if there is no selection.

## Parameters

- `column`: The column whose last selected cell is to be returned.

## See Also

### Related Documentation
- [func loadedCell(atRow: Int, column: Int) -> Any?](./loadedcell%28atrow,column%29.md)
  Loads, if necessary, and returns the cell at the specified row and column location.
### Managing Selection
- [var selectedCells: [NSCell]?](./selectedcells.md)
  All cells selected in the rightmost column.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects all cells in the last column of the browser.
- [func selectedRow(inColumn: Int) -> Int](./selectedrow%28incolumn%29.md)
  Returns the row index of the selected cell in the specified column.
- [func selectRow(Int, inColumn: Int)](./selectrow%28_,incolumn%29.md)
  Selects the cell at the specified row and column index.
- [var selectionIndexPath: IndexPath?](./selectionindexpath.md)
  The index path of the item selected in the browser.
- [var selectionIndexPaths: [IndexPath]](./selectionindexpaths.md)
  An array containing the index paths of all items selected in the browser.
- [selectedCell](./selectedcell.md)
  The last (rightmost and lowest) selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectedcell(incolumn:))*