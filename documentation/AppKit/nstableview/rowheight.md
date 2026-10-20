# rowHeight

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The height of each row in the table.

**Availability**:
- macOS

## Declaration

```swift
var rowHeight: CGFloat { get set }
```

```objc
@property CGFloat rowHeight;
```

#### Discussion

The default row height is `16.0`. The value in this property is used only if the table’s [`rowSizeStyle`](./rowsizestyle-swift.property.md) is set to [`NSTableView.RowSizeStyle.custom`](./rowsizestyle-swift.enum/custom.md).

When you change the value of this property, the table view calls the [`tile()`](./tile%28%29.md) method to redisplay the rows using the new value.

## See Also

### Related Documentation
- [var rowSizeStyle: NSTableView.RowSizeStyle](./rowsizestyle-swift.property.md)
  The row size style (small, medium, large, or custom) used by the table view.
### Setting Display Attributes
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The color used to draw the background of the table.
- [var usesAlternatingRowBackgroundColors: Bool](./usesalternatingrowbackgroundcolors.md)
  A Boolean value indicating whether the table view uses alternating row colors for its background.
- [var style: NSTableView.Style](./style-swift.property.md)
  The style that the table view uses.
- [var effectiveStyle: NSTableView.Style](./effectivestyle.md)
  The effective style that the table uses.
- [NSTableView.Style](./style-swift.enum.md)
  Contains the possible style values for a table view.
- [var selectionHighlightStyle: NSTableView.SelectionHighlightStyle](./selectionhighlightstyle-swift.property.md)
  The selection highlight style used by the table view to indicate row and column selection.
- [var gridColor: NSColor](./gridcolor.md)
  The color used to draw grid lines.
- [var gridStyleMask: NSTableView.GridLineStyle](./gridstylemask.md)
  The grid lines drawn by the table view.
- [func indicatorImage(in: NSTableColumn) -> NSImage?](./indicatorimage%28in%29.md)
  Returns the indicator image of the specified table column.
- [func setIndicatorImage(NSImage?, in: NSTableColumn)](./setindicatorimage%28_,in%29.md)
  Sets the indicator image of the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowheight)*