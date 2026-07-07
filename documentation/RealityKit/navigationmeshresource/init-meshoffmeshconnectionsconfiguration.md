# init(mesh:offMeshConnections:configuration:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously creates a NavigationMeshResource from a MeshResource. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection] = [], configuration: NavigationMeshResource.Configuration) async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/init(mesh:offmeshconnections:configuration:))*