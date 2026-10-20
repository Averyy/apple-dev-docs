# drawBackground(inClipRect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the background of the table view in the clip rect specified by the rectangle.

**Availability**:
- macOS

## Declaration

```swift
func drawBackground(inClipRect clipRect: NSRect)
```

```objc
- (void) drawBackgroundInClipRect:(NSRect) clipRect;
```

## Parameters

- `clipRect`: The rectangle, in the table view’s coordinate system.

## See Also

### Drawing
- [func drawRow(Int, clipRect: NSRect)](./drawrow%28_,cliprect%29.md)
  Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.
- [func drawGrid(inClipRect: NSRect)](./drawgrid%28incliprect%29.md)
  Draws the grid lines within the supplied rectangle.
- [func highlightSelection(inClipRect: NSRect)](./highlightselection%28incliprect%29.md)
  Highlights the region of the table view in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/drawbackground(incliprect:))*