# selectionIndexPath

**Framework**: AppKit  
**Kind**: property

The index path of the item selected in the browser.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var selectionIndexPath: IndexPath? { get set }
```

#### Discussion

When the value of this property is `nil`, there is no selection.

## See Also

- [func selectedCell(inColumn: Int) -> Any?](nsbrowser/selectedcell(incolumn:).md)
  Returns the last (lowest) cell selected in the given column.
- [var selectedCells: [NSCell]?](nsbrowser/selectedcells.md)
  All cells selected in the rightmost column.
- [func selectAll(Any?)](nsbrowser/selectall(_:).md)
  Selects all cells in the last column of the browser.
- [func selectedRow(inColumn: Int) -> Int](nsbrowser/selectedrow(incolumn:).md)
  Returns the row index of the selected cell in the specified column.
- [func selectRow(Int, inColumn: Int)](nsbrowser/selectrow(_:incolumn:).md)
  Selects the cell at the specified row and column index.
- [var selectionIndexPaths: [IndexPath]](nsbrowser/selectionindexpaths.md)
  An array containing the index paths of all items selected in the browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectionindexpath)*