# drawRow(_:clipRect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.

**Availability**:
- macOS

## Declaration

```swift
func drawRow(_ row: Int, clipRect: NSRect)
```

```objc
- (void) drawRow:(NSInteger) row clipRect:(NSRect) clipRect;
```

## Discussion

[`NSCell`](../nscell.md)-based table views can override this method to customize the drawing of the rows.

> **Note**:  For [`NSView`](../nsview.md)-based table views, do not subclass or override this method. Instead, row drawing customization should be done by subclassing [`NSTableRowView`](../nstablerowview.md).

## Parameters

- `row`: The row index.
- `clipRect`: The intersecting rectangle.

## See Also

### Drawing
- [func drawGrid(inClipRect: NSRect)](./drawgrid%28incliprect%29.md)
  Draws the grid lines within the supplied rectangle.
- [func highlightSelection(inClipRect: NSRect)](./highlightselection%28incliprect%29.md)
  Highlights the region of the table view in the specified rectangle.
- [func drawBackground(inClipRect: NSRect)](./drawbackground%28incliprect%29.md)
  Draws the background of the table view in the clip rect specified by the rectangle.
### Related Documentation
- [- columnsInRect:](./columnsinrect_.md)
  Returns a range of indexes for the table view’s columns that lie wholly or partially within the horizontal boundaries of the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/drawrow(_:cliprect:))*