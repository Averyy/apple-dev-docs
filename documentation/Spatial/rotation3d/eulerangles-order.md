# eulerAngles(order:)

**Framework**: Spatial  
**Kind**: method

Returns a rotation’s Euler angles.

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
func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles
```

#### Return Value

A structure that represents Euler angles and ordering.

## Parameters

- `order`: The Euler angle ordering.

## See Also

- [var angle: Angle2D](rotation3d/angle.md)
  The angle of the rotation.
- [var axis: RotationAxis3D](rotation3d/axis.md)
  The axis of the rotation.
- [struct EulerAngles](eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var quaternion: simd_quatd](rotation3d/quaternion.md)
  A quaternion that represents the rotation.
- [var vector: simd_double4](rotation3d/vector.md)
  The underlying vector of the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/eulerangles(order:))*