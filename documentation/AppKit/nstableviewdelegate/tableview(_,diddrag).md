# tableView(_:didDrag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified table column was dragged.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, didDrag tableColumn: NSTableColumn)
```

```objc
- (void) tableView:(NSTableView *) tableView didDragTableColumn:(NSTableColumn *) tableColumn;
```

#### Discussion

Specifically, this method is sent when the mouse button goes up in `tableView` and `tableColumn` has been dragged during the time the mouse button was down. In macOS 10.5 and later the dragged column is sent to the delegate. (In earlier versions of macOS the table column that’s currently located at the dragged column’s original index is sent.)

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.

## See Also

### Moving and resizing columns
- [func tableView(NSTableView, shouldReorderColumn: Int, toColumn: Int) -> Bool](./tableview%28_,shouldreordercolumn,tocolumn%29.md)
  Asks the delegate to allow or prohibit the specified column to be dragged to a new location.
- [func tableViewColumnDidMove(Notification)](./tableviewcolumndidmove%28_%29.md)
  Tells the delegate that a table column was moved by user action.
- [func tableViewColumnDidResize(Notification)](./tableviewcolumndidresize%28_%29.md)
  Tells the delegate that a table column was resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:diddrag:))*