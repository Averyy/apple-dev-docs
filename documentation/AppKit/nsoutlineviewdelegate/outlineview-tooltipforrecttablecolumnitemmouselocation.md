# outlineView(_:toolTipFor:rect:tableColumn:item:mouseLocation:)

**Framework**: AppKit  
**Kind**: method

When the cursor pauses over a given cell, the value returned from this method is displayed in a tooltip.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, toolTipFor cell: NSCell, rect: NSRectPointer, tableColumn: NSTableColumn?, item: Any, mouseLocation: NSPoint) -> String
```

#### Return Value

If you don’t want a tooltip at that location, return an empty string.

## Parameters

- `outlineView`: The outline view that sent the message.
- `cell`: The cell for which to generate a tooltip.
- `rect`: The proposed active area of the tooltip. To control the default active area, you can modify the   parameter. By default,   is computed as  .
- `tableColumn`: The table column that contains  .
- `item`: The item for which to display a tooltip.
- `mouseLocation`: The current mouse location in view coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:tooltipfor:rect:tablecolumn:item:mouselocation:))*