# setRotationRate(_:)

**Framework**: Game Controller  
**Kind**: method

Sets the controller’s rotation rate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setRotationRate(_ rotationRate: GCRotationRate)
```

## Parameters

- `rotationRate`: A gyroscopic measurement of the controller’s rotation around the x, y, and z axes.

## See Also

- [func setStateFrom(GCMotion)](gcmotion/setstatefrom(_:).md)
  Copies the input values from a specified motion profile to a snapshot of a motion profile.
- [func setAttitude(GCQuaternion)](gcmotion/setattitude(_:).md)
  Sets the controller’s attitude.
- [func setAcceleration(GCAcceleration)](gcmotion/setacceleration(_:).md)
  Sets the total acceleration of the controller that includes gravity and the user’s acceleration.
- [func setGravity(GCAcceleration)](gcmotion/setgravity(_:).md)
  Sets the controller’s gravity data.
- [func setUserAcceleration(GCAcceleration)](gcmotion/setuseracceleration(_:).md)
  Sets the acceleration the user applies to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/setrotationrate(_:))*