# addSubview(_:positioned:relativeTo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts a view among the view’s subviews so it’s displayed immediately above or below another view.

**Availability**:
- macOS

## Declaration

```swift
func addSubview(_ view: NSView, positioned place: NSWindow.OrderingMode, relativeTo otherView: NSView?)
```

```objc
- (void) addSubview:(NSView *) view positioned:(NSWindowOrderingMode) place relativeTo:(NSView *) otherView;
```

## Discussion

This method also sets the view as the next responder of `aView`.

The view retains `aView`. If you use [`removeFromSuperview()`](./removefromsuperview%28%29.md) to remove `aView` from the view hierarchy, `aView` is released. If you want to keep using `aView` after removing it from the view hierarchy (if, for example, you are swapping through a number of views), you must retain it before invoking [`removeFromSuperview()`](./removefromsuperview%28%29.md).

## Parameters

- `view`: The view object to add to the view as a subview.
- `place`: An `enum` constant specifying the position of the `aView` relative to `otherView`. Valid values are `NSWindowAbove` or `NSWindowBelow`.
- `otherView`: The other view `aView` is to be positioned relative to. If `otherView` is `nil` (or isn’t a subview of the view), `aView` is added above or below all of its new siblings.

## See Also

### Related Documentation
- [var subviews: [NSView]](./subviews.md)
  The array of views embedded in the current view.
- [var nextResponder: NSResponder?](../nsresponder/nextresponder.md)
  The next responder after this one, or `nil` if it has none.
### Adding and Removing Subviews
- [func addSubview(NSView)](./addsubview%28_%29.md)
  Adds a view to the view’s subviews so it’s displayed above its siblings.
- [func removeFromSuperview()](./removefromsuperview%28%29.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [func removeFromSuperviewWithoutNeedingDisplay()](./removefromsuperviewwithoutneedingdisplay%28%29.md)
  Unlinks the view from its superview and its window and removes it from the responder chain, but does not invalidate its cursor rectangles to cause redrawing.
- [func replaceSubview(NSView, with: NSView)](./replacesubview%28_,with%29.md)
  Replaces one of the view’s subviews with another view.
- [func sortSubviews((NSView, NSView, UnsafeMutableRawPointer?) -> ComparisonResult, context: UnsafeMutableRawPointer?)](./sortsubviews%28_,context%29.md)
  Orders the view’s immediate subviews using the specified comparator function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addsubview(_:positioned:relativeto:))*