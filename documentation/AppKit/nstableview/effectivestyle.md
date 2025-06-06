# effectiveStyle

**Framework**: AppKit  
**Kind**: property

The effective style that the table uses.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
var effectiveStyle: NSTableView.Style { get }
```

#### Discussion

If the [`style`](nstableview/style-swift.property.md) property value is [`NSTableView.Style.automatic`](nstableview/style-swift.enum/automatic.md), then this property contains the resolved style.

## See Also

- [var intercellSpacing: NSSize](nstableview/intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var rowHeight: CGFloat](nstableview/rowheight.md)
  The height of each row in the table.
- [var backgroundColor: NSColor](nstableview/backgroundcolor.md)
  The color used to draw the background of the table.
- [var usesAlternatingRowBackgroundColors: Bool](nstableview/usesalternatingrowbackgroundcolors.md)
  A Boolean value indicating whether the table view uses alternating row colors for its background.
- [var style: NSTableView.Style](nstableview/style-swift.property.md)
  The style that the table view uses.
- [NSTableView.Style](nstableview/style-swift.enum.md)
  Contains the possible style values for a table view.
- [var selectionHighlightStyle: NSTableView.SelectionHighlightStyle](nstableview/selectionhighlightstyle-swift.property.md)
  The selection highlight style used by the table view to indicate row and column selection.
- [var gridColor: NSColor](nstableview/gridcolor.md)
  The color used to draw grid lines.
- [var gridStyleMask: NSTableView.GridLineStyle](nstableview/gridstylemask.md)
  The grid lines drawn by the table view.
- [func indicatorImage(in: NSTableColumn) -> NSImage?](nstableview/indicatorimage(in:).md)
  Returns the indicator image of the specified table column.
- [func setIndicatorImage(NSImage?, in: NSTableColumn)](nstableview/setindicatorimage(_:in:).md)
  Sets the indicator image of the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/effectivestyle)*