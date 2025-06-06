# constraints

**Framework**: AppKit  
**Kind**: property

A change that invalidates a view’s constraints.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
static var constraints: NSView.Invalidations.Constraints { get }
```

#### Discussion

Use this invalidation type to set [`needsUpdateConstraints`](nsview/needsupdateconstraints.md) so that a change in property value triggers the containing view to update constraints.

## See Also

- [static var display: NSView.Invalidations.Display](nsviewinvalidating/display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: NSView.Invalidations.IntrinsicContentSize](nsviewinvalidating/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var layout: NSView.Invalidations.Layout](nsviewinvalidating/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [static var restorableState: NSView.Invalidations.RestorableState](nsviewinvalidating/restorablestate.md)
  A change that invalidates the restorable state of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewinvalidating/constraints)*