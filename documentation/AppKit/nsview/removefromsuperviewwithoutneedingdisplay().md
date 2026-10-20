# removeFromSuperviewWithoutNeedingDisplay()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unlinks the view from its superview and its window and removes it from the responder chain, but does not invalidate its cursor rectangles to cause redrawing.

**Availability**:
- macOS

## Declaration

```swift
func removeFromSuperviewWithoutNeedingDisplay()
```

```objc
- (void) removeFromSuperviewWithoutNeedingDisplay;
```

#### Discussion

The view is also released; if you plan to reuse it, be sure to retain it before sending this message and to release it as appropriate when adding it as a subview of another view.

Unlike its counterpart, [`removeFromSuperview()`](./removefromsuperview%28%29.md), this method can be safely invoked during display.

## See Also

### Adding and Removing Subviews
- [func addSubview(NSView)](./addsubview%28_%29.md)
  Adds a view to the view’s subviews so it’s displayed above its siblings.
- [func addSubview(NSView, positioned: NSWindow.OrderingMode, relativeTo: NSView?)](./addsubview%28_,positioned,relativeto%29.md)
  Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.
- [func removeFromSuperview()](./removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [func replaceSubview(NSView, with: NSView)](./replacesubview%28_,with%29.md)
  Replaces one of the view’s subviews with another view.
- [func sortSubviews((NSView, NSView, UnsafeMutableRawPointer?) -> ComparisonResult, context: UnsafeMutableRawPointer?)](./sortsubviews%28_,context%29.md)
  Orders the view’s immediate subviews using the specified comparator function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removefromsuperviewwithoutneedingdisplay())*