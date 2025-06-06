# outlineView(_:willDisplayOutlineCell:for:item:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate that an outline view is about to display a cell used to draw the expansion symbol.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, willDisplayOutlineCell cell: Any, for tableColumn: NSTableColumn?, item: Any)
```

#### Discussion

Informs the delegate that `outlineView` is about to display `cell`—an expandable cell (a cell that has the expansion symbol)—for the column and item specified by `tableColumn` and `item`. The delegate can modify cell to alter its display attributes.

This method is not invoked when `outlineView` is about to display a non-expandable cell.

## Parameters

- `outlineView`: The outline view that sent the message.
- `cell`: The cell.
- `tableColumn`: The table column.
- `item`: The item.

## See Also

- [func outlineView(NSOutlineView, willDisplayCell: Any, for: NSTableColumn?, item: Any)](nsoutlineviewdelegate/outlineview(_:willdisplaycell:for:item:).md)
  Informs the delegate that the cell specified by the column and item will be displayed.
- [func outlineView(NSOutlineView, dataCellFor: NSTableColumn?, item: Any) -> NSCell?](nsoutlineviewdelegate/outlineview(_:datacellfor:item:).md)
  Returns the cell to use in a given column for a given item.
- [func outlineView(NSOutlineView, shouldShowOutlineCellForItem: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldshowoutlinecellforitem:).md)
  Returns whether the specified item should display the outline cell (the disclosure triangle).
- [func outlineView(NSOutlineView, shouldShowCellExpansionFor: NSTableColumn?, item: Any) -> Bool](nsoutlineviewdelegate/outlineview(_:shouldshowcellexpansionfor:item:).md)
  Invoked to allow the delegate to control cell expansion for a specific column and item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:willdisplayoutlinecell:for:item:))*