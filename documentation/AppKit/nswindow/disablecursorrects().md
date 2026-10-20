# disableCursorRects()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Disables all cursor rectangle management within the window.

**Availability**:
- macOS

## Declaration

```swift
func disableCursorRects()
```

```objc
- (void) disableCursorRects;
```

#### Discussion

Use this method when you need to do some special cursor manipulation and you don’t want the Application Kit interfering.

## See Also

### Managing Cursor Rectangles
- [var areCursorRectsEnabled: Bool](./arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](./enablecursorrects%28%29.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](./disablecursorrects%28%29.md) message.
- [func discardCursorRects()](./discardcursorrects%28%29.md)
  Invalidates all cursor rectangles in the window.
- [func invalidateCursorRects(for: NSView)](./invalidatecursorrects%28for%29.md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.
- [func resetCursorRects()](./resetcursorrects%28%29.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](../nsview.md) objects in its view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/disablecursorrects())*