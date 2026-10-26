# gridColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color used to draw grid lines.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var gridColor: NSColor { get set }
```

```objc
@property (copy) NSColor * gridColor;
```

#### Discussion

The default color is gray.

## See Also

### Related Documentation
- [func drawGrid(inClipRect: NSRect)](./drawgrid%28incliprect%29.md)
  Draws the grid lines within the supplied rectangle.
- [- drawsGrid](./drawsgrid.md)
  Returns a Boolean value that indicates whether the table view draws a grid.
### Setting Display Attributes
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var rowHeight: CGFloat](./rowheight.md)
  The height of each row in the table.
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
- [var gridStyleMask: NSTableView.GridLineStyle](./gridstylemask.md)
  The grid lines drawn by the table view.
- [func indicatorImage(in: NSTableColumn) -> NSImage?](./indicatorimage%28in%29.md)
  Returns the indicator image of the specified table column.
- [func setIndicatorImage(NSImage?, in: NSTableColumn)](./setindicatorimage%28_,in%29.md)
  Sets the indicator image of the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/gridcolor)*