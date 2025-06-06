# invalidateCursorRects(for:)

**Framework**: AppKit  
**Kind**: method

Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func invalidateCursorRects(for view: NSView)
```

#### Discussion

If the window is current the key window, window resets the cursor rectangles immediately.

## Parameters

- `view`: The view in the window’s view hierarchy.

## See Also

- [func resetCursorRects()](nsview/resetcursorrects.md)
  Overridden by subclasses to define their default cursor rectangles.
- [var areCursorRectsEnabled: Bool](nswindow/arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](nswindow/enablecursorrects.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](nswindow/disablecursorrects().md) message.
- [func disableCursorRects()](nswindow/disablecursorrects.md)
  Disables all cursor rectangle management within the window.
- [func discardCursorRects()](nswindow/discardcursorrects.md)
  Invalidates all cursor rectangles in the window.
- [func resetCursorRects()](nswindow/resetcursorrects.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](nsview.md) objects in its view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/invalidatecursorrects(for:))*