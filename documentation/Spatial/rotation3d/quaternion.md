# quaternion

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

A quaternion that represents the rotation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var quaternion: simd_quatd { get set }
```

```c
simd_quatd quaternion;
```

## See Also

### Inspecting a 3D rotation’s properties
- [var angle: Angle2D](./angle.md)
  The angle of the rotation.
- [var axis: RotationAxis3D](./axis.md)
  The axis of the rotation.
- [func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles](./eulerangles%28order%29.md)
  Returns a rotation’s Euler angles.
- [struct EulerAngles](../eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var vector: simd_double4](./vector.md)
  The underlying vector of the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/quaternion)*