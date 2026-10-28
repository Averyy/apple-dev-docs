# areCursorRectsEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window’s cursor rectangles are enabled.

**Availability**:
- macOS

## Declaration

```swift
var areCursorRectsEnabled: Bool { get }
```

```objc
@property (readonly) BOOL areCursorRectsEnabled;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when cursor rectangles are enabled; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [func addCursorRect(NSRect, cursor: NSCursor)](../nsview/addcursorrect%28_,cursor%29.md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
### Managing Cursor Rectangles
- [func enableCursorRects()](./enablecursorrects%28%29.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](./disablecursorrects%28%29.md) message.
- [func disableCursorRects()](./disablecursorrects%28%29.md)
  Disables all cursor rectangle management within the window.
- [func discardCursorRects()](./discardcursorrects%28%29.md)
  Invalidates all cursor rectangles in the window.
- [func invalidateCursorRects(for: NSView)](./invalidatecursorrects%28for%29.md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.
- [func resetCursorRects()](./resetcursorrects%28%29.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](../nsview.md) objects in its view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/arecursorrectsenabled)*