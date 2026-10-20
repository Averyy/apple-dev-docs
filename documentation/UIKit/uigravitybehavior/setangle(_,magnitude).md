# setAngle(_:magnitude:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the angle and magnitude of the gravity vector for the behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setAngle(_ angle: CGFloat, magnitude: CGFloat)
```

```objc
- (void) setAngle:(CGFloat) angle magnitude:(CGFloat) magnitude;
```

## Parameters

- `angle`: The radian angle for the gravity vector, using standard UIKit geometry. Specify the value `pi / 2` to create a force that pulls items downward toward the bottom of the reference view.
- `magnitude`: The magnitude of the gravitational force. Specify `1.0` to get the standard UIKit gravity, which has an acceleration value of 1000 points / second².

## See Also

### Configuring a gravity behavior
- [var gravityDirection: CGVector](./gravitydirection.md)
  The direction and magnitude of the gravitational force, expressed as a vector.
- [var angle: CGFloat](./angle.md)
  The direction of the gravity vector, expressed in radians in the reference coordinate system.
- [var magnitude: CGFloat](./magnitude.md)
  The magnitude of the gravity vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigravitybehavior/setangle(_:magnitude:))*