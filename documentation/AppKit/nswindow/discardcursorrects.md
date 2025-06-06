# discardCursorRects()

**Framework**: AppKit  
**Kind**: method

Invalidates all cursor rectangles in the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func discardCursorRects()
```

#### Discussion

This method is invoked by [`resetCursorRects()`](nswindow/resetcursorrects().md) to clear out existing cursor rectangles before resetting them. You shouldn’t invoke it in the code you write, but you might want to override it to change its behavior.

## See Also

- [var areCursorRectsEnabled: Bool](nswindow/arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](nswindow/enablecursorrects.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](nswindow/disablecursorrects().md) message.
- [func disableCursorRects()](nswindow/disablecursorrects.md)
  Disables all cursor rectangle management within the window.
- [func invalidateCursorRects(for: NSView)](nswindow/invalidatecursorrects(for:).md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.
- [func resetCursorRects()](nswindow/resetcursorrects.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](nsview.md) objects in its view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/discardcursorrects())*