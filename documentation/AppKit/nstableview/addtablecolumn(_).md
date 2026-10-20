# addTableColumn(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified column as the last column of the table view.

**Availability**:
- macOS

## Declaration

```swift
func addTableColumn(_ tableColumn: NSTableColumn)
```

```objc
- (void) addTableColumn:(NSTableColumn *) tableColumn;
```

## Parameters

- `tableColumn`: The column to add to the table view.

## See Also

### Related Documentation
- [func sizeLastColumnToFit()](./sizelastcolumntofit%28%29.md)
  Resizes the last column so the table view fits exactly within its enclosing clip view.
### Column Management
- [func removeTableColumn(NSTableColumn)](./removetablecolumn%28_%29.md)
  Removes the specified column from the table view.
- [func moveColumn(Int, toColumn: Int)](./movecolumn%28_,tocolumn%29.md)
  Moves the column and heading at the specified index to the new specified index.
- [var tableColumns: [NSTableColumn]](./tablecolumns.md)
  An array containing the current table column objects.
- [func column(withIdentifier: NSUserInterfaceItemIdentifier) -> Int](./column%28withidentifier%29.md)
  Returns the index of the first column in the table view whose identifier is equal to the specified identifier.
- [func tableColumn(withIdentifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?](./tablecolumn%28withidentifier%29.md)
  Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/addtablecolumn(_:))*