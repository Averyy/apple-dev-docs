# item(atRow:inColumn:)

**Framework**: AppKit  
**Kind**: method

Returns the item located at the specified row and column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func item(atRow row: Int, inColumn column: Int) -> Any?
```

#### Return Value

The item.

## Parameters

- `row`: The row of the item.
- `column`: The column of the item.

## See Also

- [func loadedCell(atRow: Int, column: Int) -> Any?](nsbrowser/loadedcell(atrow:column:).md)
  Loads, if necessary, and returns the cell at the specified row and column location.
- [func editItem(at: IndexPath, with: NSEvent?, select: Bool)](nsbrowser/edititem(at:with:select:).md)
  Begins editing the item at the specified path.
- [func item(at: IndexPath) -> Any?](nsbrowser/item(at:).md)
  Returns the item at the specified index path.
- [func indexPath(forColumn: Int) -> IndexPath](nsbrowser/indexpath(forcolumn:).md)
  Returns the index path of the item whose children are displayed in the given column.
- [func isLeafItem(Any?) -> Bool](nsbrowser/isleafitem(_:).md)
  Returns whether the specified item is a leaf item.
- [func parentForItems(inColumn: Int) -> Any?](nsbrowser/parentforitems(incolumn:).md)
  Returns the item that contains the children located in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/item(atrow:incolumn:))*