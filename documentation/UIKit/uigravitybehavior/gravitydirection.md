# gravityDirection

**Framework**: UIKit  
**Kind**: property

The direction and magnitude of the gravitational force, expressed as a vector.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var gravityDirection: CGVector { get set }
```

#### Discussion

The gravity vector is expressed as an  pair that represents the relative motion along the x and y axes of the reference view. A value of `1.0` corresponds to an acceleration of 1000 points / second², which is referred to as UIKit gravity and approximates the Earth’s own gravitational force. A value of `-1.0` represents the same amount of force, but in the opposite direction of the corresponding axis.

The default value of this property is the vector (`0.0, 1.0`), which represents a downward force in the reference view. Changing the [`angle`](uigravitybehavior/angle.md) or [`magnitude`](uigravitybehavior/magnitude.md) values also changes the value of this property.

## See Also

- [var angle: CGFloat](uigravitybehavior/angle.md)
  The direction of the gravity vector, expressed in radians in the reference coordinate system.
- [var magnitude: CGFloat](uigravitybehavior/magnitude.md)
  The magnitude of the gravity vector.
- [func setAngle(CGFloat, magnitude: CGFloat)](uigravitybehavior/setangle(_:magnitude:).md)
  Sets the angle and magnitude of the gravity vector for the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigravitybehavior/gravitydirection)*