# drawRow(_:clipRect:)

**Framework**: AppKit  
**Kind**: method

Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawRow(_ row: Int, clipRect: NSRect)
```

#### Discussion

[`NSCell`](nscell.md)-based table views can override this method to customize the drawing of the rows.

> **Note**:  For [`NSView`](nsview.md)-based table views, do not subclass or override this method. Instead, row drawing customization should be done by subclassing [`NSTableRowView`](nstablerowview.md).

 For [`NSView`](nsview.md)-based table views, do not subclass or override this method. Instead, row drawing customization should be done by subclassing [`NSTableRowView`](nstablerowview.md).

## Parameters

- `row`: The row index.
- `clipRect`: The intersecting rectangle.

## See Also

- [func drawGrid(inClipRect: NSRect)](nstableview/drawgrid(incliprect:).md)
  Draws the grid lines within the supplied rectangle.
- [func highlightSelection(inClipRect: NSRect)](nstableview/highlightselection(incliprect:).md)
  Highlights the region of the table view in the specified rectangle.
- [func drawBackground(inClipRect: NSRect)](nstableview/drawbackground(incliprect:).md)
  Draws the background of the table view in the clip rect specified by the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/drawrow(_:cliprect:))*