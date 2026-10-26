# vector

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

The underlying vector of the rotation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
simd_double4 vector;
```

## See Also

### Inspecting a 3D rotation’s properties
- [func eulerAngles(order: __SPEulerAngleOrder) -> EulerAngles](../rotation3d/eulerangles%28order%29.md)
  Returns a rotation’s Euler angles.
- [SPRotation3DGetAngle](../sprotation3dgetangle.md)
  The angle of the rotation.
- [SPRotation3DGetAxis](../sprotation3dgetaxis.md)
  The axis of the rotation.
- [struct EulerAngles](../eulerangles.md)
  A vector that represents three Euler angles and specifies the angle ordering.
- [var quaternion: simd_quatd](../rotation3d/quaternion.md)
  A quaternion that represents the rotation.
- [SPRotation3DGetQuaternion](../sprotation3dgetquaternion.md)
  A quaternion that represents the rotation.
- [SPRotationAxis3DGetVector](../sprotationaxis3dgetvector.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprotation3d/vector)*