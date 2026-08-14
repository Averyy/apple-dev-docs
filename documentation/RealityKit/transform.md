# Transform

**Framework**: RealityKit  
**Kind**: struct

A component that defines the scale, rotation, and translation of an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@frozen
struct Transform
```

## Mentions

- [Automatically animating RealityKit entities](automatically-animating-realitykit-entities.md)

#### Overview

An entity acquires a [`Transform`](transform.md) component, as well as a set of methods for manipulating the transform, by adopting the [`HasTransform`](hastransform.md) protocol. This is true for all entities, because the [`Entity`](entity.md) base class adopts the protocol.

## Topics

### Creating a transform
- [init()](transform/init.md)
  Creates a transform with the values of the identity transform.
- [init(scale: SIMD3<Float>, rotation: simd_quatf, translation: SIMD3<Float>)](transform/init(scale:rotation:translation:).md)
  Creates a new transformation using the given values.
- [init(pitch: Float, yaw: Float, roll: Float)](transform/init(pitch:yaw:roll:).md)
  Creates a new transform from the specified Euler angles.
- [init(matrix: float4x4)](transform/init(matrix:).md)
  Creates a new transform represented as a 4x4 matrix.
### Setting transform properties
- [var scale: SIMD3<Float>](transform/scale.md)
  The scaling factor applied to the entity.
- [var rotation: simd_quatf](transform/rotation.md)
  The rotation of the entity specified as a unit quaternion.
- [var translation: SIMD3<Float>](transform/translation.md)
  The position of the entity along the x, y, and z axes.
- [var matrix: float4x4](transform/matrix.md)
  The transform represented as a 4x4 matrix.
### Getting the identity transform
- [static let identity: Transform](transform/identity.md)
  The identity transform.
### Initializers
- [init(AffineTransform3D)](transform/init(_:).md)
- [init(projectiveTransform:)](transform/init(projectivetransform:).md)
  A convenience initializer for the Transform Component that takes a `ProjectiveTransform3D`
### Instance Methods
- [func hash(into: inout Hasher)](transform/hash(into:).md)
  Hashes the essential components of the transform by feeding them into the given hash function.
### Default Implementations
- [ProjectiveTransformable3DFloat Implementations](transform/projectivetransformable3dfloat-implementations.md)

## Relationships

### Conforms To
- [AnimatableData](animatabledata.md)
- [BindableData](bindabledata.md)
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Component](component.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [ProjectiveTransformable3D](../spatial/projectivetransformable3d.md)
- [ProjectiveTransformable3DFloat](../spatial/projectivetransformable3dfloat.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol HasTransform](hastransform.md)
  An interface that enables manipulating the scale, rotation, and translation of an entity.
- [func transformMatrix(relativeTo: Entity.CoordinateSpaceReference) -> float4x4?](entity/transformmatrix(relativeto:).md)
  Returns the 4 x 4 transform matrix of an entity relative to the given coordinate space.
- [Entity.CoordinateSpaceReference](entity/coordinatespacereference.md)
  Defines the coordinate space reference for transform conversion.
- [Entity.ForwardDirection](entity/forwarddirection.md)
  Defines the forward direction for an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/transform)*