# usesAlternatingRowBackgroundColors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the table view uses alternating row colors for its background.

**Availability**:
- macOS

## Declaration

```swift
var usesAlternatingRowBackgroundColors: Bool { get set }
```

```objc
@property BOOL usesAlternatingRowBackgroundColors;
```

## Return Value

[`true`](../../Swift/true.md) if the table view uses standard alternating row colors for the background, [`false`](../../Swift/false.md) if it uses a solid color.

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the table uses the standard alternating row colors for the background. When the value is [`false`](../../Swift/false.md), the table view uses a single solid color for the background.

## See Also

### Setting Display Attributes
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var rowHeight: CGFloat](./rowheight.md)
  The height of each row in the table.
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The color used to draw the background of the table.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/usesalternatingrowbackgroundcolors)*