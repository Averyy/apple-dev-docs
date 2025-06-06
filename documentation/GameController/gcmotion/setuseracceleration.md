# setUserAcceleration(_:)

**Framework**: Game Controller  
**Kind**: method

Sets the acceleration the user applies to the controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setUserAcceleration(_ userAcceleration: GCAcceleration)
```

## Parameters

- `userAcceleration`: The acceleration that the user applies.

## See Also

- [func setStateFrom(GCMotion)](gcmotion/setstatefrom(_:).md)
  Copies the input values from a specified motion profile to a snapshot of a motion profile.
- [func setAttitude(GCQuaternion)](gcmotion/setattitude(_:).md)
  Sets the controller’s attitude.
- [func setRotationRate(GCRotationRate)](gcmotion/setrotationrate(_:).md)
  Sets the controller’s rotation rate.
- [func setAcceleration(GCAcceleration)](gcmotion/setacceleration(_:).md)
  Sets the total acceleration of the controller that includes gravity and the user’s acceleration.
- [func setGravity(GCAcceleration)](gcmotion/setgravity(_:).md)
  Sets the controller’s gravity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/setuseracceleration(_:))*