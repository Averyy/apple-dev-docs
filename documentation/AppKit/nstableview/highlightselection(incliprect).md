# highlightSelection(inClipRect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Highlights the region of the table view in the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func highlightSelection(inClipRect clipRect: NSRect)
```

```objc
- (void) highlightSelectionInClipRect:(NSRect) clipRect;
```

#### Discussion

This method is invoked before [`drawRow(_:clipRect:)`](./drawrow%28_,cliprect%29.md).

[`NSCell`](../nscell.md)-based table views can override this method to change the manner in which they highlight selections.

> **Note**:  This method should not be subclassed or overridden for a view-base table view. Instead, row drawing customization should be done by subclassing [`NSTableRowView`](../nstablerowview.md).

## Parameters

- `clipRect`: The rectangle, in the table view view’s coordinate system.

## See Also

### Drawing
- [func drawRow(Int, clipRect: NSRect)](./drawrow%28_,cliprect%29.md)
  Draws the cells for the row at `rowIndex` in the columns that intersect `clipRect`.
- [func drawGrid(inClipRect: NSRect)](./drawgrid%28incliprect%29.md)
  Draws the grid lines within the supplied rectangle.
- [func drawBackground(inClipRect: NSRect)](./drawbackground%28incliprect%29.md)
  Draws the background of the table view in the clip rect specified by the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/highlightselection(incliprect:))*