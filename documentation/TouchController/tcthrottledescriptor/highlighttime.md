# highlightTime

**Framework**: Touch Controller  
**Kind**: property

The time it takes for a highlight to fade away, in seconds.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var highlightTime: simd_float1 { get set }
```

## See Also

- [var anchor: TCTransformAnchor](tcthrottledescriptor/anchor.md)
  The anchor point that the throttle’s offset is relative to.
- [var backgroundVisuals: TCControlVisuals?](tcthrottledescriptor/backgroundvisuals.md)
  The visuals for the background of the throttle.
- [var baseValue: CGFloat](tcthrottledescriptor/basevalue.md)
  The initial value of this control.
- [var colliderType: TCColliderType](tcthrottledescriptor/collidertype.md)
  The type of collider to use for the throttle.
- [var indicatorSize: CGSize](tcthrottledescriptor/indicatorsize.md)
  The size (width, height) of the indicator itself in points.
- [var indicatorVisuals: TCControlVisuals?](tcthrottledescriptor/indicatorvisuals.md)
  The visuals for the indicator of the throttle.
- [var label: TCControlLabel](tcthrottledescriptor/label.md)
  The label associated with the throttle.
- [var layer: simd_int1](tcthrottledescriptor/layer.md)
  The layer of the throttle, used for z-sorting.
- [var offset: CGPoint](tcthrottledescriptor/offset.md)
  The control’s offset from the anchor, which determines its position.
- [var orientation: TCThrottleOrientation](tcthrottledescriptor/orientation.md)
  The orientation of the throttle.
- [var size: CGSize](tcthrottledescriptor/size.md)
  The size (width, height) of the throttle in points.
- [var snapToBaseValue: Bool](tcthrottledescriptor/snaptobasevalue.md)
  A Boolean value that indicates whether the control reverts to it’s base value.
- [var throttleSize: CGSize](tcthrottledescriptor/throttlesize.md)
  The size (width, height) of the throttle itself, providing boundaries for the indicator, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tcthrottledescriptor/highlighttime)*