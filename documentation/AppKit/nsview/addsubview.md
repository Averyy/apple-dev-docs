# addSubview(_:)

**Framework**: AppKit  
**Kind**: method

Adds a view to the view’s subviews so it’s displayed above its siblings.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addSubview(_ view: NSView)
```

#### Discussion

This method also sets the view as the next responder of `aView`.

The view retains `aView`. If you use [`removeFromSuperview()`](nsview/removefromsuperview().md) to remove `aView` from the view hierarchy, `aView` is released. If you want to keep using `aView` after removing it from the view hierarchy (if, for example, you are swapping through a number of views), you must retain it before invoking [`removeFromSuperview()`](nsview/removefromsuperview().md).

## Parameters

- `view`: The view to add to the view as a subview.

## See Also

- [func viewWillMove(toSuperview: NSView?)](nsview/viewwillmove(tosuperview:).md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [var subviews: [NSView]](nsview/subviews.md)
  The array of views embedded in the current view.
- [func viewWillMove(toWindow: NSWindow?)](nsview/viewwillmove(towindow:).md)
  Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).
- [var nextResponder: NSResponder?](nsresponder/nextresponder.md)
  The next responder after this one, or `nil` if it has none.
- [func addSubview(NSView, positioned: NSWindow.OrderingMode, relativeTo: NSView?)](nsview/addsubview(_:positioned:relativeto:).md)
  Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.
- [func removeFromSuperview()](nsview/removefromsuperview.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [func removeFromSuperviewWithoutNeedingDisplay()](nsview/removefromsuperviewwithoutneedingdisplay.md)
  Unlinks the view from its superview and its window and removes it from the responder chain, but does not invalidate its cursor rectangles to cause redrawing.
- [func replaceSubview(NSView, with: NSView)](nsview/replacesubview(_:with:).md)
  Replaces one of the view’s subviews with another view.
- [func sortSubviews((NSView, NSView, UnsafeMutableRawPointer?) -> ComparisonResult, context: UnsafeMutableRawPointer?)](nsview/sortsubviews(_:context:).md)
  Orders the view’s immediate subviews using the specified comparator function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addsubview(_:))*