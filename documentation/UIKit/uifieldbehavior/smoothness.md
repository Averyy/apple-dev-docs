# smoothness

**Framework**: UIKit  
**Kind**: property

The smoothness of the noise used to generate the field.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var smoothness: CGFloat { get set }
```

#### Discussion

For noise and turbulence fields, this value specifies the amount of noise or turbulence. The value of this property is in the range `0.0` to `1.0`, where `0.0` represents the maximum noise or turbulence and `1.0` represents the least amount of noise or turbulence.

## See Also

- [var position: CGPoint](uifieldbehavior/position.md)
  The position of the field in the reference coordinate system.
- [var region: UIRegion](uifieldbehavior/region.md)
  The shape of the field.
- [var strength: CGFloat](uifieldbehavior/strength.md)
  The strength of the field.
- [var falloff: CGFloat](uifieldbehavior/falloff.md)
  The rate of decay for the field strength.
- [var minimumRadius: CGFloat](uifieldbehavior/minimumradius.md)
  The minimum distance at which to start calculating new values for the field.
- [var direction: CGVector](uifieldbehavior/direction.md)
  The direction of motion for a linear field.
- [var animationSpeed: CGFloat](uifieldbehavior/animationspeed.md)
  The rate at which the animation should proceed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifieldbehavior/smoothness)*