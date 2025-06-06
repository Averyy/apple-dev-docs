# addSubview(_:positioned:relativeTo:)

**Framework**: AppKit  
**Kind**: method

Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addSubview(_ view: NSView, positioned place: NSWindow.OrderingMode, relativeTo otherView: NSView?)
```

#### Discussion

This method also sets the view as the next responder of `aView`.

The view retains `aView`. If you use [`removeFromSuperview()`](nsview/removefromsuperview().md) to remove `aView` from the view hierarchy, `aView` is released. If you want to keep using `aView` after removing it from the view hierarchy (if, for example, you are swapping through a number of views), you must retain it before invoking [`removeFromSuperview()`](nsview/removefromsuperview().md).

## Parameters

- `view`: The view object to add to the view as a subview.
- `place`: An   constant specifying the position of the   relative to  . Valid values are   or  .
- `otherView`: The other view   is to be positioned relative to. If   is   (or isn’t a subview of the view),   is added above or below all of its new siblings.

## See Also

- [var subviews: [NSView]](nsview/subviews.md)
  The array of views embedded in the current view.
- [var nextResponder: NSResponder?](nsresponder/nextresponder.md)
  The next responder after this one, or `nil` if it has none.
- [func addSubview(NSView)](nsview/addsubview(_:).md)
  Adds a view to the view’s subviews so it’s displayed above its siblings.
- [func removeFromSuperview()](nsview/removefromsuperview.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [func removeFromSuperviewWithoutNeedingDisplay()](nsview/removefromsuperviewwithoutneedingdisplay.md)
  Unlinks the view from its superview and its window and removes it from the responder chain, but does not invalidate its cursor rectangles to cause redrawing.
- [func replaceSubview(NSView, with: NSView)](nsview/replacesubview(_:with:).md)
  Replaces one of the view’s subviews with another view.
- [func sortSubviews((NSView, NSView, UnsafeMutableRawPointer?) -> ComparisonResult, context: UnsafeMutableRawPointer?)](nsview/sortsubviews(_:context:).md)
  Orders the view’s immediate subviews using the specified comparator function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addsubview(_:positioned:relativeto:))*