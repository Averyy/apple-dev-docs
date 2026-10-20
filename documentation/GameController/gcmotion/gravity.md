# gravity

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The gravity acceleration vector from the controller’s reference frame.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var gravity: GCAcceleration { get }
```

```objc
@property (nonatomic, readonly) GCAcceleration gravity;
```

## See Also

### Accessing Gravity and Acceleration Data
- [var acceleration: GCAcceleration](./acceleration.md)
  The total acceleration of the controller that includes gravity and the acceleration the user applies to the controller.
- [var userAcceleration: GCAcceleration](./useracceleration.md)
  The acceleration that the user applies to the controller.
- [struct GCAcceleration](../gcacceleration.md)
  A three-dimensional acceleration vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/gravity)*