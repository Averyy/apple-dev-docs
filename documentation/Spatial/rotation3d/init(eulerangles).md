# init(eulerAngles:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates a rotation structure with the specified Euler angles.

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
init(eulerAngles: EulerAngles)
```

```c
static SPRotation3D SPRotation3DMakeWithEulerAngles(SPEulerAngles eulerAngles);
```

## Parameters

- `eulerAngles`: A structure that specifies the order and values of the Euler angles.

## See Also

### Creating a 3D rotation structure
- [init()](./init%28%29-2uz53.md)
  Creates a rotation.
- [init()](./init%28%29-krpj.md)
  Creates a rotation structure.
- [struct EulerAngles](../eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [init(quaternion: simd_quatd)](./init%28quaternion%29-2c79y.md)
  Creates a rotation axis from the specified double-precision quaternion.
- [init(simd_quatd)](./init%28_%29-8z2bn.md)
  Creates a rotation from the specified double-precision quaternion.
- [init(simd_quatf)](./init%28_%29-829qb.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [init(angle: Angle2D, axis: RotationAxis3D)](./init%28angle,axis%29.md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(position: Point3D, target: Point3D, up: Vector3D)](./init%28position,target,up%29.md)
  Creates a rotation structure that represents the look-at direction from a position to a target.
- [init(forward: Vector3D)](./init%28forward%29.md)
  Creates a rotation with the specified forward vector.
- [init(forward: Vector3D, up: Vector3D)](./init%28forward,up%29.md)
  Creates a rotation with the specified forward and up vectors.
- [init(forward: Vector3D, up: Vector3D)](./init%28forward,up%29.md)
  Creates a rotation with the specified forward and up vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/init(eulerangles:))*