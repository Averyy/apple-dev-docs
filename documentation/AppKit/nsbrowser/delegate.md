# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The browser’s delegate.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSBrowserDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSBrowserDelegate> delegate;
```

## See Also

### Configuring Browsers
- [var reusesColumns: Bool](./reusescolumns.md)
  A Boolean that indicates whether the browser reuses matrix objects after their columns are unloaded.
- [var maxVisibleColumns: Int](./maxvisiblecolumns.md)
  The maximum number of visible columns.
- [var autohidesScroller: Bool](./autohidesscroller.md)
  A Boolean that indicates whether the browser automatically hides its scroller.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/delegate)*