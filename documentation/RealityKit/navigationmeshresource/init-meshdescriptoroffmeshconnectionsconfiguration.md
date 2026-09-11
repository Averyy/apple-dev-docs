# init(meshDescriptor:offMeshConnections:configuration:)

**Framework**: RealityKit  
**Kind**: init

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/init(meshdescriptor:offmeshconnections:configuration:))*