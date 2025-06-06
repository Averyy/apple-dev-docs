# discardCursorRects()

**Framework**: AppKit  
**Kind**: method

Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](nsview/addcursorrect(_:cursor:).md).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func discardCursorRects()
```

#### Discussion

You need never invoke this method directly; neither is it typically invoked during the invalidation of cursor rectangles.  [`NSWindow`](nswindow.md) automatically invalidates cursor rectangles in response to [`invalidateCursorRects(for:)`](nswindow/invalidatecursorrects(for:).md) and before the view’s cursor rectangles are reestablished using [`resetCursorRects()`](nsview/resetcursorrects().md).  This method is invoked just before the view is removed from a window and when the view is deallocated.

## See Also

- [func discardCursorRects()](nswindow/discardcursorrects.md)
  Invalidates all cursor rectangles in the window.
- [func addCursorRect(NSRect, cursor: NSCursor)](nsview/addcursorrect(_:cursor:).md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func removeCursorRect(NSRect, cursor: NSCursor)](nsview/removecursorrect(_:cursor:).md)
  Completely removes a cursor rectangle from the view.
- [func resetCursorRects()](nsview/resetcursorrects.md)
  Overridden by subclasses to define their default cursor rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/discardcursorrects())*