# EulerAngles

**Framework**: Spatial  
**Kind**: struct  
**Role**: Structure

A vector that represents three Euler angles and specifies the angle ordering.

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
struct EulerAngles
```

```c
typedef struct { ... } SPEulerAngles;
```

## Topics

### Initializers
- [init()](./eulerangles/init%28%29.md)
  Creates a new Euler angles structure.
- [init(angles: simd_float3, order: EulerAngles.Order)](./eulerangles/init%28angles,order%29-44rv1.md)
  Creates a new Euler angles structure from the specified single-precision angles and order.
- [init(angles: simd_double3, order: __SPEulerAngleOrder)](./eulerangles/init%28angles,order%29-93mu1.md)
  Creates a new Euler angles structure from the specified double-precision angles and order.
- [init(x: Angle2D, y: Angle2D, z: Angle2D, order: EulerAngles.Order)](./eulerangles/init%28x,y,z,order%29.md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](./eulerangles/init%28_,_,_,order%29.md)
  Creates a new Euler angles structure from the specified angle structures and order.
### Instance properties
- [var angles: simd_double3](./eulerangles/angles.md)
  A three-element vector that specifies the Euler angles.
- [var order: __SPEulerAngleOrder](./eulerangles/order-swift.property.md)
  The Euler angle order.
- [var angles: simd_double3](./eulerangles/angles.md)
  A three-element vector that specifies the Euler angles.
- [var order: __SPEulerAngleOrder](./eulerangles/order-swift.property.md)
  The Euler angle order.
### Supporting types
- [EulerAngles.Order](./eulerangles/order-swift.typealias.md)
  A type that specifies the order of the angles.
- [SPEulerAngleOrder](./speulerangleorder.md)
  Constants that describe the order of Euler angles.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Creating a 3D rotation structure
- [init()](./rotation3d/init%28%29-2uz53.md)
  Creates a rotation.
- [init()](./rotation3d/init%28%29-krpj.md)
  Creates a rotation structure.
- [init(eulerAngles: EulerAngles)](./rotation3d/init%28eulerangles%29.md)
  Creates a rotation structure with the specified Euler angles.
- [init(eulerAngles: EulerAngles)](./rotation3d/init%28eulerangles%29.md)
  Creates a rotation structure with the specified Euler angles.
- [init(quaternion: simd_quatd)](./rotation3d/init%28quaternion%29-2c79y.md)
  Creates a rotation axis from the specified double-precision quaternion.
- [init(simd_quatd)](./rotation3d/init%28_%29-8z2bn.md)
  Creates a rotation from the specified double-precision quaternion.
- [init(simd_quatf)](./rotation3d/init%28_%29-829qb.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [init(angle: Angle2D, axis: RotationAxis3D)](./rotation3d/init%28angle,axis%29.md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(position: Point3D, target: Point3D, up: Vector3D)](./rotation3d/init%28position,target,up%29.md)
  Creates a rotation structure that represents the look-at direction from a position to a target.
- [init(forward: Vector3D)](./rotation3d/init%28forward%29.md)
  Creates a rotation with the specified forward vector.
- [init(forward: Vector3D, up: Vector3D)](./rotation3d/init%28forward,up%29.md)
  Creates a rotation with the specified forward and up vectors.
- [init(forward: Vector3D, up: Vector3D)](./rotation3d/init%28forward,up%29.md)
  Creates a rotation with the specified forward and up vectors.
- [SPRotation3DMakeWithQuaternion](./sprotation3dmakewithquaternion.md)
- [SPRotation3DMake](./sprotation3dmake-2i9jt.md)
  Creates a rotation structure.
- [SPRotation3DMakeLookAt](./sprotation3dmakelookat-6ypo8.md)
  Creates a rotation structure that’s the look-at direction from a position to a target.
- [SPRotation3DMakeLookAt](./sprotation3dmakelookat-4xrh6.md)
- [SPRotationAxis3DMakeWithVector](./sprotationaxis3dmakewithvector-1n9ib.md)
  Creates a rotation axis from the specified double-precision vector.
- [SPRotationAxis3DMakeWithVector](./sprotationaxis3dmakewithvector-kk1p.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/eulerangles)*