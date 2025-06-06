# parentForItems(inColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the item that contains the children located in the specified column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func parentForItems(inColumn column: Int) -> Any?
```

#### Return Value

The parent item for the specified column.

## Parameters

- `column`: The column.

## See Also

- [func loadedCell(atRow: Int, column: Int) -> Any?](nsbrowser/loadedcell(atrow:column:).md)
  Loads, if necessary, and returns the cell at the specified row and column location.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/parentforitems(incolumn:))*