# SPRotation3DMakeLookAt

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Creates a rotation structure that’s the look-at direction from a position to a target.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPRotation3D SPRotation3DMakeLookAt(SPPoint3D position, SPPoint3D target, SPVector3D up);
```

## See Also

### Creating a 3D rotation structure
- [init(eulerAngles: EulerAngles)](./rotation3d/init%28eulerangles%29.md)
  Creates a rotation structure with the specified Euler angles.
- [init(eulerAngles: EulerAngles)](./rotation3d/init%28eulerangles%29.md)
  Creates a rotation structure with the specified Euler angles.
- [struct EulerAngles](./eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [init(angle: Angle2D, axis: RotationAxis3D)](./rotation3d/init%28angle,axis%29.md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(forward: Vector3D, up: Vector3D)](./rotation3d/init%28forward,up%29.md)
  Creates a rotation with the specified forward and up vectors.
- [SPRotation3DMakeWithQuaternion](./sprotation3dmakewithquaternion.md)
- [SPRotation3DMake](./sprotation3dmake-2i9jt.md)
  Creates a rotation structure.
- [SPRotation3DMakeLookAt](./sprotation3dmakelookat-4xrh6.md)
- [init(forward: Vector3D, up: Vector3D)](./rotation3d/init%28forward,up%29.md)
  Creates a rotation with the specified forward and up vectors.
- [SPRotationAxis3DMakeWithVector](./sprotationaxis3dmakewithvector-1n9ib.md)
  Creates a rotation axis from the specified double-precision vector.
- [SPRotationAxis3DMakeWithVector](./sprotationaxis3dmakewithvector-kk1p.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3dmakelookat-6ypo8)*