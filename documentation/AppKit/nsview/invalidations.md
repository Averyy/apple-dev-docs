# NSView.Invalidations

**Framework**: AppKit  
**Kind**: enum

Changes that cause aspects of a view to be invalid and require an update.

**Availability**:
- macOS 12.0+
- Swift 5.1+

## Declaration

```swift
enum Invalidations
```

## Topics

### Types of Invalidations
- [NSView.Invalidations.Constraints](nsview/invalidations/constraints.md)
  A change that invalidates a view’s constraints.
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

## See Also

- [func invalidate(view: NSView)](nsviewinvalidating/invalidate(view:).md)
  Indicates to the system that an aspect of a view is invalid and triggers the necessary update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/invalidations)*