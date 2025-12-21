# takesTitleFromPreviousColumn

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether a column takes its title from the selected cell in the previous column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var takesTitleFromPreviousColumn: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the title of a column is set to the string value of the selected `NSCell` in the previous column.

## See Also

- [var reusesColumns: Bool](nsbrowser/reusescolumns.md)
  A Boolean that indicates whether the browser reuses matrix objects after their columns are unloaded.
- [var maxVisibleColumns: Int](nsbrowser/maxvisiblecolumns.md)
  The maximum number of visible columns.
- [var autohidesScroller: Bool](nsbrowser/autohidesscroller.md)
  A Boolean that indicates whether the browser automatically hides its scroller.
- [var backgroundColor: NSColor](nsbrowser/backgroundcolor.md)
  The browser’s background color.
- [var minColumnWidth: CGFloat](nsbrowser/mincolumnwidth.md)
  The minimum column width, in pixels.
- [var separatesColumns: Bool](nsbrowser/separatescolumns.md)
  A Boolean that indicates whether columns are separated by bezeled borders.
- [func tile()](nsbrowser/tile.md)
  Adjusts the various subviews of the browser—scrollers, columns, titles, and so on—without redrawing.
- [var delegate: (any NSBrowserDelegate)?](nsbrowser/delegate.md)
  The browser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/takestitlefrompreviouscolumn)*