# baselineLocation

**Framework**: AppKit  
**Kind**: property

The location of the receiver’s baseline, in its own coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var baselineLocation: CGFloat { get }
```

#### Discussion

This is a y position for horizontal rulers and an x position for vertical ones.

## See Also

- [var scrollView: NSScrollView?](nsrulerview/scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
- [var orientation: NSRulerView.Orientation](nsrulerview/orientation-swift.property.md)
  The orientation of the receiver to `orientation`.
- [NSRulerView.Orientation](nsrulerview/orientation-swift.enum.md)
  These constants are defined to specify a ruler’s orientation and are used by [`orientation`](nsrulerview/orientation-swift.property.md).
- [var reservedThicknessForAccessoryView: CGFloat](nsrulerview/reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.
- [var reservedThicknessForMarkers: CGFloat](nsrulerview/reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
- [var ruleThickness: CGFloat](nsrulerview/rulethickness.md)
  The thickness of the area where ruler hash marks and labels are drawn.
- [var requiredThickness: CGFloat](nsrulerview/requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var isFlipped: Bool](nsrulerview/isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/baselinelocation)*