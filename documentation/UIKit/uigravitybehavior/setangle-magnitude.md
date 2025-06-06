# setAngle(_:magnitude:)

**Framework**: UIKit  
**Kind**: method

Sets the angle and magnitude of the gravity vector for the behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setAngle(_ angle: CGFloat, magnitude: CGFloat)
```

## Parameters

- `angle`: The radian angle for the gravity vector, using standard UIKit geometry. Specify the value   to create a force that pulls items downward toward the bottom of the reference view.
- `magnitude`: The magnitude of the gravitational force. Specify   to get the standard UIKit gravity, which has an acceleration value of 1000 points / second².

## See Also

- [var gravityDirection: CGVector](uigravitybehavior/gravitydirection.md)
  The direction and magnitude of the gravitational force, expressed as a vector.
- [var angle: CGFloat](uigravitybehavior/angle.md)
  The direction of the gravity vector, expressed in radians in the reference coordinate system.
- [var magnitude: CGFloat](uigravitybehavior/magnitude.md)
  The magnitude of the gravity vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigravitybehavior/setangle(_:magnitude:))*