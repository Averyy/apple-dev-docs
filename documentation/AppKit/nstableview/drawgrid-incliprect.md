# drawGrid(inClipRect:)

**Framework**: AppKit  
**Kind**: method

Draws the grid lines within the supplied rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawGrid(inClipRect clipRect: NSRect)
```

#### Discussion

Draws the grid lines within `clipRect`, using the grid color set with [`gridColor`](nstableview/gridcolor.md).

Subclasses can override this method to draw grid lines other than the standard ones. This method draws a grid regardless of whether the table view is set to draw one automatically.

## Parameters

- `clipRect`: The rectangle in the table view’s coordinate system.

## See Also

- [var intercellSpacing: NSSize](nstableview/intercellspacing.md)
  The horizontal and vertical spacing between cells.
- [var gridColor: NSColor](nstableview/gridcolor.md)
  The color used to draw grid lines.
- [func drawRow(Int, clipRect: NSRect)](nstableview/drawrow(_:cliprect:).md)
  Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.
- [func highlightSelection(inClipRect: NSRect)](nstableview/highlightselection(incliprect:).md)
  Highlights the region of the table view in the specified rectangle.
- [func drawBackground(inClipRect: NSRect)](nstableview/drawbackground(incliprect:).md)
  Draws the background of the table view in the clip rect specified by the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/drawgrid(incliprect:))*