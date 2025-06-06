# NSView.Invalidations.RestorableState

**Framework**: AppKit  
**Kind**: struct

A change that invalidates the restorable state of the view.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
struct RestorableState
```

#### Overview

Use [`restorableState`](nsviewinvalidating/restorablestate.md) to create an instance of this type.

## Topics

### Creating the invalidation type
- [init()](nsview/invalidations/restorablestate/init.md)
  Creates the invalidation type.

## Relationships

### Conforms To
- [NSViewInvalidating](nsviewinvalidating.md)

## See Also

- [NSView.Invalidations.Constraints](nsview/invalidations/constraints.md)
  A change that invalidates a view’s constraints.
- [NSView.Invalidations.Display](nsview/invalidations/display.md)
  A change that requires the system to redraw a view’s content.
- [NSView.Invalidations.IntrinsicContentSize](nsview/invalidations/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [NSView.Invalidations.Layout](nsview/invalidations/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [NSView.Invalidations.Tuple](nsview/invalidations/tuple.md)
  A change that invalidates a combination of factors covered by the other invalidation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidations/restorablestate)*