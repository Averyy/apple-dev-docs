# outlineView(_:mouseDownInHeaderOf:)

**Framework**: AppKit  
**Kind**: method

Sent to the delegate whenever the mouse button is clicked in `outlineView` while the cursor is in a column header `tableColumn`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, mouseDownInHeaderOf tableColumn: NSTableColumn)
```

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column.

## See Also

- [func outlineView(NSOutlineView, didClick: NSTableColumn)](nsoutlineviewdelegate/outlineview(_:didclick:).md)
  Sent at the time the mouse button subsequently goes up in `outlineView` and `tableColumn` has been “clicked” without having been dragged anywhere.
- [func outlineView(NSOutlineView, didDrag: NSTableColumn)](nsoutlineviewdelegate/outlineview(_:diddrag:).md)
  Sent at the time the mouse button goes up in `outlineView` and `tableColumn` has been dragged during the time the mouse button was down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:mousedowninheaderof:))*