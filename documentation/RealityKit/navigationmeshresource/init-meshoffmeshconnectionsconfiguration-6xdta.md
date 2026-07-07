# init(mesh:offMeshConnections:configuration:)

**Framework**: RealityKit  
**Kind**: init

Creates a NavigationMeshResource from a MeshResource. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection] = [], configuration: NavigationMeshResource.Configuration) throws
```

## See Also

- [convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](navigationmeshresource/init(mesh:offmeshconnections:configuration:)-7mj9i.md)
  Asynchronously creates a NavigationMeshResource from a MeshResource. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](navigationmeshresource/init(meshdescriptor:offmeshconnections:configuration:)-3n43t.md)
  Creates a NavigationMeshResource from a MeshDescriptor. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](navigationmeshresource/init(meshdescriptor:offmeshconnections:configuration:)-6zzvf.md)
  Asynchronously creates a NavigationMeshResource from a MeshDescriptor. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](navigationmeshresource/init(triangleindices:vertices:offmeshconnections:configuration:)-2rrq1.md)
  Creates a NavigationMeshResource from triangle indices and vertices. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](navigationmeshresource/init(triangleindices:vertices:offmeshconnections:configuration:)-480i3.md)
  Asynchronously creates a NavigationMeshResource from triangle indices and vertices. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(polygonIndices: [[Int]], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration, areas: [NavigationMeshResource.Area], flags: [[NavigationMeshResource.Flag]], heightData: NavigationMeshResource.HeightData) throws](navigationmeshresource/init(polygonindices:vertices:offmeshconnections:configuration:areas:flags:heightdata:).md)
  Creates a NavigationMeshResource through existing Navigation Mesh data. This will not regenerate the Navigation Mesh. It will copy and save the input data to create a Navigation Mesh with this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/init(mesh:offmeshconnections:configuration:)-6xdta)*