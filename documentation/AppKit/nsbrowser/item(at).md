# item(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the item at the specified index path.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func item(at indexPath: IndexPath) -> Any?
```

```objc
- (id) itemAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

The item.

## Discussion

This method can only be used if the delegate implements the item data source methods. The specified index path must be displayable in the browser.

## Parameters

- `indexPath`: The index path of the item to return.

## See Also

### Accessing Components
- [func loadedCell(atRow: Int, column: Int) -> Any?](./loadedcell%28atrow,column%29.md)
  Loads, if necessary, and returns the cell at the specified row and column location.
- [func editItem(at: IndexPath, with: NSEvent?, select: Bool)](./edititem%28at,with,select%29.md)
  Begins editing the item at the specified path.
- [func item(atRow: Int, inColumn: Int) -> Any?](./item%28atrow,incolumn%29.md)
  Returns the item located at the specified row and column.
- [func indexPath(forColumn: Int) -> IndexPath](./indexpath%28forcolumn%29.md)
  Returns the index path of the item whose children are displayed in the given column.
- [func isLeafItem(Any?) -> Bool](./isleafitem%28_%29.md)
  Returns whether the specified item is a leaf item.
- [func parentForItems(inColumn: Int) -> Any?](./parentforitems%28incolumn%29.md)
  Returns the item that contains the children located in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/item(at:))*