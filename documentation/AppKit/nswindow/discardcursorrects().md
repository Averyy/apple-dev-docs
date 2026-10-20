# discardCursorRects()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates all cursor rectangles in the window.

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

This method is invoked by [`resetCursorRects()`](./resetcursorrects%28%29.md) to clear out existing cursor rectangles before resetting them. You shouldn’t invoke it in the code you write, but you might want to override it to change its behavior.

## See Also

### Managing Cursor Rectangles
- [var areCursorRectsEnabled: Bool](./arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](./enablecursorrects%28%29.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](./disablecursorrects%28%29.md) message.
- [func disableCursorRects()](./disablecursorrects%28%29.md)
  Disables all cursor rectangle management within the window.
- [func invalidateCursorRects(for: NSView)](./invalidatecursorrects%28for%29.md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.
- [func resetCursorRects()](./resetcursorrects%28%29.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](../nsview.md) objects in its view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/discardcursorrects())*