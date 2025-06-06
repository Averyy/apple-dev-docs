# reservedThicknessForAccessoryView

**Framework**: AppKit  
**Kind**: property

The room available for the receiver’s accessory view to `thickness`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var reservedThicknessForAccessoryView: CGFloat { get set }
```

#### Discussion

If the ruler is horizontal, `thickness` is the height of the accessory view; otherwise, it’s the width. NSRulerViews by default reserve no space for an accessory view.

An NSRulerView automatically increases the reserved thickness as necessary to that of the accessory view. When the accessory view is thinner than the reserved space, it’s centered in that space. If you plan to use several accessory views of different sizes, you should set the reserved thickness beforehand to that of the thickest accessory view, in order to avoid retiling of the NSScrollView.

## See Also

- [var accessoryView: NSView?](nsrulerview/accessoryview.md)
  The receiver’s accessory view to `aView`.
- [var scrollView: NSScrollView?](nsrulerview/scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
- [var orientation: NSRulerView.Orientation](nsrulerview/orientation-swift.property.md)
  The orientation of the receiver to `orientation`.
- [NSRulerView.Orientation](nsrulerview/orientation-swift.enum.md)
  These constants are defined to specify a ruler’s orientation and are used by [`orientation`](nsrulerview/orientation-swift.property.md).
- [var reservedThicknessForMarkers: CGFloat](nsrulerview/reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
- [var ruleThickness: CGFloat](nsrulerview/rulethickness.md)
  The thickness of the area where ruler hash marks and labels are drawn.
- [var requiredThickness: CGFloat](nsrulerview/requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var baselineLocation: CGFloat](nsrulerview/baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.
- [var isFlipped: Bool](nsrulerview/isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/reservedthicknessforaccessoryview)*