# autohidesScroller

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the browser automatically hides its scroller.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var autohidesScroller: Bool { get set }
```

```objc
@property BOOL autohidesScroller;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the scroller is automatically hidden.

## See Also

### Configuring Browsers
- [var reusesColumns: Bool](./reusescolumns.md)
  A Boolean that indicates whether the browser reuses matrix objects after their columns are unloaded.
- [var maxVisibleColumns: Int](./maxvisiblecolumns.md)
  The maximum number of visible columns.
- [var backgroundColor: NSColor](./backgroundcolor.md)
  The browser’s background color.
- [var minColumnWidth: CGFloat](./mincolumnwidth.md)
  The minimum column width, in pixels.
- [var separatesColumns: Bool](./separatescolumns.md)
  A Boolean that indicates whether columns are separated by bezeled borders.
- [var takesTitleFromPreviousColumn: Bool](./takestitlefrompreviouscolumn.md)
  A Boolean that indicates whether a column takes its title from the selected cell in the previous column.
- [func tile()](./tile%28%29.md)
  Adjusts the various subviews of the browser—scrollers, columns, titles, and so on—without redrawing.
- [var delegate: (any NSBrowserDelegate)?](./delegate.md)
  The browser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/autohidesscroller)*