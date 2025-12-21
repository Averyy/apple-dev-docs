# NSView.Invalidations.Display

**Framework**: AppKit  
**Kind**: struct

A change that requires the system to redraw a view’s content.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
struct Display
```

#### Overview

Use [`display`](nsviewinvalidating/display.md) to create an instance of this type.

## Topics

### Creating the invalidation type
- [func display()](nsview/display.md)
  Displays the view and all its subviews if possible, invoking each of the `NSView` methods [`lockFocus()`](nsview/lockfocus().md), [`draw(_:)`](nsview/draw(_:).md), and [`unlockFocus()`](nsview/unlockfocus().md) as necessary.
- [init()](nsview/invalidations/display/init.md)
  Creates the invalidation type.
### Invalidating the display
- [func invalidate(view: NSView)](nsviewinvalidating/invalidate(view:).md)
  Indicates to the system that an aspect of a view is invalid and triggers the necessary update.

## Relationships

### Conforms To
- [NSViewInvalidating](nsviewinvalidating.md)

## See Also

- [NSView.Invalidations.Constraints](nsview/invalidations/constraints.md)
  A change that invalidates a view’s constraints.
- [NSView.Invalidations.IntrinsicContentSize](nsview/invalidations/intrinsiccontentsize.md)
  A change that invalidates a view’s intrinsic size.
- [NSView.Invalidations.Layout](nsview/invalidations/layout.md)
  A change that invalidates the layout of the containing view’s subviews.
- [NSView.Invalidations.RestorableState](nsview/invalidations/restorablestate.md)
  A change that invalidates the restorable state of the view.
- [NSView.Invalidations.Tuple](nsview/invalidations/tuple.md)
  A change that invalidates a combination of factors covered by the other invalidation types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidations/display)*