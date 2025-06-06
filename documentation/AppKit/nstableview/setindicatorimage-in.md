# setIndicatorImage(_:in:)

**Framework**: AppKit  
**Kind**: method

Sets the indicator image of the specified column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setIndicatorImage(_ image: NSImage?, in tableColumn: NSTableColumn)
```

#### Discussion

The default sorting order indicators are available as named `NSImage` objects. These images are accessed using `[NSImage imageNamed:]` passing either `@"NSAscendingSortIndicator"` (the “^” icon), and `@"NSDescendingSortIndicator"` (the “v” icon).

## Parameters

- `image`: The indicator image for the column.
- `tableColumn`: The table column.

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
- [var gridStyleMask: NSTableView.GridLineStyle](nstableview/gridstylemask.md)
  The grid lines drawn by the table view.
- [func indicatorImage(in: NSTableColumn) -> NSImage?](nstableview/indicatorimage(in:).md)
  Returns the indicator image of the specified table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/setindicatorimage(_:in:))*