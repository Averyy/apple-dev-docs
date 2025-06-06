# CMQuaternion

**Framework**: Core Motion  
**Kind**: struct

The type for a quaternion representing a measurement of attitude.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CMQuaternion
```

#### Overview

A quaternion offers a way to parameterize attitude. If `q` is an instance of `CMQuaternion`, mathematically it represents the following unit quaternion: `q.x*i + q.y*j + q.z*k + q.w`. A unit quaternion represents a rotation of theta radians about the unit vector `{x,y,z}`, and `{q.x, q.y, q.z, q.w}` satisfies the following:

```objc
q.x = x * sin(theta / 2)
q.y = y * sin(theta / 2)
q.z = z * sin(theta / 2)
q.w = cos(theta / 2)
```

## Topics

### Initializing the Quaternion
- [init()](cmquaternion/init.md)
- [init(x: Double, y: Double, z: Double, w: Double)](cmquaternion/init(x:y:z:w:).md)
### Getting the Quaternion Values
- [var w: Double](cmquaternion/w.md)
  The value for the w axis.
- [var x: Double](cmquaternion/x.md)
  The value for the x axis.
- [var y: Double](cmquaternion/y.md)
  The value for the y axis.
- [var z: Double](cmquaternion/z.md)
  The value for the z axis.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var quaternion: CMQuaternion](cmattitude/quaternion.md)
  Returns a quaternion representing the device’s attitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmquaternion)*