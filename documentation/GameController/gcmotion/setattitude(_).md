# setAttitude(_:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setAttitude:(GCQuaternion) attitude;
```

## Parameters

- `attitude`: The orientation of a body relative to the controller’s reference frame.

## See Also

### Setting Snapshot Values
- [func setStateFrom(GCMotion)](./setstatefrom%28_%29.md)
  Copies the input values from a specified motion profile to a snapshot of a motion profile.
- [func setRotationRate(GCRotationRate)](./setrotationrate%28_%29.md)
  Sets the controller’s rotation rate.
- [func setAcceleration(GCAcceleration)](./setacceleration%28_%29.md)
  Sets the total acceleration of the controller that includes gravity and the user’s acceleration.
- [func setGravity(GCAcceleration)](./setgravity%28_%29.md)
  Sets the controller’s gravity data.
- [func setUserAcceleration(GCAcceleration)](./setuseracceleration%28_%29.md)
  Sets the acceleration the user applies to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/setattitude(_:))*