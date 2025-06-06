# setAttitude(_:)

**Framework**: Game Controller  
**Kind**: method

Sets the controller’s attitude.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setAttitude(_ attitude: GCQuaternion)
```

## Parameters

- `attitude`: The orientation of a body relative to the controller’s reference frame.

## See Also

- [func setStateFrom(GCMotion)](gcmotion/setstatefrom(_:).md)
  Copies the input values from a specified motion profile to a snapshot of a motion profile.
- [func setRotationRate(GCRotationRate)](gcmotion/setrotationrate(_:).md)
  Sets the controller’s rotation rate.
- [func setAcceleration(GCAcceleration)](gcmotion/setacceleration(_:).md)
  Sets the total acceleration of the controller that includes gravity and the user’s acceleration.
- [func setGravity(GCAcceleration)](gcmotion/setgravity(_:).md)
  Sets the controller’s gravity data.
- [func setUserAcceleration(GCAcceleration)](gcmotion/setuseracceleration(_:).md)
  Sets the acceleration the user applies to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/setattitude(_:))*