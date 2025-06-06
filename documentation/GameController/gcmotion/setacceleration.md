# setAcceleration(_:)

**Framework**: Game Controller  
**Kind**: method

Sets the total acceleration of the controller that includes gravity and the user’s acceleration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setAcceleration(_ acceleration: GCAcceleration)
```

## Parameters

- `acceleration`: The total acceleration of the controller.

## See Also

- [func setStateFrom(GCMotion)](gcmotion/setstatefrom(_:).md)
  Copies the input values from a specified motion profile to a snapshot of a motion profile.
- [func setAttitude(GCQuaternion)](gcmotion/setattitude(_:).md)
  Sets the controller’s attitude.
- [func setRotationRate(GCRotationRate)](gcmotion/setrotationrate(_:).md)
  Sets the controller’s rotation rate.
- [func setGravity(GCAcceleration)](gcmotion/setgravity(_:).md)
  Sets the controller’s gravity data.
- [func setUserAcceleration(GCAcceleration)](gcmotion/setuseracceleration(_:).md)
  Sets the acceleration the user applies to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/setacceleration(_:))*