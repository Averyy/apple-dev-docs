# isFlipped

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates if the ruler view’s coordinate system is flipped.

**Availability**:
- macOS

## Declaration

```swift
var isFlipped: Bool { get }
```

```objc
@property (readonly, getter=isFlipped) BOOL flipped;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver’s coordinate system is flipped, [`false`](../../Swift/false.md) otherwise.

A vertical ruler takes into account whether the coordinate system of the [`NSScrollView`](../nsscrollview.md)‘s document view—not the receiver’s client view—is flipped. A horizontal ruler is always flipped.

## See Also

### Ruler layout
- [var scrollView: NSScrollView?](./scrollview.md)
  The NSScrollView that owns the receiver to `scrollView`, without retaining it.
- [var orientation: NSRulerView.Orientation](./orientation-swift.property.md)
  The orientation of the receiver to `orientation`.
- [NSRulerView.Orientation](./orientation-swift.enum.md)
  These constants are defined to specify a ruler’s orientation and are used by [`orientation`](./orientation-swift.property.md).
- [var reservedThicknessForAccessoryView: CGFloat](./reservedthicknessforaccessoryview.md)
  The room available for the receiver’s accessory view to `thickness`.
- [var reservedThicknessForMarkers: CGFloat](./reservedthicknessformarkers.md)
  The room available for ruler markers to `thickness`.
- [var ruleThickness: CGFloat](./rulethickness.md)
  The thickness of the area where ruler hash marks and labels are drawn.
- [var requiredThickness: CGFloat](./requiredthickness.md)
  The thickness needed for proper tiling of the receiver within an NSScrollView.
- [var baselineLocation: CGFloat](./baselinelocation.md)
  The location of the receiver’s baseline, in its own coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulerview/isflipped)*