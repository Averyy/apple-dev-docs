# reusesColumns

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the browser reuses matrix objects after their columns are unloaded.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var reusesColumns: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the `NSMatrix` objects aren’t freed when their columns are unloaded, so they can be reused.

## See Also

- [Browser Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Browser/Browser.html#//apple_ref/doc/uid/10000018i)
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
- [var takesTitleFromPreviousColumn: Bool](nsbrowser/takestitlefrompreviouscolumn.md)
  A Boolean that indicates whether a column takes its title from the selected cell in the previous column.
- [func tile()](nsbrowser/tile.md)
  Adjusts the various subviews of the browser—scrollers, columns, titles, and so on—without redrawing.
- [var delegate: (any NSBrowserDelegate)?](nsbrowser/delegate.md)
  The browser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/reusescolumns)*