# NSViewInvalidating

**Framework**: AppKit  
**Kind**: protocol

Implements a type of invalidation that can occur on a view that requires an update.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
protocol NSViewInvalidating
```

## Topics

### Types of Invalidations
- [static var constraints: NSView.Invalidations.Constraints](nsviewinvalidating/constraints.md)
  A change that invalidates a view’s constraints.
- [static var display: NSView.Invalidations.Display](nsviewinvalidating/display.md)
  A change that requires the system to redraw a view’s content.
- [static var intrinsicContentSize: NSView.Invalidations.IntrinsicContentSize](nsviewinvalidating/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [static var layout: NSView.Invalidations.Layout](nsviewinvalidating/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [static var restorableState: NSView.Invalidations.RestorableState](nsviewinvalidating/restorablestate.md)
  A change that invalidates the restorable state of the view.
### Supporting Types
- [func invalidate(view: NSView)](nsviewinvalidating/invalidate(view:).md)
  Indicates to the system that an aspect of a view is invalid and triggers the necessary update.
- [NSView.Invalidations](nsview/invalidations.md)
  Changes that cause aspects of a view to be invalid and require an update.

## Relationships

### Conforming Types
- [NSView.Invalidations.Constraints](nsview/invalidations/constraints.md)
- [NSView.Invalidations.Display](nsview/invalidations/display.md)
- [NSView.Invalidations.IntrinsicContentSize](nsview/invalidations/intrinsiccontentsize.md)
- [NSView.Invalidations.Layout](nsview/invalidations/layout.md)
- [NSView.Invalidations.RestorableState](nsview/invalidations/restorablestate.md)
- [NSView.Invalidations.Tuple](nsview/invalidations/tuple.md)

## See Also

- [NSView.Invalidating](nsview/invalidating.md)
  A property wrapper that notifies the system that a property value change has invalidated an aspect of the containing view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewinvalidating)*