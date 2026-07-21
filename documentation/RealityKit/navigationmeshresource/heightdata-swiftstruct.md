# NavigationMeshResource.HeightData

**Framework**: RealityKit  
**Kind**: struct

A container for the detailed height data of the NavigationMeshResource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct HeightData
```

## Topics

### Creating height data
- [init(vertices: [SIMD3<Float>], triangleIndices: [[Int]], polygonTriangleIndices: [Int])](navigationmeshresource/heightdata-swift.struct/init(vertices:triangleindices:polygontriangleindices:).md)
### Accessing mesh geometry
- [var vertices: [SIMD3<Float>]](navigationmeshresource/heightdata-swift.struct/vertices.md)
  The vertices of the detailed height data mesh.
- [var triangleIndices: [[Int]]](navigationmeshresource/heightdata-swift.struct/triangleindices.md)
  The triangle indices of the detailed height data mesh.
- [var polygonTriangleIndices: [Int]](navigationmeshresource/heightdata-swift.struct/polygontriangleindices.md)
  The groups of triangles that make up a polygon in the detailed height data mesh, used to get the corresponding triangles for a given polygon in the generated Navigation Mesh.

## See Also

- [NavigationMeshResource.Configuration](navigationmeshresource/configuration-swift.struct.md)
  The NavigationMeshResource configuration that defines how the mesh is created.
- [NavigationMeshResource.Area](navigationmeshresource/area.md)
  An identifier for different areas on a Navigation Mesh.
- [NavigationMeshResource.Flag](navigationmeshresource/flag.md)
  An identifier for different flags on a Navigation Mesh.
- [NavigationMeshResource.FlagGroup](navigationmeshresource/flaggroup.md)
  A collection of Flags.
- [NavigationMeshResource.OffMeshConnection](navigationmeshresource/offmeshconnection.md)
  A container for the data associated with an off-mesh connection.
- [NavigationMeshResource.Layer](navigationmeshresource/layer-swift.struct.md)
  An identifier for a Navigation Mesh, used by a [`NavigationComponent`](navigationcomponent.md) to select a specific Navigation Mesh for pathfinding.
- [NavigationMeshResource.PathNode](navigationmeshresource/pathnode.md)
  A container for the path node data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/heightdata-swift.struct)*