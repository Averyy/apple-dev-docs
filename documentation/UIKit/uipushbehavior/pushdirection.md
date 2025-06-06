# pushDirection

**Framework**: UIKit  
**Kind**: property

The direction of the force vector for the behavior, expressed as  and  components and using standard UIKit geometry.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var pushDirection: CGVector { get set }
```

#### Discussion

The default `x` and `y` values of the push direction vector are each `0.0`. A value for either component of `1.0`, applied to a 100 point x 100 point view, whose density value is `1.0`, results in view acceleration of 100 points / second² in the positive direction for the component.

Setting either direction component to a negative value reverses the direction of force for the component.

Whether you express a push behavior’s push direction in terms of ,  components or with an angle (by using the [`angle`](uipushbehavior/angle.md) property), the alternate, equivalent value updates automatically.

## See Also

- [func setAngle(CGFloat, magnitude: CGFloat)](uipushbehavior/setangle(_:magnitude:).md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var angle: CGFloat](uipushbehavior/angle.md)
  The angle, in radians, of the force vector for the behavior.
- [var magnitude: CGFloat](uipushbehavior/magnitude.md)
  The magnitude of the force vector for the push behavior.
- [var mode: UIPushBehavior.Mode](uipushbehavior/mode-swift.property.md)
  Returns the force mode for the push behavior.
- [func setTargetOffsetFromCenter(UIOffset, for: any UIDynamicItem)](uipushbehavior/settargetoffsetfromcenter(_:for:).md)
  Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](uipushbehavior/targetoffsetfromcenter(for:).md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/pushdirection)*