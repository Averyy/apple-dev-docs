# column(withIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the first column in the table view whose identifier is equal to the specified identifier.

**Availability**:
- macOS

## Declaration

```swift
func column(withIdentifier identifier: NSUserInterfaceItemIdentifier) -> Int
```

```objc
- (NSInteger) columnWithIdentifier:(NSUserInterfaceItemIdentifier) identifier;
```

## Return Value

The index in the [`tableColumns`](./tablecolumns.md) array of the first column in the table view whose identifier is equal to `anObject` (when compared using `isEqual:`), or `–1` if no columns are found with the specified identifier.

## Parameters

- `identifier`: A column identifier.

## See Also

### Column Management
- [func addTableColumn(NSTableColumn)](./addtablecolumn%28_%29.md)
  Adds the specified column as the last column of the table view.
- [func removeTableColumn(NSTableColumn)](./removetablecolumn%28_%29.md)
  Removes the specified column from the table view.
- [func moveColumn(Int, toColumn: Int)](./movecolumn%28_,tocolumn%29.md)
  Moves the column and heading at the specified index to the new specified index.
- [var tableColumns: [NSTableColumn]](./tablecolumns.md)
  An array containing the current table column objects.
- [func tableColumn(withIdentifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?](./tablecolumn%28withidentifier%29.md)
  Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/column(withidentifier:))*