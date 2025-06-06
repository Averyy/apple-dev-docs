# maxVisibleColumns

**Framework**: AppKit  
**Kind**: property

The maximum number of visible columns.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var maxVisibleColumns: Int { get set }
```

## See Also

- [var reusesColumns: Bool](nsbrowser/reusescolumns.md)
  A Boolean that indicates whether the browser reuses matrix objects after their columns are unloaded.
- [var autohidesScroller: Bool](nsbrowser/autohidesscroller.md)
  A Boolean that indicates whether the browser automatically hides its scroller.
- [var backgroundColor: NSColor](nsbrowser/backgroundcolor.md)
  The browser’s background color.
- [var minColumnWidth: CGFloat](nsbrowser/mincolumnwidth.md)
  The minimum column width, in pixels.
- [var separatesColumns: Bool](nsbrowser/separatescolumns.md)
  A Boolean that indicates whether columns are separated by bezeled borders.
- [var takesTitleFromPreviousColumn: Bool](nsbrowser/takestitlefrompreviouscolumn.md)
  A Boolean that indicates whether a column takes its title from the selected cell in the previous column.
- [func tile()](nsbrowser/tile.md)
  Adjusts the various subviews of the browser—scrollers, columns, titles, and so on—without redrawing.
- [var delegate: (any NSBrowserDelegate)?](nsbrowser/delegate.md)
  The browser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/maxvisiblecolumns)*