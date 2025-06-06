# drawBackground(inClipRect:)

**Framework**: AppKit  
**Kind**: method

Draws the background of the table view in the clip rect specified by the rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawBackground(inClipRect clipRect: NSRect)
```

## Parameters

- `clipRect`: The rectangle, in the table view’s coordinate system.

## See Also

- [func drawRow(Int, clipRect: NSRect)](nstableview/drawrow(_:cliprect:).md)
  Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.
- [func drawGrid(inClipRect: NSRect)](nstableview/drawgrid(incliprect:).md)
  Draws the grid lines within the supplied rectangle.
- [func highlightSelection(inClipRect: NSRect)](nstableview/highlightselection(incliprect:).md)
  Highlights the region of the table view in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/drawbackground(incliprect:))*