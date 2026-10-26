# SPRotationAxis3DGetVector

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

A simd three-element vector that contains the x-, y-, and z-coordinate values.

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
static simd_double3 SPRotationAxis3DGetVector(SPRotationAxis3D axis);
```

## See Also

### Inspecting a 3D rotation’s properties
- [func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles](./rotation3d/eulerangles%28order%29.md)
  Returns a rotation’s Euler angles.
- [SPRotation3DGetAngle](./sprotation3dgetangle.md)
  The angle of the rotation.
- [SPRotation3DGetAxis](./sprotation3dgetaxis.md)
  The axis of the rotation.
- [struct EulerAngles](./eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var quaternion: simd_quatd](./rotation3d/quaternion.md)
  A quaternion that represents the rotation.
- [vector](./sprotation3d/vector.md)
  The underlying vector of the rotation.
- [SPRotation3DGetQuaternion](./sprotation3dgetquaternion.md)
  A quaternion that represents the rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotationaxis3dgetvector)*