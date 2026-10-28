# parentForItems(inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the item that contains the children located in the specified column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func parentForItems(inColumn column: Int) -> Any?
```

```objc
- (id) parentForItemsInColumn:(NSInteger) column;
```

## Return Value

The parent item for the specified column.

## Parameters

- `column`: The column.

## See Also

### Accessing Components
- [func loadedCell(atRow: Int, column: Int) -> Any?](./loadedcell%28atrow,column%29.md)
  Loads, if necessary, and returns the cell at the specified row and column location.
- [func editItem(at: IndexPath, with: NSEvent?, select: Bool)](./edititem%28at,with,select%29.md)
  Begins editing the item at the specified path.
- [func item(at: IndexPath) -> Any?](./item%28at%29.md)
  Returns the item at the specified index path.
- [func item(atRow: Int, inColumn: Int) -> Any?](./item%28atrow,incolumn%29.md)
  Returns the item located at the specified row and column.
- [func indexPath(forColumn: Int) -> IndexPath](./indexpath%28forcolumn%29.md)
  Returns the index path of the item whose children are displayed in the given column.
- [func isLeafItem(Any?) -> Bool](./isleafitem%28_%29.md)
  Returns whether the specified item is a leaf item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/parentforitems(incolumn:))*