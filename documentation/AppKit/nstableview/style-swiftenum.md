# NSTableView.Style

**Framework**: AppKit  
**Kind**: enum

Contains the possible style values for a table view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum Style
```

## Topics

### Table Styles
- [NSTableView.Style.automatic](nstableview/style-swift.enum/automatic.md)
  The system resolves the table view style based on the table view hierarchy.
- [NSTableView.Style.fullWidth](nstableview/style-swift.enum/fullwidth.md)
  The table view style resolves to a full-width style.
- [NSTableView.Style.inset](nstableview/style-swift.enum/inset.md)
  The table view style resolves to an inset style.
- [NSTableView.Style.sourceList](nstableview/style-swift.enum/sourcelist.md)
  The table view style resolves to a source-list style.
- [NSTableView.Style.plain](nstableview/style-swift.enum/plain.md)
  The table view style resolves to a plain style.
### Initializers
- [init?(rawValue: Int)](nstableview/style-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/style-swift.enum)*