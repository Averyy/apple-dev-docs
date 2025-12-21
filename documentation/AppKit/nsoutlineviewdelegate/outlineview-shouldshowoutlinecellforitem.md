# outlineView(_:shouldShowOutlineCellForItem:)

**Framework**: AppKit  
**Kind**: method

Returns whether the specified item should display the outline cell (the disclosure triangle).

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldShowOutlineCellForItem item: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the outline cell should be displayed, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Returning [`false`](https://developer.apple.com/documentation/Swift/false) causes [`frameOfOutlineCell(atRow:)`](nsoutlineview/frameofoutlinecell(atrow:).md) to return `NSZeroRect`, hiding the cell. In addition, the row will not be collapsible by keyboard shortcuts.

This method is called only for expandable rows.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: An item in the outline view.

## See Also

- [func outlineView(NSOutlineView, willDisplayCell: Any, for: NSTableColumn?, item: Any)](nsoutlineviewdelegate/outlineview(_:willdisplaycell:for:item:).md)
  Informs the delegate that the cell specified by the column and item will be displayed.
- [func outlineView(NSOutlineView, willDisplayOutlineCell: Any, for: NSTableColumn?, item: Any)](nsoutlineviewdelegate/outlineview(_:willdisplayoutlinecell:for:item:).md)
  Informs the delegate that an outline view is about to display a cell used to draw the expansion symbol.
- [func outlineView(NSOutlineView, dataCellFor: NSTableColumn?, item: Any) -> NSCell?](nsoutlineviewdelegate/outlineview(_:datacellfor:item:).md)
  Returns the cell to use in a given column for a given item.
- [func outlineView(NSOutlineView, shouldShowCellExpansionFor: NSTableColumn?, item: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldshowcellexpansionfor:item:).md)
  Invoked to allow the delegate to control cell expansion for a specific column and item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldshowoutlinecellforitem:))*