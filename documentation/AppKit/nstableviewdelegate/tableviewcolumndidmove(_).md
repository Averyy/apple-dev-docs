# tableViewColumnDidMove(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a table column was moved by user action.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func tableViewColumnDidMove(_ notification: Notification)
```

```objc
- (void) tableViewColumnDidMove:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`columnDidMoveNotification`](../nstableview/columndidmovenotification.md).

## See Also

### Moving and resizing columns
- [func tableView(NSTableView, shouldReorderColumn: Int, toColumn: Int) -> Bool](./tableview%28_,shouldreordercolumn,tocolumn%29.md)
  Asks the delegate to allow or prohibit the specified column to be dragged to a new location.
- [func tableView(NSTableView, didDrag: NSTableColumn)](./tableview%28_,diddrag%29.md)
  Tells the delegate that the specified table column was dragged.
- [func tableViewColumnDidResize(Notification)](./tableviewcolumndidresize%28_%29.md)
  Tells the delegate that a table column was resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableviewcolumndidmove(_:))*