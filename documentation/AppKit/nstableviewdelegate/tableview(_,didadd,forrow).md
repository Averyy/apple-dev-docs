# tableView(_:didAdd:forRow:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that a row view was added at the specified row.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: NSTableView, didAdd rowView: NSTableRowView, forRow row: Int)
```

```objc
- (void) tableView:(NSTableView *) tableView didAddRowView:(NSTableRowView *) rowView forRow:(NSInteger) row;
```

#### Discussion

At this point, the delegate can add extra views, or modify the properties of `rowView`.

> **Note**:  This method is only valid for [`NSView`](../nsview.md)-based table views.

## Parameters

- `tableView`: The table view that sent the message.
- `rowView`: The row view.
- `row`: The index of the row.

## See Also

### Notification of row views being added or removed
- [func tableView(NSTableView, didRemove: NSTableRowView, forRow: Int)](./tableview%28_,didremove,forrow%29.md)
  Tells the delegate that a row view was removed from the table at the specified row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:didadd:forrow:))*