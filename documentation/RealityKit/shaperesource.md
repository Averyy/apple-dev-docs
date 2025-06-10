# ShapeResource

**Framework**: RealityKit  
**Kind**: class

A representation of a shape.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class ShapeResource
```

## Topics

### Transforming a shape
- [func offsetBy(rotation: simd_quatf) -> ShapeResource](shaperesource/offsetby(rotation:).md)
  Creates a new shape resource by applying a rotation.
- [func offsetBy(translation: SIMD3<Float>) -> ShapeResource](shaperesource/offsetby(translation:).md)
  Creates a new shape resource by applying a translation.
- [func offsetBy(rotation: simd_quatf, translation: SIMD3<Float>) -> ShapeResource](shaperesource/offsetby(rotation:translation:).md)
  Creates a new shape resource by applying a rotation and a translation.
### Generating boxes
- [static func generateBox(size: SIMD3<Float>) -> ShapeResource](shaperesource/generatebox(size:).md)
  Creates a box shape with the specified extent.
- [static func generateBox(width: Float, height: Float, depth: Float) -> ShapeResource](shaperesource/generatebox(width:height:depth:).md)
  Creates a box shape with the specified dimensions.
### Generating spheres
- [static func generateSphere(radius: Float) -> ShapeResource](shaperesource/generatesphere(radius:).md)
  Creates a sphere shape with the specified radius.
### Generating capsules
- [static func generateCapsule(height: Float, radius: Float) -> ShapeResource](shaperesource/generatecapsule(height:radius:).md)
  Creates a capsule shape with the specified height and radius.
### Generating convex shapes
- [static func generateConvex(from: [SIMD3<Float>]) -> ShapeResource](shaperesource/generateconvex(from:)-6q0wj.md)
  Creates a convex shape from the given points.
- [static func generateConvex(from: MeshResource) -> ShapeResource](shaperesource/generateconvex(from:)-53jm9.md)
  Creates a convex shape from the given mesh.
### Comparing shapes
- [static func == (ShapeResource, ShapeResource) -> Bool](shaperesource/==(_:_:).md)
  Indicates whether two shapes are equal.
- [func hash(into: inout Hasher)](shaperesource/hash(into:).md)
  Hashes the essential components of the shape by feeding them into the given hash function.
### Instance Properties
- [var bounds: BoundingBox](shaperesource/bounds.md)
  Axis aligned bounding box in world space.
### Type Methods
- [static generateConvex(from:)](shaperesource/generateconvex(from:).md)
  Creates a convex shape from the given mesh.
- [static generateStaticMesh(from:)](shaperesource/generatestaticmesh(from:).md)
  Creates a static collision mesh from a mesh resource.
- [static generateStaticMesh(positions:faceIndices:)](shaperesource/generatestaticmesh(positions:faceindices:).md)
  Creates a static collision mesh from an array of vertex positions and face indices.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Simulating physics with collisions in your visionOS app](simulating-physics-with-collisions-in-your-visionos-app.md)
  Create entities that behave and react like physical objects in a RealityKit view.
- [Configuring Collision in RealityKit](configuring-collision-in-realitykit.md)
  Use collision groups and collision filters to control which objects collide.
- [struct CollisionComponent](collisioncomponent.md)
  A component that gives an entity the ability to collide with other entities that also have collision components.
- [CollisionComponent.Mode](collisioncomponent/mode-swift.enum.md)
  A mode that dictates how much collision data is collected for a given entity.
- [enum ShapeResourceError](shaperesourceerror.md)
- [struct CollisionGroup](collisiongroup.md)
  A bitmask used to define the collision group to which an entity belongs.
- [struct CollisionFilter](collisionfilter.md)
  A set of masks that determine whether entities can collide during simulations.
- [class TriggerVolume](triggervolume.md)
  An invisible 3D shape that detects when objects enter or exit a given region of space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource)*