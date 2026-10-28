# magnitude

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The magnitude of the force vector for the push behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var magnitude: CGFloat { get set }
```

```objc
@property (nonatomic, readwrite) CGFloat magnitude;
```

## Discussion

The default magnitude is `0.0`, equivalent to no force. A continuous force vector with a magnitude of `1.0`, applied to a 100 point x 100 point view whose density value is `1.0`, results in view acceleration of 100 points / second² in the direction indicated by the [`angle`](./angle.md) or [`pushDirection`](./pushdirection.md) property.

Setting the [`magnitude`](./magnitude.md) parameter to a negative value reverses the direction of the force.

## See Also

### Configuring a push behavior
- [func setAngle(CGFloat, magnitude: CGFloat)](./setangle%28_,magnitude%29.md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var angle: CGFloat](./angle.md)
  The angle, in radians, of the force vector for the behavior.
- [var mode: UIPushBehavior.Mode](./mode-swift.property.md)
  Returns the force mode for the push behavior.
- [func setTargetOffsetFromCenter(UIOffset, for: any UIDynamicItem)](./settargetoffsetfromcenter%28_,for%29.md)
  Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](./targetoffsetfromcenter%28for%29.md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [var pushDirection: CGVector](./pushdirection.md)
  The direction of the force vector for the behavior, expressed as *x* and *y* components and using standard UIKit geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/magnitude)*