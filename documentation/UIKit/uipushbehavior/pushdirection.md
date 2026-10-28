# pushDirection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The direction of the force vector for the behavior, expressed as *x* and *y* components and using standard UIKit geometry.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var pushDirection: CGVector { get set }
```

```objc
@property (nonatomic, readwrite) CGVector pushDirection;
```

## Discussion

The default `x` and `y` values of the push direction vector are each `0.0`. A value for either component of `1.0`, applied to a 100 point x 100 point view, whose density value is `1.0`, results in view acceleration of 100 points / second² in the positive direction for the component.

Setting either direction component to a negative value reverses the direction of force for the component.

Whether you express a push behavior’s push direction in terms of *x*, *y* components or with an angle (by using the [`angle`](./angle.md) property), the alternate, equivalent value updates automatically.

## See Also

### Configuring a push behavior
- [func setAngle(CGFloat, magnitude: CGFloat)](./setangle%28_,magnitude%29.md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var angle: CGFloat](./angle.md)
  The angle, in radians, of the force vector for the behavior.
- [var magnitude: CGFloat](./magnitude.md)
  The magnitude of the force vector for the push behavior.
- [var mode: UIPushBehavior.Mode](./mode-swift.property.md)
  Returns the force mode for the push behavior.
- [func setTargetOffsetFromCenter(UIOffset, for: any UIDynamicItem)](./settargetoffsetfromcenter%28_,for%29.md)
  Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](./targetoffsetfromcenter%28for%29.md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/pushdirection)*