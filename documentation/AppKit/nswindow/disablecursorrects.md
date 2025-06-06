# disableCursorRects()

**Framework**: AppKit  
**Kind**: method

Disables all cursor rectangle management within the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func disableCursorRects()
```

#### Discussion

Use this method when you need to do some special cursor manipulation and you don’t want the Application Kit interfering.

## See Also

- [var areCursorRectsEnabled: Bool](nswindow/arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](nswindow/enablecursorrects.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](nswindow/disablecursorrects().md) message.
- [func discardCursorRects()](nswindow/discardcursorrects.md)
  Invalidates all cursor rectangles in the window.
- [func invalidateCursorRects(for: NSView)](nswindow/invalidatecursorrects(for:).md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.
- [func resetCursorRects()](nswindow/resetcursorrects.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](nsview.md) objects in its view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/disablecursorrects())*