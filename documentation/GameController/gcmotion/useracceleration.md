# userAcceleration

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The acceleration that the user applies to the controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var userAcceleration: GCAcceleration { get }
```

```objc
@property (nonatomic, readonly) GCAcceleration userAcceleration;
```

## See Also

### Accessing Gravity and Acceleration Data
- [var acceleration: GCAcceleration](./acceleration.md)
  The total acceleration of the controller that includes gravity and the acceleration the user applies to the controller.
- [var gravity: GCAcceleration](./gravity.md)
  The gravity acceleration vector from the controller’s reference frame.
- [struct GCAcceleration](../gcacceleration.md)
  A three-dimensional acceleration vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/useracceleration)*