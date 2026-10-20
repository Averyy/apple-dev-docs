# init(meshDescriptor:offMeshConnections:configuration:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Asynchronously creates a NavigationMeshResource from a MeshDescriptor. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection] = [], configuration: NavigationMeshResource.Configuration) async throws
```

**Other overloads**:

```swift
convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection] = [], configuration: NavigationMeshResource.Configuration) throws
```

## See Also

### Creating a navigation mesh
- [convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](./init%28mesh,offmeshconnections,configuration%29-6xdta.md)
  Creates a NavigationMeshResource from a MeshResource. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](./init%28mesh,offmeshconnections,configuration%29-7mj9i.md)
  Asynchronously creates a NavigationMeshResource from a MeshResource. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](./init%28meshdescriptor,offmeshconnections,configuration%29-3n43t.md)
  Creates a NavigationMeshResource from a MeshDescriptor. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](./init%28triangleindices,vertices,offmeshconnections,configuration%29-2rrq1.md)
  Creates a NavigationMeshResource from triangle indices and vertices. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](./init%28triangleindices,vertices,offmeshconnections,configuration%29-480i3.md)
  Asynchronously creates a NavigationMeshResource from triangle indices and vertices. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(polygonIndices: [[Int]], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration, areas: [NavigationMeshResource.Area], flags: [[NavigationMeshResource.Flag]], heightData: NavigationMeshResource.HeightData) throws](./init%28polygonindices,vertices,offmeshconnections,configuration,areas,flags,heightdata%29.md)
  Creates a NavigationMeshResource through existing Navigation Mesh data. This will not regenerate the Navigation Mesh. It will copy and save the input data to create a Navigation Mesh with this information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/init(meshdescriptor:offmeshconnections:configuration:)-6zzvf)*