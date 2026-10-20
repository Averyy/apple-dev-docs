# tableView(_:shouldReorderColumn:toColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to allow or prohibit the specified column to be dragged to a new location.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, shouldReorderColumn columnIndex: Int, toColumn newColumnIndex: Int) -> Bool
```

```objc
- (BOOL) tableView:(NSTableView *) tableView shouldReorderColumn:(NSInteger) columnIndex toColumn:(NSInteger) newColumnIndex;
```

#### Return Value

[`true`](../../Swift/true.md) if the column reordering should be allowed, otherwise [`false`](../../Swift/false.md).

#### Discussion

When a column is initially dragged by the user, the delegate is first called with a `newColumnIndex` value of `-1`. Returning [`false`](../../Swift/false.md) will disallow that column from being reordered at all. Returning [`true`](../../Swift/true.md) allows it to be reordered, and the delegate will be called again when the column reaches a new location.

The actual [`NSTableColumn`](../nstablecolumn.md) instance can be retrieved from the [`tableColumns`](../nstableview/tablecolumns.md) array.

If this method isn’t implemented, all columns are considered reorderable.

## Parameters

- `tableView`: The table view that sent the message.
- `columnIndex`: The index of the column being dragged.
- `newColumnIndex`: The proposed target index of the column.

## See Also

### Moving and resizing columns
- [func tableView(NSTableView, didDrag: NSTableColumn)](./tableview%28_,diddrag%29.md)
  Tells the delegate that the specified table column was dragged.
- [func tableViewColumnDidMove(Notification)](./tableviewcolumndidmove%28_%29.md)
  Tells the delegate that a table column was moved by user action.
- [func tableViewColumnDidResize(Notification)](./tableviewcolumndidresize%28_%29.md)
  Tells the delegate that a table column was resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:shouldreordercolumn:tocolumn:))*