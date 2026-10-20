# outlineView(_:shouldShowOutlineCellForItem:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether the specified item should display the outline cell (the disclosure triangle).

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldShowOutlineCellForItem item: Any) -> Bool
```

```objc
- (BOOL) outlineView:(NSOutlineView *) outlineView shouldShowOutlineCellForItem:(id) item;
```

#### Return Value

[`true`](../../Swift/true.md) if the outline cell should be displayed, otherwise [`false`](../../Swift/false.md).

#### Discussion

Returning [`false`](../../Swift/false.md) causes [`frameOfOutlineCell(atRow:)`](../nsoutlineview/frameofoutlinecell%28atrow%29.md) to return `NSZeroRect`, hiding the cell. In addition, the row will not be collapsible by keyboard shortcuts.

This method is called only for expandable rows.

## Parameters

- `outlineView`: The outline view that sent the message.
- `item`: An item in the outline view.

## See Also

### Displaying Cells
- [func outlineView(NSOutlineView, willDisplayCell: Any, for: NSTableColumn?, item: Any)](./outlineview%28_,willdisplaycell,for,item%29.md)
  Informs the delegate that the cell specified by the column and item will be displayed.
- [func outlineView(NSOutlineView, willDisplayOutlineCell: Any, for: NSTableColumn?, item: Any)](./outlineview%28_,willdisplayoutlinecell,for,item%29.md)
  Informs the delegate that an outline view is about to display a cell used to draw the expansion symbol.
- [func outlineView(NSOutlineView, dataCellFor: NSTableColumn?, item: Any) -> NSCell?](./outlineview%28_,datacellfor,item%29.md)
  Returns the cell to use in a given column for a given item.
- [func outlineView(NSOutlineView, shouldShowCellExpansionFor: NSTableColumn?, item: Any) -> Bool](./outlineview%28_,shouldshowcellexpansionfor,item%29.md)
  Invoked to allow the delegate to control cell expansion for a specific column and item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldshowoutlinecellforitem:))*