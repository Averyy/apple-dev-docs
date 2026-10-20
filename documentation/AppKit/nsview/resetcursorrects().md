# resetCursorRects()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to define their default cursor rectangles.

**Availability**:
- macOS

## Declaration

```swift
func resetCursorRects()
```

```objc
- (void) resetCursorRects;
```

#### Discussion

A subclass’s implementation must invoke [`addCursorRect(_:cursor:)`](./addcursorrect%28_,cursor%29.md) for each cursor rectangle it wants to establish. The default implementation does nothing.

Application code should never invoke this method directly; it’s invoked automatically as described in “[Responding to User Events and Actions](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/SubclassingNSView/SubclassingNSView.html#//apple_ref/doc/uid/TP40002978-CH7-SW26).” Use the [`invalidateCursorRects(for:)`](../nswindow/invalidatecursorrects%28for%29.md) method instead to explicitly rebuild cursor rectangles.

## See Also

### Related Documentation
- [var visibleRect: NSRect](./visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
### Responding to Cursor Movements
- [func addCursorRect(NSRect, cursor: NSCursor)](./addcursorrect%28_,cursor%29.md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func removeCursorRect(NSRect, cursor: NSCursor)](./removecursorrect%28_,cursor%29.md)
  Completely removes a cursor rectangle from the view.
- [func discardCursorRects()](./discardcursorrects%28%29.md)
  Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](./addcursorrect%28_,cursor%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/resetcursorrects())*