# layout

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A change that invalidates the layout of the containing view’s subviews.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
static var layout: NSView.Invalidations.Layout { get }
```

Available when `Self` is `NSView.Invalidations.Layout`.

#### Discussion

Use this invalidation type to set [`needsLayout`](../nsview/needslayout.md) so that a change in property value triggers the system to update the layout of the containing view’s subviews.

## See Also

### Types of Invalidations
- [static var constraints: NSView.Invalidations.Constraints](./constraints.md)
  A change that invalidates a view’s constraints.
- [static var display: NSView.Invalidations.Display](./display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: NSView.Invalidations.IntrinsicContentSize](./intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var restorableState: NSView.Invalidations.RestorableState](./restorablestate.md)
  A change that invalidates the restorable state of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewinvalidating/layout)*