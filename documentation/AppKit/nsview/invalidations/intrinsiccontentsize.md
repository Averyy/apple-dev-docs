# NSView.Invalidations.IntrinsicContentSize

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A change that invalidates a view’s intrinsic size.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
struct IntrinsicContentSize
```

#### Overview

Use [`intrinsicContentSize`](../../nsviewinvalidating/intrinsiccontentsize.md) to create an instance of this type.

## Topics

### Creating the invalidation type
- [var intrinsicContentSize: NSSize](../intrinsiccontentsize.md)
  The natural size for the receiving view, considering only properties of the view itself.
- [init()](./intrinsiccontentsize/init%28%29.md)
  Creates the invalidation type.
### Invalidating the intrinsic size
- [func invalidate(view: NSView)](../../nsviewinvalidating/invalidate%28view%29.md)
  Indicates to the system that an aspect of a view is invalid and triggers the necessary update.

## Relationships

### Conforms To
- [NSViewInvalidating](../../nsviewinvalidating.md)

## See Also

### Types of Invalidations
- [NSView.Invalidations.Constraints](./constraints.md)
  A change that invalidates a view’s constraints.
- [NSView.Invalidations.Display](./display.md)
  A change that requires the system to redraw a view’s content.
- [NSView.Invalidations.Layout](./layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [NSView.Invalidations.RestorableState](./restorablestate.md)
  A change that invalidates the restorable state of the view.
- [NSView.Invalidations.Tuple](./tuple.md)
  A change that invalidates a combination of factors covered by the other invalidation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidations/intrinsiccontentsize)*