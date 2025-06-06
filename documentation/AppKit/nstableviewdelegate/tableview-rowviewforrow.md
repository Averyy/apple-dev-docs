# tableView(_:rowViewForRow:)

**Framework**: Appkit  
**Kind**: method

Asks the delegate for a view to display the specified row.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, rowViewForRow row: Int) -> NSTableRowView?
```

#### Return Value

An instance or subclass of [`NSTableRowView`](nstablerowview.md). If `nil` is returned, an [`NSTableRowView`](nstablerowview.md) instance will be created and used.

#### Discussion

The delegate can implement this method to return a custom [`NSTableRowView`](nstablerowview.md) for `row`.

The reuse queue can be used in the same way as documented in [`tableView(_:viewFor:row:)`](nstableviewdelegate/tableview(_:viewfor:row:).md). The returned view will have attributes properly set to it before it’s added to the `tableView`.

> **Note**:  This method is only valid for [`NSView`](nsview.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `row`: The row index.

## See Also

- [func tableView(NSTableView, viewFor: NSTableColumn?, row: Int) -> NSView?](nstableviewdelegate/tableview(_:viewfor:row:).md)
  Asks the delegate for a view to display the specified row and column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:rowviewforrow:))*