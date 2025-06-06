# EulerAngles

**Framework**: Spatial  
**Kind**: struct

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

## Topics

### Initializers
- [init()](eulerangles/init.md)
  Creates a new Euler angles structure.
- [init(angles: simd_float3, order: EulerAngles.Order)](eulerangles/init(angles:order:)-44rv1.md)
  Creates a new Euler angles structure from the specified single-precision angles and order.
- [init(angles: simd_double3, order: __SPEulerAngleOrder)](eulerangles/init(angles:order:)-93mu1.md)
  Creates a new Euler angles structure from the specified double-precision angles and order.
- [init(x: Angle2D, y: Angle2D, z: Angle2D, order: EulerAngles.Order)](eulerangles/init(x:y:z:order:).md)
  Creates a new Euler angles structure from the specified angle structures and order.
- [init(Angle2D, Angle2D, Angle2D, order: EulerAngles.Order)](eulerangles/init(_:_:_:order:).md)
  Creates a new Euler angles structure from the specified angle structures and order.
### Instance properties
- [var angles: simd_double3](eulerangles/angles.md)
  A three-element vector that specifies the Euler angles.
- [var order: __SPEulerAngleOrder](eulerangles/order-swift.property.md)
  The Euler angle order.
- [var angles: simd_double3](eulerangles/angles.md)
  A three-element vector that specifies the Euler angles.
- [var order: __SPEulerAngleOrder](eulerangles/order-swift.property.md)
  The Euler angle order.
### Supporting types
- [EulerAngles.Order](eulerangles/order-swift.typealias.md)
  A type that specifies the order of the angles.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init()](rotation3d/init-2uz53.md)
  Creates a rotation.
- [init()](rotation3d/init-krpj.md)
  Creates a rotation structure.
- [init(eulerAngles: EulerAngles)](rotation3d/init(eulerangles:).md)
  Creates a rotation structure with the specified Euler angles.
- [init(eulerAngles: EulerAngles)](rotation3d/init(eulerangles:).md)
  Creates a rotation structure with the specified Euler angles.
- [init(quaternion: simd_quatd)](rotation3d/init(quaternion:)-2c79y.md)
  Creates a rotation axis from the specified double-precision quaternion.
- [init(simd_quatd)](rotation3d/init(_:)-8z2bn.md)
  Creates a rotation from the specified double-precision quaternion.
- [init(simd_quatf)](rotation3d/init(_:)-829qb.md)
  Creates a rotation axis from the specified single-precision quaternion.
- [init(angle: Angle2D, axis: RotationAxis3D)](rotation3d/init(angle:axis:).md)
  Creates a rotation structure with the specified axis and the specified angle from Spatial structures.
- [init(position: Point3D, target: Point3D, up: Vector3D)](rotation3d/init(position:target:up:).md)
  Creates a rotation structure that represents the look-at direction from a position to a target.
- [init(forward: Vector3D)](rotation3d/init(forward:).md)
  Creates a rotation with the specified forward vector.
- [init(forward: Vector3D, up: Vector3D)](rotation3d/init(forward:up:).md)
  Creates a rotation with the specified forward and up vectors.
- [init(forward: Vector3D, up: Vector3D)](rotation3d/init(forward:up:).md)
  Creates a rotation with the specified forward and up vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/eulerangles)*