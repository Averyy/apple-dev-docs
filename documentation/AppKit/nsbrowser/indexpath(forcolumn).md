# indexPath(forColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index path of the item whose children are displayed in the given column.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func indexPath(forColumn column: Int) -> IndexPath
```

```objc
- (NSIndexPath *) indexPathForColumn:(NSInteger) column;
```

#### Return Value

The index path of the column.

#### Discussion

This method can only be used if the delegate implements the item data source methods.

## Parameters

- `column`: The column to find the index path for.

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
- [func isLeafItem(Any?) -> Bool](./isleafitem%28_%29.md)
  Returns whether the specified item is a leaf item.
- [func parentForItems(inColumn: Int) -> Any?](./parentforitems%28incolumn%29.md)
  Returns the item that contains the children located in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/indexpath(forcolumn:))*