# GCMotion

**Framework**: Game Controller  
**Kind**: class

A controller profile that supports orientation and motion.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCMotion
```

#### Overview

The motion controller profile provides attitude and rotation data, as well as acceleration and sensor information. Use this profile to get motion input from a controller that measures acceleration and rotation rate. If the controller’s [`motion`](gccontroller/motion.md) property is a `GCMotion` object, the controller supports motion.

This illustration shows the direction of the x, y, and z axes of an iPhone when held upright.

![An illustration of a vertical iPhone with the  x-axis passing through its center from side to side, the y-axis passing through its center from top to bottom, and the z-axis passing through its center from back to front.](https://docs-assets.developer.apple.com/published/bfa00799a86f2c65db1da8219375e6dd/media-2930224%402x.png)

## Topics

### Getting the Controller
- [var controller: GCController?](gcmotion/controller.md)
  The controller for the profile.
### Receiving a Callback When Input Values Change
- [var valueChangedHandler: GCMotionValueChangedHandler?](gcmotion/valuechangedhandler.md)
  The block that the profile calls when an element’s value changes.
- [typealias GCMotionValueChangedHandler](gcmotionvaluechangedhandler.md)
  The signature for the block that the profile calls when an element’s value changes.
### Verifying Capabilities
- [var hasAttitude: Bool](gcmotion/hasattitude.md)
  A Boolean value that indicates whether the controller provides attitude data.
- [var hasRotationRate: Bool](gcmotion/hasrotationrate.md)
  A Boolean value that indicates whether the controller provides rotation data.
- [var hasGravityAndUserAcceleration: Bool](gcmotion/hasgravityanduseracceleration.md)
  A Boolean value that indicates whether the controller provides gravity and user acceleration data.
- [var hasAttitudeAndRotationRate: Bool](gcmotion/hasattitudeandrotationrate.md)
  A Boolean value that indicates whether the controller provides attitude and rotation data.
### Accessing Attitude and Rotation Data
- [var attitude: GCQuaternion](gcmotion/attitude.md)
  The attitude of the controller.
- [struct GCQuaternion](gcquaternion.md)
  A quaternion that represents a controller’s measurement of attitude.
- [var rotationRate: GCRotationRate](gcmotion/rotationrate.md)
  The rotation rate of the controller.
- [struct GCRotationRate](gcrotationrate.md)
  A structure that represents rotation rates around the x, y, and z axes.
- [struct GCEulerAngles](gceulerangles.md)
  A structure that specifies the controller’s attitude as a series of rotations around the x, y, and z axes.
### Accessing Gravity and Acceleration Data
- [var acceleration: GCAcceleration](gcmotion/acceleration.md)
  The total acceleration of the controller that includes gravity and the acceleration the user applies to the controller.
- [var gravity: GCAcceleration](gcmotion/gravity.md)
  The gravity acceleration vector from the controller’s reference frame.
- [var userAcceleration: GCAcceleration](gcmotion/useracceleration.md)
  The acceleration that the user applies to the controller.
- [struct GCAcceleration](gcacceleration.md)
  A three-dimensional acceleration vector.
### Accessing Sensor Data
- [var sensorsRequireManualActivation: Bool](gcmotion/sensorsrequiremanualactivation.md)
  A Boolean value that indicates whether the sensors that compute the motion data require manual activation.
- [var sensorsActive: Bool](gcmotion/sensorsactive.md)
  A Boolean value that indicates whether the sensors that compute the motion data are active.
### Setting Snapshot Values
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
- [func setUserAcceleration(GCAcceleration)](gcmotion/setuseracceleration(_:).md)
  Sets the acceleration the user applies to the controller.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Input](input.md)
  Receive controller input in the way that best integrates with the flow of your game or game engine.
- [class GCDeviceBattery](gcdevicebattery.md)
  The charge level and state of a device’s battery.
- [class GCDeviceHaptics](gcdevicehaptics.md)
  The locations of haptic actuators on a game controller.
- [class GCDeviceLight](gcdevicelight.md)
  The colored light on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion)*