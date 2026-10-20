# moveColumn(_:toColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the column and heading at the specified index to the new specified index.

**Availability**:
- macOS

## Declaration

```swift
func moveColumn(_ oldIndex: Int, toColumn newIndex: Int)
```

```objc
- (void) moveColumn:(NSInteger) oldIndex toColumn:(NSInteger) newIndex;
```

#### Discussion

This method posts [`columnDidMoveNotification`](./columndidmovenotification.md) to the default notification center.

## Parameters

- `oldIndex`: The current index in the [`tableColumns`](./tablecolumns.md) array of the column to move.
- `newIndex`: The new index in the [`tableColumns`](./tablecolumns.md) array for the moved column.

## See Also

### Column Management
- [func addTableColumn(NSTableColumn)](./addtablecolumn%28_%29.md)
  Adds the specified column as the last column of the table view.
- [func removeTableColumn(NSTableColumn)](./removetablecolumn%28_%29.md)
  Removes the specified column from the table view.
- [var tableColumns: [NSTableColumn]](./tablecolumns.md)
  An array containing the current table column objects.
- [func column(withIdentifier: NSUserInterfaceItemIdentifier) -> Int](./column%28withidentifier%29.md)
  Returns the index of the first column in the table view whose identifier is equal to the specified identifier.
- [func tableColumn(withIdentifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?](./tablecolumn%28withidentifier%29.md)
  Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/movecolumn(_:tocolumn:))*