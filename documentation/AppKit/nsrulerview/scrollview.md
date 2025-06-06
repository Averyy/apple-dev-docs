# scrollView

**Framework**: AppKit  
**Kind**: property

The NSScrollView that owns the receiver to `scrollView`, without retaining it.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var scrollView: NSScrollView? { get set }
```

#### Discussion

This method is generally invoked only by the ruler’s scroll view; you should rarely need to invoke it directly.

## See Also

- [var verticalRulerView: NSRulerView?](nsscrollview/verticalrulerview.md)
  The scroll view’s vertical ruler view.
- [var horizontalRulerView: NSRulerView?](nsscrollview/horizontalrulerview.md)
  The scroll view’s horizontal ruler view.
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
- [var baselineLocation: CGFloat](nsrulerview/baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.
- [var isFlipped: Bool](nsrulerview/isflipped.md)
  A Boolean that indicates if the ruler view’s coordinate system is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/scrollview)*