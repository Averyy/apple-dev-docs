# editItem(at:with:select:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Begins editing the item at the specified path.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func editItem(at indexPath: IndexPath, with event: NSEvent?, select: Bool)
```

```objc
- (void) editItemAtIndexPath:(NSIndexPath *) indexPath withEvent:(NSEvent *) event select:(BOOL) select;
```

## Parameters

- `indexPath`: The path of the item.
- `event`: The event to use when beginning the edit.
- `select`: If [`true`](../../Swift/true.md), the cells contents will be selected; if [`false`](../../Swift/false.md), they will not be selected.

## See Also

### Accessing Components
- [func loadedCell(atRow: Int, column: Int) -> Any?](./loadedcell%28atrow,column%29.md)
  Loads, if necessary, and returns the cell at the specified row and column location.
- [func item(at: IndexPath) -> Any?](./item%28at%29.md)
  Returns the item at the specified index path.
- [func item(atRow: Int, inColumn: Int) -> Any?](./item%28atrow,incolumn%29.md)
  Returns the item located at the specified row and column.
- [func indexPath(forColumn: Int) -> IndexPath](./indexpath%28forcolumn%29.md)
  Returns the index path of the item whose children are displayed in the given column.
- [func isLeafItem(Any?) -> Bool](./isleafitem%28_%29.md)
  Returns whether the specified item is a leaf item.
- [func parentForItems(inColumn: Int) -> Any?](./parentforitems%28incolumn%29.md)
  Returns the item that contains the children located in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/edititem(at:with:select:))*