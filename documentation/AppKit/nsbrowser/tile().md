# tile()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adjusts the various subviews of the browser—scrollers, columns, titles, and so on—without redrawing.

**Availability**:
- macOS

## Declaration

```swift
func tile()
```

```objc
- (void) tile;
```

#### Discussion

Your code shouldn’t send this message. It’s invoked any time the appearance of the browser changes.

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
- [var delegate: (any NSBrowserDelegate)?](./delegate.md)
  The browser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/tile())*