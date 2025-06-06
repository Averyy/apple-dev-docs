# attitude

**Framework**: Game Controller  
**Kind**: property

The attitude of the controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var attitude: GCQuaternion { get }
```

#### Discussion

The  is the orientation of a body relative to the controller’s reference frame.

## See Also

- [struct GCQuaternion](gcquaternion.md)
  A quaternion that represents a controller’s measurement of attitude.
- [var rotationRate: GCRotationRate](gcmotion/rotationrate.md)
  The rotation rate of the controller.
- [struct GCRotationRate](gcrotationrate.md)
  A structure that represents rotation rates around the x, y, and z axes.
- [struct GCEulerAngles](gceulerangles.md)
  A structure that specifies the controller’s attitude as a series of rotations around the x, y, and z axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmotion/attitude)*