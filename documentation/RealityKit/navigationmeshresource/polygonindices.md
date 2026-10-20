# polygonIndices

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The polygon indices of the generated Navigation Mesh. Polygons may have different numbers of vertices, so each entry in the list is a list of indices into the vertices array for that polygon.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var polygonIndices: [[Int]] { get }
```

## See Also

### Accessing mesh data
- [var vertices: [SIMD3<Float>]](./vertices.md)
  The vertices of the generated Navigation Mesh.
- [var areas: [NavigationMeshResource.Area]](./areas.md)
  The areas associated with each polygon in the generated Navigation Mesh.
- [var flags: [[NavigationMeshResource.Flag]]](./flags.md)
  The flags associated with each polygon in the generated Navigation Mesh.
- [var offMeshConnections: [NavigationMeshResource.OffMeshConnection]](./offmeshconnections.md)
  The off-mesh connections of the generated Navigation Mesh.
- [var heightData: NavigationMeshResource.HeightData](./heightdata-swift.property.md)
  The detailed height data of the generated Navigation Mesh.
- [var layer: NavigationMeshResource.Layer?](./layer-swift.property.md)
  The identification of this NavigationMeshResource, used when entities are searching for a specific NavigationMeshResource in a scene.
- [var configuration: NavigationMeshResource.Configuration](./configuration-swift.property.md)
  The configuration this Navigation Mesh was created with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/polygonindices)*