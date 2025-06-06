# outlineView(_:didClick:)

**Framework**: AppKit  
**Kind**: method

Sent at the time the mouse button subsequently goes up in `outlineView` and `tableColumn` has been “clicked” without having been dragged anywhere.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, didClick tableColumn: NSTableColumn)
```

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column.

## See Also

- [func outlineView(NSOutlineView, mouseDownInHeaderOf: NSTableColumn)](nsoutlineviewdelegate/outlineview(_:mousedowninheaderof:).md)
  Sent to the delegate whenever the mouse button is clicked in `outlineView` while the cursor is in a column header `tableColumn`.
- [func outlineView(NSOutlineView, didDrag: NSTableColumn)](nsoutlineviewdelegate/outlineview(_:diddrag:).md)
  Sent at the time the mouse button goes up in `outlineView` and `tableColumn` has been dragged during the time the mouse button was down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:didclick:))*