# gridStyleMask

**Framework**: AppKit  
**Kind**: property

The grid lines drawn by the table view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var gridStyleMask: NSTableView.GridLineStyle { get set }
```

#### Discussion

Use this property to specify whether lines should be drawn between rows and columns. When setting this property, you can specify multiple styles at once by adding the corresponding constants together. The default value of this property is [`NSTableViewGridNone`](nstableviewgridlinestyle/nstableviewgridnone.md).

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
- [var effectiveStyle: NSTableView.Style](nstableview/effectivestyle.md)
  The effective style that the table uses.
- [NSTableView.Style](nstableview/style-swift.enum.md)
  Contains the possible style values for a table view.
- [var selectionHighlightStyle: NSTableView.SelectionHighlightStyle](nstableview/selectionhighlightstyle-swift.property.md)
  The selection highlight style used by the table view to indicate row and column selection.
- [var gridColor: NSColor](nstableview/gridcolor.md)
  The color used to draw grid lines.
- [func indicatorImage(in: NSTableColumn) -> NSImage?](nstableview/indicatorimage(in:).md)
  Returns the indicator image of the specified table column.
- [func setIndicatorImage(NSImage?, in: NSTableColumn)](nstableview/setindicatorimage(_:in:).md)
  Sets the indicator image of the specified column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/gridstylemask)*