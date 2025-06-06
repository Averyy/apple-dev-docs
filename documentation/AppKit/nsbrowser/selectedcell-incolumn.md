# selectedCell(inColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the last (lowest) cell selected in the given column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectedCell(inColumn column: Int) -> Any?
```

#### Return Value

The last (or lowest) selected cell. Returns `nil` if there is no selection.

## Parameters

- `column`: The column whose last selected cell is to be returned.

## See Also

- [func loadedCell(atRow: Int, column: Int) -> Any?](nsbrowser/loadedcell(atrow:column:).md)
  Loads, if necessary, and returns the cell at the specified row and column location.
- [var selectedCells: [NSCell]?](nsbrowser/selectedcells.md)
  All cells selected in the rightmost column.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectedcell(incolumn:))*