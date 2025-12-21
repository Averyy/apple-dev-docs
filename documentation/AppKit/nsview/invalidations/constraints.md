# NSView.Invalidations.Constraints

**Framework**: AppKit  
**Kind**: struct

A change that invalidates a view’s constraints.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
struct Constraints
```

#### Overview

Use [`constraints`](nsview/constraints.md) to create an instance of this type.

## Topics

### Creating the invalidation type
- [var constraints: [NSLayoutConstraint]](nsview/constraints.md)
  Returns the constraints held by the view.
- [init()](nsview/invalidations/constraints/init.md)
  Creates the invalidation type.
### Invalidating the constraints
- [func invalidate(view: NSView)](nsviewinvalidating/invalidate(view:).md)
  Indicates to the system that an aspect of a view is invalid and triggers the necessary update.

## Relationships

### Conforms To
- [NSViewInvalidating](nsviewinvalidating.md)

## See Also

- [NSView.Invalidations.Display](nsview/invalidations/display.md)
  A change that requires the system to redraw a view’s content.
- [NSView.Invalidations.IntrinsicContentSize](nsview/invalidations/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [NSView.Invalidations.Layout](nsview/invalidations/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [NSView.Invalidations.RestorableState](nsview/invalidations/restorablestate.md)
  A change that invalidates the restorable state of the view.
- [NSView.Invalidations.Tuple](nsview/invalidations/tuple.md)
  A change that invalidates a combination of factors covered by the other invalidation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidations/constraints)*