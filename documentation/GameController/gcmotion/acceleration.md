# acceleration

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The total acceleration of the controller that includes gravity and the acceleration the user applies to the controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var acceleration: GCAcceleration { get }
```

```objc
@property (nonatomic, readonly) GCAcceleration acceleration;
```

## See Also

### Accessing Gravity and Acceleration Data
- [var gravity: GCAcceleration](./gravity.md)
  The gravity acceleration vector from the controller’s reference frame.
- [var userAcceleration: GCAcceleration](./useracceleration.md)
  The acceleration that the user applies to the controller.
- [struct GCAcceleration](../gcacceleration.md)
  A three-dimensional acceleration vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/acceleration)*