# angle

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

The angle of the rotation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
var angle: Angle2D { get set }
```

## See Also

### Inspecting a 3D rotation’s properties
- [var axis: RotationAxis3D](./axis.md)
  The axis of the rotation.
- [func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles](./eulerangles%28order%29.md)
  Returns a rotation’s Euler angles.
- [struct EulerAngles](../eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var quaternion: simd_quatd](./quaternion.md)
  A quaternion that represents the rotation.
- [var vector: simd_double4](./vector.md)
  The underlying vector of the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/angle)*