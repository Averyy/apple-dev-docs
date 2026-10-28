# takesTitleFromPreviousColumn

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether a column takes its title from the selected cell in the previous column.

**Availability**:
- macOS

## Declaration

```swift
var takesTitleFromPreviousColumn: Bool { get set }
```

```objc
@property BOOL takesTitleFromPreviousColumn;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the title of a column is set to the string value of the selected `NSCell` in the previous column.

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
- [func tile()](./tile%28%29.md)
  Adjusts the various subviews of the browser—scrollers, columns, titles, and so on—without redrawing.
- [var delegate: (any NSBrowserDelegate)?](./delegate.md)
  The browser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/takestitlefrompreviouscolumn)*