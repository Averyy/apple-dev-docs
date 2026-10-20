# tableView(_:didClick:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the mouse button was clicked in the specified table column, but the column was not dragged.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, didClick tableColumn: NSTableColumn)
```

```objc
- (void) tableView:(NSTableView *) tableView didClickTableColumn:(NSTableColumn *) tableColumn;
```

## Parameters

- `tableView`: The table view that sent the message.
- `tableColumn`: The table column.

## See Also

### Responding to mouse events
- [func tableView(NSTableView, mouseDownInHeaderOf: NSTableColumn)](./tableview%28_,mousedowninheaderof%29.md)
  Tells the delegate that the mouse button was clicked in the specified table column’s header.
- [func tableView(NSTableView, shouldTrackCell: NSCell, for: NSTableColumn?, row: Int) -> Bool](./tableview%28_,shouldtrackcell,for,row%29.md)
  Asks the delegate whether the specified cell should be tracked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:didclick:))*