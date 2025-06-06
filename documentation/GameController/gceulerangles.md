# GCEulerAngles

**Framework**: Game Controller  
**Kind**: struct

A structure that specifies the controller’s attitude as a series of rotations around the x, y, and z axes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GCEulerAngles
```

## Topics

### Getting Euler Angle Values
- [var pitch: Double](gceulerangles/pitch.md)
  The pitch of the controller in radians.
- [var yaw: Double](gceulerangles/yaw.md)
  The yaw of the device in radians.
- [var roll: Double](gceulerangles/roll.md)
  The roll of the controller in radians.
### Initializers
- [init()](gceulerangles/init.md)
  Creates the Euler angles structure.
- [init(pitch: Double, yaw: Double, roll: Double)](gceulerangles/init(pitch:yaw:roll:).md)
  Creates the structure with the specified values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var attitude: GCQuaternion](gcmotion/attitude.md)
  The attitude of the controller.
- [struct GCQuaternion](gcquaternion.md)
  A quaternion that represents a controller’s measurement of attitude.
- [var rotationRate: GCRotationRate](gcmotion/rotationrate.md)
  The rotation rate of the controller.
- [struct GCRotationRate](gcrotationrate.md)
  A structure that represents rotation rates around the x, y, and z axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gceulerangles)*