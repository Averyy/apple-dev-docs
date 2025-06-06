# resetCursorRects()

**Framework**: AppKit  
**Kind**: method

Overridden by subclasses to define their default cursor rectangles.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func resetCursorRects()
```

#### Discussion

A subclass’s implementation must invoke [`addCursorRect(_:cursor:)`](nsview/addcursorrect(_:cursor:).md) for each cursor rectangle it wants to establish. The default implementation does nothing.

Application code should never invoke this method directly; it’s invoked automatically as described in “[`Responding to User Events and Actions`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/SubclassingNSView/SubclassingNSView.html#//apple_ref/doc/uid/TP40002978-CH7-SW26).” Use the [`invalidateCursorRects(for:)`](nswindow/invalidatecursorrects(for:).md) method instead to explicitly rebuild cursor rectangles.

## See Also

- [var visibleRect: NSRect](nsview/visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
- [func addCursorRect(NSRect, cursor: NSCursor)](nsview/addcursorrect(_:cursor:).md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func removeCursorRect(NSRect, cursor: NSCursor)](nsview/removecursorrect(_:cursor:).md)
  Completely removes a cursor rectangle from the view.
- [func discardCursorRects()](nsview/discardcursorrects.md)
  Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](nsview/addcursorrect(_:cursor:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/resetcursorrects())*