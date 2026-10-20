# drawGrid(inClipRect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the grid lines within the supplied rectangle.

**Availability**:
- macOS

## Declaration

```swift
func drawGrid(inClipRect clipRect: NSRect)
```

```objc
- (void) drawGridInClipRect:(NSRect) clipRect;
```

#### Discussion

Draws the grid lines within `clipRect`, using the grid color set with [`gridColor`](./gridcolor.md).

Subclasses can override this method to draw grid lines other than the standard ones. This method draws a grid regardless of whether the table view is set to draw one automatically.

## Parameters

- `clipRect`: The rectangle in the table view’s coordinate system.

## See Also

### Related Documentation
- [var intercellSpacing: NSSize](./intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var gridColor: NSColor](./gridcolor.md)
  The color used to draw grid lines.
### Drawing
- [func drawRow(Int, clipRect: NSRect)](./drawrow%28_,cliprect%29.md)
  Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.
- [func highlightSelection(inClipRect: NSRect)](./highlightselection%28incliprect%29.md)
  Highlights the region of the table view in the specified rectangle.
- [func drawBackground(inClipRect: NSRect)](./drawbackground%28incliprect%29.md)
  Draws the background of the table view in the clip rect specified by the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/drawgrid(incliprect:))*