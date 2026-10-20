# setIndicatorImage(_:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the indicator image of the specified column.

**Availability**:
- macOS

## Declaration

```swift
func setIndicatorImage(_ image: NSImage?, in tableColumn: NSTableColumn)
```

```objc
- (void) setIndicatorImage:(NSImage *) image inTableColumn:(NSTableColumn *) tableColumn;
```

#### Discussion

The default sorting order indicators are available as named `NSImage` objects. These images are accessed using `[NSImage imageNamed:]` passing either `@"NSAscendingSortIndicator"` (the “^” icon), and `@"NSDescendingSortIndicator"` (the “v” icon).

## Parameters

- `image`: The indicator image for the column.
- `tableColumn`: The table column.

## See Also

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
- [var gridColor: NSColor](./gridcolor.md)
  The color used to draw grid lines.
- [var gridStyleMask: NSTableView.GridLineStyle](./gridstylemask.md)
  The grid lines drawn by the table view.
- [func indicatorImage(in: NSTableColumn) -> NSImage?](./indicatorimage%28in%29.md)
  Returns the indicator image of the specified table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/setindicatorimage(_:in:))*