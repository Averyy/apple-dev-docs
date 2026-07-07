# ClothMeshResource

**Framework**: RealityKit  
**Kind**: class

A mesh resource that defines the topology and shape of a cloth body or a mesh-shaped cloth collider.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class ClothMeshResource
```

#### Overview

Use this resource as the mesh for a [`mesh`](clothbodycomponent/mesh.md) or a [`mesh`](clothmeshshape/mesh.md).

## Topics

### Creating a cloth mesh
- [convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32]) throws](clothmeshresource/init(positions:triangleindices:).md)
  Creates a cloth mesh resource from the given vertex positions and triangle indices.
- [static func patch(size: SIMD2<Float>, targetEdgeLength: Float) throws -> Self](clothmeshresource/patch(size:targetedgelength:).md)
  Creates a rectangular patch mesh with a topology suitable for cloth simulation.
- [static func box(size: SIMD3<Float>, targetEdgeLength: Float) throws -> Self](clothmeshresource/box(size:targetedgelength:).md)
  Creates a box mesh with a topology suitable for cloth simulation.
- [static func sphere(radius: Float, targetEdgeLength: Float) throws -> Self](clothmeshresource/sphere(radius:targetedgelength:).md)
  Creates a sphere mesh with a topology suitable for cloth simulation.
- [static func capsule(height: Float, radius: Float, targetEdgeLength: Float) throws -> Self](clothmeshresource/capsule(height:radius:targetedgelength:).md)
  Creates a capsule mesh with a topology suitable for cloth simulation.
- [static func cylinder(height: Float, radius: Float, withCaps: Bool, targetEdgeLength: Float) throws -> Self](clothmeshresource/cylinder(height:radius:withcaps:targetedgelength:).md)
  Creates a cylinder mesh with a topology suitable for cloth simulation.
- [static let defaultTargetEdgeLength: Float](clothmeshresource/defaulttargetedgelength.md)
  Default target edge length for mesh generation.
### Accessing vertex data
- [var vertexCount: Int](clothmeshresource/vertexcount.md)
  The number of vertices in the mesh.
- [var positions: Span<SIMD3<Float>>](clothmeshresource/positions.md)
  The positions of all the vertices.
- [func position(at: UInt32) -> SIMD3<Float>](clothmeshresource/position(at:).md)
  Returns the position of the vertex at the given index.
- [func withPositions<Result>((Span<SIMD3<Float>>) -> Result) -> Result](clothmeshresource/withpositions(_:).md)
  Provides access to the positions of all the vertices within a callback.
- [func vertexIndex(at: UInt32) -> UInt32](clothmeshresource/vertexindex(at:).md)
  Returns the vertex index at the given position in the mesh’s flattened primitive index array.
- [func vertexIndex(primitive: UInt32, vertex: UInt32) -> UInt32](clothmeshresource/vertexindex(primitive:vertex:).md)
  Returns the vertex index of the specified vertex within the specified primitive.
- [func vertices(in: ClothVolumeShape, center: SIMD3<Float>, orientation: simd_quatf) -> [UInt32]](clothmeshresource/vertices(in:center:orientation:).md)
  Returns the indices of the vertices that lie inside the given volume shape.
### Inspecting mesh geometry
- [var isWatertight: Bool](clothmeshresource/iswatertight.md)
  Indicates whether the mesh is “watertight”.
- [var volume: Float?](clothmeshresource/volume.md)
  The volume of the mesh, or `nil` if the mesh is not watertight.
### Initializers
- [convenience init(from: MeshResource) throws](clothmeshresource/init(from:).md)
  Creates a cloth mesh resource from a rendering mesh resource.
### Instance Properties
- [var indexCount: Int](clothmeshresource/indexcount.md)
  The number of indices in the mesh.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ClothPoseResource](clothposeresource.md)
  A resource that defines a set of vertex positions for a cloth body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothmeshresource)*