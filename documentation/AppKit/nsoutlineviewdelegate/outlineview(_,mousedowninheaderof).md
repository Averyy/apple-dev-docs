# outlineView(_:mouseDownInHeaderOf:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate whenever the mouse button is clicked in `outlineView` while the cursor is in a column header `tableColumn`.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, mouseDownInHeaderOf tableColumn: NSTableColumn)
```

```objc
- (void) outlineView:(NSOutlineView *) outlineView mouseDownInHeaderOfTableColumn:(NSTableColumn *) tableColumn;
```

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: The table column.

## See Also

### Working with Table Columns
- [func outlineView(NSOutlineView, didClick: NSTableColumn)](./outlineview%28_,didclick%29.md)
  Sent at the time the mouse button subsequently goes up in `outlineView` and `tableColumn` has been “clicked” without having been dragged anywhere.
- [func outlineView(NSOutlineView, didDrag: NSTableColumn)](./outlineview%28_,diddrag%29.md)
  Sent at the time the mouse button goes up in `outlineView` and `tableColumn` has been dragged during the time the mouse button was down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:mousedowninheaderof:))*