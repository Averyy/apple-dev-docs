# quaternion

**Framework**: Spatial  
**Kind**: property

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

## See Also

- [var angle: Angle2D](rotation3d/angle.md)
  The angle of the rotation.
- [var axis: RotationAxis3D](rotation3d/axis.md)
  The axis of the rotation.
- [func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles](rotation3d/eulerangles(order:).md)
  Returns a rotation’s Euler angles.
- [struct EulerAngles](eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var vector: simd_double4](rotation3d/vector.md)
  The underlying vector of the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/quaternion)*