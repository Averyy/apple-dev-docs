# GCQuaternion

**Framework**: Game Controller  
**Kind**: struct

A quaternion that represents a controller’s measurement of attitude.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GCQuaternion
```

## Topics

### Getting Quaternion Values
- [var x: Double](gcquaternion/x.md)
  The value for the x-axis of the quaternion.
- [var y: Double](gcquaternion/y.md)
  The value for the y-axis of the quaternion.
- [var z: Double](gcquaternion/z.md)
  The value for the z-axis of the quaternion.
- [var w: Double](gcquaternion/w.md)
  The value for the w-axis of the quaternion.
### Initializers
- [init()](gcquaternion/init.md)
  Creates a quaternion structure.
- [init(x: Double, y: Double, z: Double, w: Double)](gcquaternion/init(x:y:z:w:).md)
  Creates a quaternion structure with the specified values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var attitude: GCQuaternion](gcmotion/attitude.md)
  The attitude of the controller.
- [var rotationRate: GCRotationRate](gcmotion/rotationrate.md)
  The rotation rate of the controller.
- [struct GCRotationRate](gcrotationrate.md)
  A structure that represents rotation rates around the x, y, and z axes.
- [struct GCEulerAngles](gceulerangles.md)
  A structure that specifies the controller’s attitude as a series of rotations around the x, y, and z axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcquaternion)*