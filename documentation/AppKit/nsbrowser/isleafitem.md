# isLeafItem(_:)

**Framework**: AppKit  
**Kind**: method

Returns whether the specified item is a leaf item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func isLeafItem(_ item: Any?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the item is a leaf item; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method may return [`false`](https://developer.apple.com/documentation/Swift/false) if the item has never been displayed in the browser or accessed via [`item(at:)`](nsbrowser/item(at:).md). Overriding this method has no effect. It may be used only if the browser’s delegate implements the item data source methods.

## Parameters

- `item`: The item to be checked.

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
- [func parentForItems(inColumn: Int) -> Any?](nsbrowser/parentforitems(incolumn:).md)
  Returns the item that contains the children located in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/isleafitem(_:))*