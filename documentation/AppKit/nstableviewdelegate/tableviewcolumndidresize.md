# tableViewColumnDidResize(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that a table column was resized.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func tableViewColumnDidResize(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  .

## See Also

- [func tableView(NSTableView, shouldReorderColumn: Int, toColumn: Int) -> Bool](nstableviewdelegate/tableview(_:shouldreordercolumn:tocolumn:).md)
  Asks the delegate to allow or prohibit the specified column to be dragged to a new location.
- [func tableView(NSTableView, didDrag: NSTableColumn)](nstableviewdelegate/tableview(_:diddrag:).md)
  Tells the delegate that the specified table column was dragged.
- [func tableViewColumnDidMove(Notification)](nstableviewdelegate/tableviewcolumndidmove(_:).md)
  Tells the delegate that a table column was moved by user action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableviewcolumndidresize(_:))*