# highlightSelection(inClipRect:)

**Framework**: AppKit  
**Kind**: method

Highlights the region of the table view in the specified rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func highlightSelection(inClipRect clipRect: NSRect)
```

#### Discussion

This method is invoked before [`drawRow(_:clipRect:)`](nstableview/drawrow(_:cliprect:).md).

[`NSCell`](nscell.md)-based table views can override this method to change the manner in which they highlight selections.

> **Note**:  This method should not be subclassed or overridden for a view-base table view. Instead, row drawing customization should be done by subclassing [`NSTableRowView`](nstablerowview.md).

## Parameters

- `clipRect`: The rectangle, in the table view view’s coordinate system.

## See Also

- [func drawRow(Int, clipRect: NSRect)](nstableview/drawrow(_:cliprect:).md)
  Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.
- [func drawGrid(inClipRect: NSRect)](nstableview/drawgrid(incliprect:).md)
  Draws the grid lines within the supplied rectangle.
- [func drawBackground(inClipRect: NSRect)](nstableview/drawbackground(incliprect:).md)
  Draws the background of the table view in the clip rect specified by the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/highlightselection(incliprect:))*