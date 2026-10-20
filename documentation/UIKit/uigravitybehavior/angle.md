# angle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The direction of the gravity vector, expressed in radians in the reference coordinate system.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var angle: CGFloat { get set }
```

```objc
@property (nonatomic, readwrite) CGFloat angle;
```

#### Discussion

Modify this property when you want to change the angle of the gravity vector separately from the magnitude of that vector. The value in this property is tied to the value in the [`gravityDirection`](./gravitydirection.md) property, so changes in one affect the other.

The default angle is `pi / 2` radians, which represents a downward force in the reference view. A value of `0` represents a force that moves items toward the right side of the reference view.

## See Also

### Configuring a gravity behavior
- [var gravityDirection: CGVector](./gravitydirection.md)
  The direction and magnitude of the gravitational force, expressed as a vector.
- [var magnitude: CGFloat](./magnitude.md)
  The magnitude of the gravity vector.
- [func setAngle(CGFloat, magnitude: CGFloat)](./setangle%28_,magnitude%29.md)
  Sets the angle and magnitude of the gravity vector for the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigravitybehavior/angle)*