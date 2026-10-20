# loadedCell(atRow:column:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Loads, if necessary, and returns the cell at the specified row and column location.

**Availability**:
- macOS

## Declaration

```swift
func loadedCell(atRow row: Int, column col: Int) -> Any?
```

```objc
- (id) loadedCellAtRow:(NSInteger) row column:(NSInteger) col;
```

## Parameters

- `row`: The row index of the cell to return.
- `col`: The column index of the cell to return.

## See Also

### Related Documentation
- [func selectRow(Int, inColumn: Int)](./selectrow%28_,incolumn%29.md)
  Selects the cell at the specified row and column index.
- [func selectedCell(inColumn: Int) -> Any?](./selectedcell%28incolumn%29.md)
  Returns the last (lowest) cell selected in the given column.
### Accessing Components
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
- [func parentForItems(inColumn: Int) -> Any?](./parentforitems%28incolumn%29.md)
  Returns the item that contains the children located in the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/loadedcell(atrow:column:))*