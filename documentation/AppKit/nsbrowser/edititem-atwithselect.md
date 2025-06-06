# editItem(at:with:select:)

**Framework**: AppKit  
**Kind**: method

Begins editing the item at the specified path.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func editItem(at indexPath: IndexPath, with event: NSEvent?, select: Bool)
```

## Parameters

- `indexPath`: The path of the item.
- `event`: The event to use when beginning the edit.
- `select`: If  , the cells contents will be selected; if  , they will not be selected.

## See Also

- [func loadedCell(atRow: Int, column: Int) -> Any?](nsbrowser/loadedcell(atrow:column:).md)
  Loads, if necessary, and returns the cell at the specified row and column location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/edititem(at:with:select:))*