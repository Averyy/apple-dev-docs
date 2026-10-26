# selectRow(_:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the cell at the specified row and column index.

**Availability**:
- macOS

## Declaration

```swift
func selectRow(_ row: Int, inColumn column: Int)
```

```objc
- (void) selectRow:(NSInteger) row inColumn:(NSInteger) column;
```

## Parameters

- `row`: The row index of the cell to select.
- `column`: The column index of the cell to select.

## See Also

### Related Documentation
- [func loadedCell(atRow: Int, column: Int) -> Any?](./loadedcell%28atrow,column%29.md)
  Loads, if necessary, and returns the cell at the specified row and column location.
### Managing Selection
- [func selectedCell(inColumn: Int) -> Any?](./selectedcell%28incolumn%29.md)
  Returns the last (lowest) cell selected in the given column.
- [var selectedCells: [NSCell]?](./selectedcells.md)
  All cells selected in the rightmost column.
- [func selectAll(Any?)](./selectall%28_%29.md)
  Selects all cells in the last column of the browser.
- [func selectedRow(inColumn: Int) -> Int](./selectedrow%28incolumn%29.md)
  Returns the row index of the selected cell in the specified column.
- [var selectionIndexPath: IndexPath?](./selectionindexpath.md)
  The index path of the item selected in the browser.
- [var selectionIndexPaths: [IndexPath]](./selectionindexpaths.md)
  An array containing the index paths of all items selected in the browser.
- [selectedCell](./selectedcell.md)
  The last (rightmost and lowest) selected cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectrow(_:incolumn:))*