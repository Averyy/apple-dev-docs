# NSTableView.Style

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Contains the possible style values for a table view.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum Style
```

```c
enum NSTableViewStyle : NSInteger;
```

## Topics

### Table Styles
- [NSTableView.Style.automatic](./style-swift.enum/automatic.md)
  The system resolves the table view style based on the table view hierarchy.
- [NSTableView.Style.fullWidth](./style-swift.enum/fullwidth.md)
  The table view style resolves to a full-width style.
- [NSTableView.Style.inset](./style-swift.enum/inset.md)
  The table view style resolves to an inset style.
- [NSTableView.Style.sourceList](./style-swift.enum/sourcelist.md)
  The table view style resolves to a source-list style.
- [NSTableView.Style.plain](./style-swift.enum/plain.md)
  The table view style resolves to a plain style.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/style-swift.enum)*