# NSView.Invalidations.Tuple

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

A change that invalidates a combination of factors covered by the other invalidation types.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
struct Tuple<Invalidation1, Invalidation2> where Invalidation1 : NSViewInvalidating, Invalidation2 : NSViewInvalidating
```

## Overview

The system uses this type when a change invalidates multiple aspects of a view. Use a tuple of the static values defined in [`NSViewInvalidating`](../../nsviewinvalidating.md) when more than one invalidation type applies to a change.

## Topics

### Creating the invalidation type
- [init(Invalidation1, Invalidation2)](./tuple/init%28_,_%29.md)
  Creates the invalidation type.
### Invalidating the view
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
- [NSView.Invalidations.IntrinsicContentSize](./intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [NSView.Invalidations.Layout](./layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [NSView.Invalidations.RestorableState](./restorablestate.md)
  A change that invalidates the restorable state of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidations/tuple)*