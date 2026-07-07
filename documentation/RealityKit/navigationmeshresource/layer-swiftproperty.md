# layer

**Framework**: RealityKit  
**Kind**: property

The identification of this NavigationMeshResource, used when entities are searching for a specific NavigationMeshResource in a scene.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var layer: NavigationMeshResource.Layer? { get set }
```

## See Also

- [var vertices: [SIMD3<Float>]](navigationmeshresource/vertices.md)
  The vertices of the generated Navigation Mesh.
- [var polygonIndices: [[Int]]](navigationmeshresource/polygonindices.md)
  The polygon indices of the generated Navigation Mesh. Polygons may have different numbers of vertices, so each entry in the list is a list of indices into the vertices array for that polygon.
- [var areas: [NavigationMeshResource.Area]](navigationmeshresource/areas.md)
  The areas associated with each polygon in the generated Navigation Mesh.
- [var flags: [[NavigationMeshResource.Flag]]](navigationmeshresource/flags.md)
  The flags associated with each polygon in the generated Navigation Mesh.
- [var offMeshConnections: [NavigationMeshResource.OffMeshConnection]](navigationmeshresource/offmeshconnections.md)
  The off-mesh connections of the generated Navigation Mesh.
- [var heightData: NavigationMeshResource.HeightData](navigationmeshresource/heightdata-swift.property.md)
  The detailed height data of the generated Navigation Mesh.
- [var configuration: NavigationMeshResource.Configuration](navigationmeshresource/configuration-swift.property.md)
  The configuration this Navigation Mesh was created with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/layer-swift.property)*