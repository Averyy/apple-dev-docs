# init(angle:axis:)

**Framework**: Spatial  
**Kind**: init

Creates a rotation structure with the specified axis and the specified angle from Spatial structures.

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
init(angle: Angle2D, axis: RotationAxis3D)
```

## Parameters

- `angle`: The rotation angle.
- `axis`: The rotation axis.

## See Also

- [init()](rotation3d/init-2uz53.md)
  Creates a rotation.
- [init()](rotation3d/init-krpj.md)
  Creates a rotation structure.
- [init(eulerAngles: EulerAngles)](rotation3d/init(eulerangles:).md)
  Creates a rotation structure with the specified Euler angles.
- [init(eulerAngles: EulerAngles)](rotation3d/init(eulerangles:).md)
  Creates a rotation structure with the specified Euler angles.
- [struct EulerAngles](eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [init(quaternion: simd_quatd)](rotation3d/init(quaternion:)-2c79y.md)
  Creates a rotation axis from the specified double-precision quaternion.
- [init(simd_quatd)](rotation3d/init(_:)-8z2bn.md)
  Creates a rotation from the specified double-precision quaternion.
- [init(simd_quatf)](rotation3d/init(_:)-829qb.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [init(position: Point3D, target: Point3D, up: Vector3D)](rotation3d/init(position:target:up:).md)
  Creates a rotation structure that represents the look-at direction from a position to a target.
- [init(forward: Vector3D)](rotation3d/init(forward:).md)
  Creates a rotation with the specified forward vector.
- [init(forward: Vector3D, up: Vector3D)](rotation3d/init(forward:up:).md)
  Creates a rotation with the specified forward and up vectors.
- [init(forward: Vector3D, up: Vector3D)](rotation3d/init(forward:up:).md)
  Creates a rotation with the specified forward and up vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/init(angle:axis:))*