# tableView(_:shouldReorderColumn:toColumn:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to allow or prohibit the specified column to be dragged to a new location.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldReorderColumn columnIndex: Int, toColumn newColumnIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the column reordering should be allowed, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

When a column is initially dragged by the user, the delegate is first called with a `newColumnIndex` value of `-1`. Returning [`false`](https://developer.apple.com/documentation/swift/false) will disallow that column from being reordered at all. Returning [`true`](https://developer.apple.com/documentation/swift/true) allows it to be reordered, and the delegate will be called again when the column reaches a new location.

The actual [`NSTableColumn`](nstablecolumn.md) instance can be retrieved from the [`tableColumns`](nstableview/tablecolumns.md) array.

If this method isn’t implemented, all columns are considered reorderable.

## Parameters

- `tableView`: The table view that sent the message.
- `columnIndex`: The index of the column being dragged.
- `newColumnIndex`: The proposed target index of the column.

## See Also

- [func tableView(NSTableView, didDrag: NSTableColumn)](nstableviewdelegate/tableview(_:diddrag:).md)
  Tells the delegate that the specified table column was dragged.
- [func tableViewColumnDidMove(Notification)](nstableviewdelegate/tableviewcolumndidmove(_:).md)
  Tells the delegate that a table column was moved by user action.
- [func tableViewColumnDidResize(Notification)](nstableviewdelegate/tableviewcolumndidresize(_:).md)
  Tells the delegate that a table column was resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldreordercolumn:tocolumn:))*