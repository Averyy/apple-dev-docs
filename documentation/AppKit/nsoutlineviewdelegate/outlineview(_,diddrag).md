# outlineView(_:didDrag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent at the time the mouse button goes up in `outlineView` and `tableColumn` has been dragged during the time the mouse button was down.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, didDrag tableColumn: NSTableColumn)
```

```objc
- (void) outlineView:(NSOutlineView *) outlineView didDragTableColumn:(NSTableColumn *) tableColumn;
```

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column.

## See Also

### Working with Table Columns
- [func outlineView(NSOutlineView, mouseDownInHeaderOf: NSTableColumn)](./outlineview%28_,mousedowninheaderof%29.md)
  Sent to the delegate whenever the mouse button is clicked in `outlineView` while the cursor is in a column header `tableColumn`.
- [func outlineView(NSOutlineView, didClick: NSTableColumn)](./outlineview%28_,didclick%29.md)
  Sent at the time the mouse button subsequently goes up in `outlineView` and `tableColumn` has been “clicked” without having been dragged anywhere.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:diddrag:))*