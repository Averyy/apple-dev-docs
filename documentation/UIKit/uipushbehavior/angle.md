# angle

**Framework**: UIKit  
**Kind**: property

The angle, in radians, of the force vector for the behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var angle: CGFloat { get set }
```

#### Discussion

The default angle is `0` radians, using standard UIKit geometry. To configure the force vector for a push behavior, set the [`magnitude`](uipushbehavior/magnitude.md) property as well as the [`angle`](uipushbehavior/angle.md) property.

Alternatively, you can express the direction of force by using  and  components with the [`pushDirection`](uipushbehavior/pushdirection.md) property. Whichever approach you use, the alternate, equivalent values update automatically.

## See Also

- [func setAngle(CGFloat, magnitude: CGFloat)](uipushbehavior/setangle(_:magnitude:).md)
  Sets the angle and magnitude of the force vector for the behavior.
- [var magnitude: CGFloat](uipushbehavior/magnitude.md)
  The magnitude of the force vector for the push behavior.
- [var mode: UIPushBehavior.Mode](uipushbehavior/mode-swift.property.md)
  Returns the force mode for the push behavior.
- [func setTargetOffsetFromCenter(UIOffset, for: any UIDynamicItem)](uipushbehavior/settargetoffsetfromcenter(_:for:).md)
  Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [func targetOffsetFromCenter(for: any UIDynamicItem) -> UIOffset](uipushbehavior/targetoffsetfromcenter(for:).md)
  Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [var pushDirection: CGVector](uipushbehavior/pushdirection.md)
  The direction of the force vector for the behavior, expressed as  and  components and using standard UIKit geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipushbehavior/angle)*