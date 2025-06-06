# areCursorRectsEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window’s cursor rectangles are enabled.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var areCursorRectsEnabled: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when cursor rectangles are enabled; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func addCursorRect(NSRect, cursor: NSCursor)](nsview/addcursorrect(_:cursor:).md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func enableCursorRects()](nswindow/enablecursorrects.md)
  Reenables cursor rectangle management within the window after a [`disableCursorRects()`](nswindow/disablecursorrects().md) message.
- [func disableCursorRects()](nswindow/disablecursorrects.md)
  Disables all cursor rectangle management within the window.
- [func discardCursorRects()](nswindow/discardcursorrects.md)
  Invalidates all cursor rectangles in the window.
- [func invalidateCursorRects(for: NSView)](nswindow/invalidatecursorrects(for:).md)
  Marks as invalid the cursor rectangles of a given view object in the window, so they’ll be set up again when the window becomes key.
- [func resetCursorRects()](nswindow/resetcursorrects.md)
  Clears the window’s cursor rectangles and the cursor rectangles of the [`NSView`](nsview.md) objects in its view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/arecursorrectsenabled)*