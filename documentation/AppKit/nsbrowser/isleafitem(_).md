# isLeafItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the specified item is a leaf item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func isLeafItem(_ item: Any?) -> Bool
```

```objc
- (BOOL) isLeafItem:(id) item;
```

## Return Value

[`true`](../../Swift/true.md) if the item is a leaf item; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method may return [`false`](../../Swift/false.md) if the item has never been displayed in the browser or accessed via [`item(at:)`](./item%28at%29.md). Overriding this method has no effect. It may be used only if the browser’s delegate implements the item data source methods.

## Parameters

- `item`: The item to be checked.

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
- [func parentForItems(inColumn: Int) -> Any?](./parentforitems%28incolumn%29.md)
  Returns the item that contains the children located in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/isleafitem(_:))*