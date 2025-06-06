# resetCursorRects()

**Framework**: AppKit  
**Kind**: method

Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](nsview.md) objects in its view hierarchy.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resetCursorRects()
```

#### Discussion

Invokes [`discardCursorRects()`](nswindow/discardcursorrects().md) to clear the window’s cursor rectangles, then sends [`resetCursorRects()`](nswindow/resetcursorrects().md) to every `NSView` object in the window’s view hierarchy.

This method is typically invoked by the NSApplication object when it detects that the key window’s cursor rectangles are invalid. In program code, it’s more efficient to invoke [`invalidateCursorRects(for:)`](nswindow/invalidatecursorrects(for:).md).

## See Also

- [var areCursorRectsEnabled: Bool](nswindow/arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](nswindow/enablecursorrects.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](nswindow/disablecursorrects().md) message.
- [func disableCursorRects()](nswindow/disablecursorrects.md)
  Disables all cursor rectangle management within the window.
- [func discardCursorRects()](nswindow/discardcursorrects.md)
  Invalidates all cursor rectangles in the window.
- [func invalidateCursorRects(for: NSView)](nswindow/invalidatecursorrects(for:).md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/resetcursorrects())*