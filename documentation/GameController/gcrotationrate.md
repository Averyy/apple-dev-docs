# GCRotationRate

**Framework**: Game Controller  
**Kind**: struct

A structure that represents rotation rates around the x, y, and z axes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GCRotationRate
```

## Topics

### Getting Rotation Rate Values
- [var x: Double](gcrotationrate/x.md)
  The rotation rate around the x-axis in radians per second.
- [var y: Double](gcrotationrate/y.md)
  The rotation rate around the y-axis in radians per second.
- [var z: Double](gcrotationrate/z.md)
  The rotation rate around the z-axis in radians per second.
### Initializers
- [init()](gcrotationrate/init.md)
  Creates a rotation rate structure.
- [init(x: Double, y: Double, z: Double)](gcrotationrate/init(x:y:z:).md)
  Creates a rotation rate structure with the specified values.

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
- [struct GCEulerAngles](gceulerangles.md)
  A structure that specifies the controller’s attitude as a series of rotations around the x, y, and z axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcrotationrate)*