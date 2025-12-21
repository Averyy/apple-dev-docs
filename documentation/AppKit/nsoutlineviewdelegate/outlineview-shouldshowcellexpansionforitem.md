# outlineView(_:shouldShowCellExpansionFor:item:)

**Framework**: AppKit  
**Kind**: method

Invoked to allow the delegate to control cell expansion for a specific column and item.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldShowCellExpansionFor tableColumn: NSTableColumn?, item: Any) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow an expansion tooltip to appear in the column `tableColumn` for item `item`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Cell expansion can occur when the mouse hovers over the specified cell and the cell contents are unable to be fully displayed within the cell. If this method returns [`true`](https://developer.apple.com/documentation/Swift/true), the full cell contents will be shown in a special floating tool tip view, otherwise the content is truncated.

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: A table column in the outline view.
- `item`: An item in the outline view.

## See Also

- [func outlineView(NSOutlineView, willDisplayCell: Any, for: NSTableColumn?, item: Any)](nsoutlineviewdelegate/outlineview(_:willdisplaycell:for:item:).md)
  Informs the delegate that the cell specified by the column and item will be displayed.
- [func outlineView(NSOutlineView, willDisplayOutlineCell: Any, for: NSTableColumn?, item: Any)](nsoutlineviewdelegate/outlineview(_:willdisplayoutlinecell:for:item:).md)
  Informs the delegate that an outline view is about to display a cell used to draw the expansion symbol.
- [func outlineView(NSOutlineView, dataCellFor: NSTableColumn?, item: Any) -> NSCell?](nsoutlineviewdelegate/outlineview(_:datacellfor:item:).md)
  Returns the cell to use in a given column for a given item.
- [func outlineView(NSOutlineView, shouldShowOutlineCellForItem: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldshowoutlinecellforitem:).md)
  Returns whether the specified item should display the outline cell (the disclosure triangle).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldshowcellexpansionfor:item:))*