# setRotationRate(_:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setRotationRate:(GCRotationRate) rotationRate;
```

## Parameters

- `rotationRate`: A gyroscopic measurement of the controller’s rotation around the x, y, and z axes.

## See Also

### Setting Snapshot Values
- [func setStateFrom(GCMotion)](./setstatefrom%28_%29.md)
  Copies the input values from a specified motion profile to a snapshot of a motion profile.
- [func setAttitude(GCQuaternion)](./setattitude%28_%29.md)
  Sets the controller’s attitude.
- [func setAcceleration(GCAcceleration)](./setacceleration%28_%29.md)
  Sets the total acceleration of the controller that includes gravity and the user’s acceleration.
- [func setGravity(GCAcceleration)](./setgravity%28_%29.md)
  Sets the controller’s gravity data.
- [func setUserAcceleration(GCAcceleration)](./setuseracceleration%28_%29.md)
  Sets the acceleration the user applies to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/setrotationrate(_:))*