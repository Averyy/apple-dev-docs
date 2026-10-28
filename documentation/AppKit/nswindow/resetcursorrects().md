# resetCursorRects()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](../nsview.md) objects in its view hierarchy.

**Availability**:
- macOS

## Declaration

```swift
func resetCursorRects()
```

```objc
- (void) resetCursorRects;
```

## Discussion

Invokes [`discardCursorRects()`](./discardcursorrects%28%29.md) to clear the window’s cursor rectangles, then sends [`resetCursorRects()`](./resetcursorrects%28%29.md) to every `NSView` object in the window’s view hierarchy.

This method is typically invoked by the NSApplication object when it detects that the key window’s cursor rectangles are invalid. In program code, it’s more efficient to invoke [`invalidateCursorRects(for:)`](./invalidatecursorrects%28for%29.md).

## See Also

### Managing Cursor Rectangles
- [var areCursorRectsEnabled: Bool](./arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](./enablecursorrects%28%29.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](./disablecursorrects%28%29.md) message.
- [func disableCursorRects()](./disablecursorrects%28%29.md)
  Disables all cursor rectangle management within the window.
- [func discardCursorRects()](./discardcursorrects%28%29.md)
  Invalidates all cursor rectangles in the window.
- [func invalidateCursorRects(for: NSView)](./invalidatecursorrects%28for%29.md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/resetcursorrects())*