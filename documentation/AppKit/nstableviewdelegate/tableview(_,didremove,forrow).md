# tableView(_:didRemove:forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a row view was removed from the table at the specified row.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, didRemove rowView: NSTableRowView, forRow row: Int)
```

```objc
- (void) tableView:(NSTableView *) tableView didRemoveRowView:(NSTableRowView *) rowView forRow:(NSInteger) row;
```

#### Discussion

If `row` equals `-1`, the row is being deleted from the table and is no longer a valid row; otherwise `row` is a valid row that is being removed by being moved off screen.

> **Note**:  This method is only valid for [`NSView`](../nsview.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `rowView`: The row view.
- `row`: The index of the row.

## See Also

### Notification of row views being added or removed
- [func tableView(NSTableView, didAdd: NSTableRowView, forRow: Int)](./tableview%28_,didadd,forrow%29.md)
  Tells the delegate that a row view was added at the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:didremove:forrow:))*