# NavigationMeshResource.HeightData

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A container for the detailed height data of the NavigationMeshResource.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct HeightData
```

## Topics

### Creating height data
- [init(vertices: [SIMD3<Float>], triangleIndices: [[Int]], polygonTriangleIndices: [Int])](./heightdata-swift.struct/init%28vertices,triangleindices,polygontriangleindices%29.md)
### Accessing mesh geometry
- [var vertices: [SIMD3<Float>]](./heightdata-swift.struct/vertices.md)
  The vertices of the detailed height data mesh.
- [var triangleIndices: [[Int]]](./heightdata-swift.struct/triangleindices.md)
  The triangle indices of the detailed height data mesh.
- [var polygonTriangleIndices: [Int]](./heightdata-swift.struct/polygontriangleindices.md)
  The groups of triangles that make up a polygon in the detailed height data mesh, used to get the corresponding triangles for a given polygon in the generated Navigation Mesh.

## See Also

### Supporting types
- [NavigationMeshResource.Configuration](./configuration-swift.struct.md)
  The NavigationMeshResource configuration that defines how the mesh is created.
- [NavigationMeshResource.Area](./area.md)
  An identifier for different areas on a Navigation Mesh.
- [NavigationMeshResource.Flag](./flag.md)
  An identifier for different flags on a Navigation Mesh.
- [NavigationMeshResource.FlagGroup](./flaggroup.md)
  A collection of Flags.
- [NavigationMeshResource.OffMeshConnection](./offmeshconnection.md)
  A container for the data associated with an off-mesh connection.
- [NavigationMeshResource.Layer](./layer-swift.struct.md)
  An identifier for a Navigation Mesh, used by a [`NavigationComponent`](../navigationcomponent.md) to select a specific Navigation Mesh for pathfinding.
- [NavigationMeshResource.PathNode](./pathnode.md)
  A container for the path node data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/heightdata-swift.struct)*