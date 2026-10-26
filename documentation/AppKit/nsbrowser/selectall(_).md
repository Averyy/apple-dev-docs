# selectAll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects all cells in the last column of the browser.

**Availability**:
- macOS

## Declaration

```swift
func selectAll(_ sender: Any?)
```

```objc
- (void) selectAll:(id) sender;
```

## See Also

### Related Documentation
- [var selectedColumn: Int](./selectedcolumn.md)
  The index of the last column with a selected item.
- [selectedCell](./selectedcell.md)
  The last (rightmost and lowest) selected cell.
### Managing Selection
- [func selectedCell(inColumn: Int) -> Any?](./selectedcell%28incolumn%29.md)
  Returns the last (lowest) cell selected in the given column.
- [var selectedCells: [NSCell]?](./selectedcells.md)
  All cells selected in the rightmost column.
- [func selectedRow(inColumn: Int) -> Int](./selectedrow%28incolumn%29.md)
  Returns the row index of the selected cell in the specified column.
- [func selectRow(Int, inColumn: Int)](./selectrow%28_,incolumn%29.md)
  Selects the cell at the specified row and column index.
- [var selectionIndexPath: IndexPath?](./selectionindexpath.md)
  The index path of the item selected in the browser.
- [var selectionIndexPaths: [IndexPath]](./selectionindexpaths.md)
  An array containing the index paths of all items selected in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectall(_:))*