# removeFromSuperviewWithoutNeedingDisplay()

**Framework**: AppKit  
**Kind**: method

Unlinks the view from its superview and its window and removes it from the responder chain, but does not invalidate its cursor rectangles to cause redrawing.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeFromSuperviewWithoutNeedingDisplay()
```

#### Discussion

The view is also released; if you plan to reuse it, be sure to retain it before sending this message and to release it as appropriate when adding it as a subview of another view.

Unlike its counterpart, [`removeFromSuperview()`](nsview/removefromsuperview().md), this method can be safely invoked during display.

## See Also

- [func addSubview(NSView)](nsview/addsubview(_:).md)
  Adds a view to the view’s subviews so it’s displayed above its siblings.
- [func addSubview(NSView, positioned: NSWindow.OrderingMode, relativeTo: NSView?)](nsview/addsubview(_:positioned:relativeto:).md)
  Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.
- [func removeFromSuperview()](nsview/removefromsuperview.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [func replaceSubview(NSView, with: NSView)](nsview/replacesubview(_:with:).md)
  Replaces one of the view’s subviews with another view.
- [func sortSubviews((NSView, NSView, UnsafeMutableRawPointer?) -> ComparisonResult, context: UnsafeMutableRawPointer?)](nsview/sortsubviews(_:context:).md)
  Orders the view’s immediate subviews using the specified comparator function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removefromsuperviewwithoutneedingdisplay())*