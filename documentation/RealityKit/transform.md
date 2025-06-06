# Transform

**Framework**: RealityKit  
**Kind**: struct

A component that defines the scale, rotation, and translation of an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@frozen
struct Transform
```

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
### Comparing transforms
- [static func == (Transform, Transform) -> Bool](transform/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](transform/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](transform/hash(into:).md)
  Hashes the essential components of the transform by feeding them into the given hash function.
- [var hashValue: Int](transform/hashvalue.md)
  The hash value.
### Registering a component type
- [static func registerComponent()](transform/registercomponent.md)
  Registers a new component type.
### Initializers
- [init(AffineTransform3D)](transform/init(_:).md)
### Default Implementations
- [Component Implementations](transform/component-implementations.md)
- [Decodable Implementations](transform/decodable-implementations.md)
- [Encodable Implementations](transform/encodable-implementations.md)
- [Equatable Implementations](transform/equatable-implementations.md)

## Relationships

### Conforms To
- [AnimatableData](animatabledata.md)
- [BindableData](bindabledata.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Component](component.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

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