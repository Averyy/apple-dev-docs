# init(triangleIndices:vertices:offMeshConnections:configuration:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously creates a NavigationMeshResource from triangle indices and vertices. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection] = [], configuration: NavigationMeshResource.Configuration) async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/init(triangleindices:vertices:offmeshconnections:configuration:))*