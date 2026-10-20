# discardCursorRects()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](./addcursorrect%28_,cursor%29.md).

**Availability**:
- macOS

## Declaration

```swift
func discardCursorRects()
```

```objc
- (void) discardCursorRects;
```

#### Discussion

You need never invoke this method directly; neither is it typically invoked during the invalidation of cursor rectangles.  [`NSWindow`](../nswindow.md) automatically invalidates cursor rectangles in response to [`invalidateCursorRects(for:)`](../nswindow/invalidatecursorrects%28for%29.md) and before the view’s cursor rectangles are reestablished using [`resetCursorRects()`](./resetcursorrects%28%29.md).  This method is invoked just before the view is removed from a window and when the view is deallocated.

## See Also

### Related Documentation
- [func discardCursorRects()](../nswindow/discardcursorrects%28%29.md)
  Invalidates all cursor rectangles in the window.
### Responding to Cursor Movements
- [func addCursorRect(NSRect, cursor: NSCursor)](./addcursorrect%28_,cursor%29.md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func removeCursorRect(NSRect, cursor: NSCursor)](./removecursorrect%28_,cursor%29.md)
  Completely removes a cursor rectangle from the view.
- [func resetCursorRects()](./resetcursorrects%28%29.md)
  Overridden by subclasses to define their default cursor rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/discardcursorrects())*