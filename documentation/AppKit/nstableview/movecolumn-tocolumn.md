# moveColumn(_:toColumn:)

**Framework**: AppKit  
**Kind**: method

Moves the column and heading at the specified index to the new specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func moveColumn(_ oldIndex: Int, toColumn newIndex: Int)
```

#### Discussion

This method posts [`columnDidMoveNotification`](nstableview/columndidmovenotification.md) to the default notification center.

## Parameters

- `oldIndex`: The current index in the   array of the column to move.
- `newIndex`: The new index in the   array for the moved column.

## See Also

- [func addTableColumn(NSTableColumn)](nstableview/addtablecolumn(_:).md)
  Adds the specified column as the last column of the table view.
- [func removeTableColumn(NSTableColumn)](nstableview/removetablecolumn(_:).md)
  Removes the specified column from the table view.
- [var tableColumns: [NSTableColumn]](nstableview/tablecolumns.md)
  An array containing the current table column objects.
- [func column(withIdentifier: NSUserInterfaceItemIdentifier) -> Int](nstableview/column(withidentifier:).md)
  Returns the index of the first column in the table view whose identifier is equal to the specified identifier.
- [func tableColumn(withIdentifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?](nstableview/tablecolumn(withidentifier:).md)
  Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/movecolumn(_:tocolumn:))*