# loadedCell(atRow:column:)

**Framework**: AppKit  
**Kind**: method

Loads, if necessary, and returns the cell at the specified row and column location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func loadedCell(atRow row: Int, column col: Int) -> Any?
```

## Parameters

- `row`: The row index of the cell to return.
- `col`: The column index of the cell to return.

## See Also

- [func selectRow(Int, inColumn: Int)](nsbrowser/selectrow(_:incolumn:).md)
  Selects the cell at the specified row and column index.
- [func selectedCell(inColumn: Int) -> Any?](nsbrowser/selectedcell(incolumn:).md)
  Returns the last (lowest) cell selected in the given column.
- [func editItem(at: IndexPath, with: NSEvent?, select: Bool)](nsbrowser/edititem(at:with:select:).md)
  Begins editing the item at the specified path.
- [func item(at: IndexPath) -> Any?](nsbrowser/item(at:).md)
  Returns the item at the specified index path.
- [func item(atRow: Int, inColumn: Int) -> Any?](nsbrowser/item(atrow:incolumn:).md)
  Returns the item located at the specified row and column.
- [func indexPath(forColumn: Int) -> IndexPath](nsbrowser/indexpath(forcolumn:).md)
  Returns the index path of the item whose children are displayed in the given column.
- [func isLeafItem(Any?) -> Bool](nsbrowser/isleafitem(_:).md)
  Returns whether the specified item is a leaf item.
- [func parentForItems(inColumn: Int) -> Any?](nsbrowser/parentforitems(incolumn:).md)
  Returns the item that contains the children located in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/loadedcell(atrow:column:))*