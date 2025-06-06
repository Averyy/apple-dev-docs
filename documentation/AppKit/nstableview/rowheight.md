# rowHeight

**Framework**: AppKit  
**Kind**: property

The height of each row in the table.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var rowHeight: CGFloat { get set }
```

#### Discussion

The default row height is `16.0`. The value in this property is used only if the table’s [`rowSizeStyle`](nstableview/rowsizestyle-swift.property.md) is set to [`NSTableView.RowSizeStyle.custom`](nstableview/rowsizestyle-swift.enum/custom.md).

When you change the value of this property, the table view calls the [`tile()`](nstableview/tile().md) method to redisplay the rows using the new value.

## See Also

- [var rowSizeStyle: NSTableView.RowSizeStyle](nstableview/rowsizestyle-swift.property.md)
  The row size style (small, medium, large, or custom) used by the table view.
- [var intercellSpacing: NSSize](nstableview/intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var backgroundColor: NSColor](nstableview/backgroundcolor.md)
  The color used to draw the background of the table.
- [var usesAlternatingRowBackgroundColors: Bool](nstableview/usesalternatingrowbackgroundcolors.md)
  A Boolean value indicating whether the table view uses alternating row colors for its background.
- [var style: NSTableView.Style](nstableview/style-swift.property.md)
  The style that the table view uses.
- [var effectiveStyle: NSTableView.Style](nstableview/effectivestyle.md)
  The effective style that the table uses.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/rowheight)*