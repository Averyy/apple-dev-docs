# invalidateCursorRects(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.

**Availability**:
- macOS

## Declaration

```swift
func invalidateCursorRects(for view: NSView)
```

```objc
- (void) invalidateCursorRectsForView:(NSView *) view;
```

## Discussion

If the window is current the key window, window resets the cursor rectangles immediately.

## Parameters

- `view`: The view in the window’s view hierarchy.

## See Also

### Related Documentation
- [func resetCursorRects()](../nsview/resetcursorrects%28%29.md)
  Overridden by subclasses to define their default cursor rectangles.
### Managing Cursor Rectangles
- [var areCursorRectsEnabled: Bool](./arecursorrectsenabled.md)
  A Boolean value that indicates whether the window’s cursor rectangles are enabled.
- [func enableCursorRects()](./enablecursorrects%28%29.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](./disablecursorrects%28%29.md) message.
- [func disableCursorRects()](./disablecursorrects%28%29.md)
  Disables all cursor rectangle management within the window.
- [func discardCursorRects()](./discardcursorrects%28%29.md)
  Invalidates all cursor rectangles in the window.
- [func resetCursorRects()](./resetcursorrects%28%29.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](../nsview.md) objects in its view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/invalidatecursorrects(for:))*