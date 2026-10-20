# selectionIndexPaths

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the index paths of all items selected in the browser.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var selectionIndexPaths: [IndexPath] { get set }
```

```objc
@property (copy) NSArray<NSIndexPath *> * selectionIndexPaths;
```

## See Also

### Managing Selection
- [func selectedCell(inColumn: Int) -> Any?](./selectedcell%28incolumn%29.md)
  Returns the last (lowest) cell selected in the given column.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectionindexpaths)*