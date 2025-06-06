# usesAlternatingRowBackgroundColors

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the table view uses alternating row colors for its background.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesAlternatingRowBackgroundColors: Bool { get set }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the table view uses standard alternating row colors for the background, [`false`](https://developer.apple.com/documentation/swift/false) if it uses a solid color.

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the table uses the standard alternating row colors for the background. When the value is [`false`](https://developer.apple.com/documentation/swift/false), the table view uses a single solid color for the background.

## See Also

- [var intercellSpacing: NSSize](nstableview/intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var rowHeight: CGFloat](nstableview/rowheight.md)
  The height of each row in the table.
- [var backgroundColor: NSColor](nstableview/backgroundcolor.md)
  The color used to draw the background of the table.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/usesalternatingrowbackgroundcolors)*