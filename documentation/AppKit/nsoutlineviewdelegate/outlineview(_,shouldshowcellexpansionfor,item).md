# outlineView(_:shouldShowCellExpansionFor:item:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked to allow the delegate to control cell expansion for a specific column and item.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func outlineView(_ outlineView: NSOutlineView, shouldShowCellExpansionFor tableColumn: NSTableColumn?, item: Any) -> Bool
```

```objc
- (BOOL) outlineView:(NSOutlineView *) outlineView shouldShowCellExpansionForTableColumn:(NSTableColumn *) tableColumn item:(id) item;
```

## Return Value

[`true`](../../Swift/true.md) to allow an expansion tooltip to appear in the column `tableColumn` for item `item`, otherwise [`false`](../../Swift/false.md).

## Discussion

Cell expansion can occur when the mouse hovers over the specified cell and the cell contents are unable to be fully displayed within the cell. If this method returns [`true`](../../Swift/true.md), the full cell contents will be shown in a special floating tool tip view, otherwise the content is truncated.

## Parameters

- `outlineView`: The outline view that sent the message.
- `tableColumn`: A table column in the outline view.
- `item`: An item in the outline view.

## See Also

### Displaying Cells
- [func outlineView(NSOutlineView, willDisplayCell: Any, for: NSTableColumn?, item: Any)](./outlineview%28_,willdisplaycell,for,item%29.md)
  Informs the delegate that the cell specified by the column and item will be displayed.
- [func outlineView(NSOutlineView, willDisplayOutlineCell: Any, for: NSTableColumn?, item: Any)](./outlineview%28_,willdisplayoutlinecell,for,item%29.md)
  Informs the delegate that an outline view is about to display a cell used to draw the expansion symbol.
- [func outlineView(NSOutlineView, dataCellFor: NSTableColumn?, item: Any) -> NSCell?](./outlineview%28_,datacellfor,item%29.md)
  Returns the cell to use in a given column for a given item.
- [func outlineView(NSOutlineView, shouldShowOutlineCellForItem: Any) -> Bool](./outlineview%28_,shouldshowoutlinecellforitem%29.md)
  Returns whether the specified item should display the outline cell (the disclosure triangle).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsoutlineviewdelegate/outlineview(_:shouldshowcellexpansionfor:item:))*