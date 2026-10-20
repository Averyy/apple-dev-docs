# ShapeResource

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A representation of a shape.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency class ShapeResource
```

## Topics

### Transforming a shape
- [func offsetBy(rotation: simd_quatf) -> ShapeResource](./shaperesource/offsetby%28rotation%29.md)
  Creates a new shape resource by applying a rotation.
- [func offsetBy(translation: SIMD3<Float>) -> ShapeResource](./shaperesource/offsetby%28translation%29.md)
  Creates a new shape resource by applying a translation.
- [func offsetBy(rotation: simd_quatf, translation: SIMD3<Float>) -> ShapeResource](./shaperesource/offsetby%28rotation,translation%29.md)
  Creates a new shape resource by applying a rotation and a translation.
### Generating boxes
- [static func generateBox(size: SIMD3<Float>) -> ShapeResource](./shaperesource/generatebox%28size%29.md)
  Creates a box shape with the specified extent.
- [static func generateBox(width: Float, height: Float, depth: Float) -> ShapeResource](./shaperesource/generatebox%28width,height,depth%29.md)
  Creates a box shape with the specified dimensions.
### Generating spheres
- [static func generateSphere(radius: Float) -> ShapeResource](./shaperesource/generatesphere%28radius%29.md)
  Creates a sphere shape with the specified radius.
### Generating capsules
- [static func generateCapsule(height: Float, radius: Float) -> ShapeResource](./shaperesource/generatecapsule%28height,radius%29.md)
  Creates a capsule shape with the specified height and radius.
### Generating convex shapes
- [static func generateConvex(from: [SIMD3<Float>]) -> ShapeResource](./shaperesource/generateconvex%28from%29-6q0wj.md)
  Creates a convex shape from the given points.
- [static func generateConvex(from: MeshResource) -> ShapeResource](./shaperesource/generateconvex%28from%29-53jm9.md)
  Creates a convex shape from the given mesh.
### Operators
- [static func == (ShapeResource, ShapeResource) -> Bool](./shaperesource/eqeq%28_,_%29.md)
  Indicates whether two shapes are equal.
### Instance Properties
- [var bounds: BoundingBox](./shaperesource/bounds.md)
  Axis aligned bounding box in world space.
### Instance Methods
- [func hash(into: inout Hasher)](./shaperesource/hash%28into%29.md)
  Hashes the essential components of the shape by feeding them into the given hash function.
### Type Methods
- [static generateConvex(from:)](./shaperesource/generateconvex%28from%29.md)
  Creates a convex shape from the given mesh.
- [static generateStaticMesh(from:)](./shaperesource/generatestaticmesh%28from%29.md)
  Creates a static collision mesh from a mesh resource.
- [static func generateStaticMesh(positions: [SIMD3<Float>], faceIndices: [UInt16]) async throws -> ShapeResource](./shaperesource/generatestaticmesh%28positions,faceindices%29.md)
  Creates a static collision mesh from an array of vertex positions and face indices.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Resource](./resource.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Collision shapes and groups
- [Simulating physics with collisions in your visionOS app](./simulating-physics-with-collisions-in-your-visionos-app.md)
  Create entities that behave and react like physical objects in a RealityKit view.
- [Configuring Collision in RealityKit](./configuring-collision-in-realitykit.md)
  Use collision groups and collision filters to control which objects collide.
- [Creating an interactive 3D model in visionOS](../visionOS/creating-an-interactable-3d-model-in-visionos.md)
  Display an interactive car model using gestures in a reality view.
- [struct CollisionComponent](./collisioncomponent.md)
  A component that gives an entity the ability to collide with other entities that also have collision components.
- [CollisionComponent.Mode](./collisioncomponent/mode-swift.enum.md)
  A mode that dictates how much collision data is collected for a given entity.
- [enum ShapeResourceError](./shaperesourceerror.md)
- [struct CollisionGroup](./collisiongroup.md)
  A bitmask used to define the collision group to which an entity belongs.
- [struct CollisionFilter](./collisionfilter.md)
  A set of masks that determine whether entities can collide during simulations.
- [class TriggerVolume](./triggervolume.md)
  An invisible 3D shape that detects when objects enter or exit a given region of space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource)*