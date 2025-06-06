# restorableState

**Framework**: AppKit  
**Kind**: property

A change that invalidates the restorable state of the view.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
static var restorableState: NSView.Invalidations.RestorableState { get }
```

#### Discussion

Use this invalidation type to call [`invalidateRestorableState()`](nsresponder/invalidaterestorablestate().md) so that a change in property value invalidates the viewʼs restorable state. This triggers the app to save any information the restoration system needs to restore the current state of the view.

## See Also

- [static var constraints: NSView.Invalidations.Constraints](nsviewinvalidating/constraints.md)
  A change that invalidates a view’s constraints.
- [static var display: NSView.Invalidations.Display](nsviewinvalidating/display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: NSView.Invalidations.IntrinsicContentSize](nsviewinvalidating/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var layout: NSView.Invalidations.Layout](nsviewinvalidating/layout.md)
  A change that invalidates the layout of the containing view’s subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewinvalidating/restorablestate)*