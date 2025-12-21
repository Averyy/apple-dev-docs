# NSView.Invalidations.IntrinsicContentSize

**Framework**: AppKit  
**Kind**: struct

A change that invalidates a view’s intrinsic size.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
struct IntrinsicContentSize
```

#### Overview

Use [`intrinsicContentSize`](nsviewinvalidating/intrinsiccontentsize.md) to create an instance of this type.

## Topics

### Creating the invalidation type
- [var intrinsicContentSize: NSSize](nsview/intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [init()](nsview/invalidations/intrinsiccontentsize/init.md)
  Creates the invalidation type.
### Invalidating the intrinsic size
- [func invalidate(view: NSView)](nsviewinvalidating/invalidate(view:).md)
  Indicates to the system that an aspect of a view is invalid and triggers the necessary update.

## Relationships

### Conforms To
- [NSViewInvalidating](nsviewinvalidating.md)

## See Also

- [NSView.Invalidations.Constraints](nsview/invalidations/constraints.md)
  A change that invalidates a view’s constraints.
- [NSView.Invalidations.Display](nsview/invalidations/display.md)
  A change that requires the system to redraw a view’s content.
- [NSView.Invalidations.Layout](nsview/invalidations/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [NSView.Invalidations.RestorableState](nsview/invalidations/restorablestate.md)
  A change that invalidates the restorable state of the view.
- [NSView.Invalidations.Tuple](nsview/invalidations/tuple.md)
  A change that invalidates a combination of factors covered by the other invalidation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidations/intrinsiccontentsize)*