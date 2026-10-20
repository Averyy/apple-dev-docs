# addSubview(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a view to the view’s subviews so it’s displayed above its siblings.

**Availability**:
- macOS

## Declaration

```swift
func addSubview(_ view: NSView)
```

```objc
- (void) addSubview:(NSView *) view;
```

#### Discussion

This method also sets the view as the next responder of `aView`.

The view retains `aView`. If you use [`removeFromSuperview()`](./removefromsuperview%28%29.md) to remove `aView` from the view hierarchy, `aView` is released. If you want to keep using `aView` after removing it from the view hierarchy (if, for example, you are swapping through a number of views), you must retain it before invoking [`removeFromSuperview()`](./removefromsuperview%28%29.md).

## Parameters

- `view`: The view to add to the view as a subview.

## See Also

### Related Documentation
- [func viewWillMove(toSuperview: NSView?)](./viewwillmove%28tosuperview%29.md)
  Informs the view that its superview is about to change to the specified superview (which may be `nil`).
- [var subviews: [NSView]](./subviews.md)
  The array of views embedded in the current view.
- [func viewWillMove(toWindow: NSWindow?)](./viewwillmove%28towindow%29.md)
  Informs the view that it’s being added to the view hierarchy of the specified window object (which may be `nil`).
- [var nextResponder: NSResponder?](../nsresponder/nextresponder.md)
  The next responder after this one, or `nil` if it has none.
### Adding and Removing Subviews
- [func addSubview(NSView, positioned: NSWindow.OrderingMode, relativeTo: NSView?)](./addsubview%28_,positioned,relativeto%29.md)
  Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.
- [func removeFromSuperview()](./removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [func removeFromSuperviewWithoutNeedingDisplay()](./removefromsuperviewwithoutneedingdisplay%28%29.md)
  Unlinks the view from its superview and its window and removes it from the responder chain, but does not invalidate its cursor rectangles to cause redrawing.
- [func replaceSubview(NSView, with: NSView)](./replacesubview%28_,with%29.md)
  Replaces one of the view’s subviews with another view.
- [func sortSubviews((NSView, NSView, UnsafeMutableRawPointer?) -> ComparisonResult, context: UnsafeMutableRawPointer?)](./sortsubviews%28_,context%29.md)
  Orders the view’s immediate subviews using the specified comparator function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addsubview(_:))*