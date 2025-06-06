# selectedCells

**Framework**: AppKit  
**Kind**: property

All cells selected in the rightmost column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectedCells: [NSCell]? { get }
```

#### Discussion

When the array is empty, there is no selection.

## See Also

- [func selectedCell(inColumn: Int) -> Any?](nsbrowser/selectedcell(incolumn:).md)
  Returns the last (lowest) cell selected in the given column.
- [func selectAll(Any?)](nsbrowser/selectall(_:).md)
  Selects all cells in the last column of the browser.
- [func selectedRow(inColumn: Int) -> Int](nsbrowser/selectedrow(incolumn:).md)
  Returns the row index of the selected cell in the specified column.
- [func selectRow(Int, inColumn: Int)](nsbrowser/selectrow(_:incolumn:).md)
  Selects the cell at the specified row and column index.
- [var selectionIndexPath: IndexPath?](nsbrowser/selectionindexpath.md)
  The index path of the item selected in the browser.
- [var selectionIndexPaths: [IndexPath]](nsbrowser/selectionindexpaths.md)
  An array containing the index paths of all items selected in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectedcells)*