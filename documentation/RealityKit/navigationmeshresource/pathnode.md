# NavigationMeshResource.PathNode

**Framework**: RealityKit  
**Kind**: struct

A container for the path node data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct PathNode
```

## Topics

### Creating a path node
- [init(position: SIMD3<Float>, category: NavigationMeshResource.PathNode.Category, label: String)](navigationmeshresource/pathnode/init(position:category:label:).md)
### Categorizing path nodes
- [var category: NavigationMeshResource.PathNode.Category](navigationmeshresource/pathnode/category-swift.property.md)
  The category of the node.
- [NavigationMeshResource.PathNode.Category](navigationmeshresource/pathnode/category-swift.enum.md)
  The categories of path nodes.
### Instance Properties
- [var label: String](navigationmeshresource/pathnode/label.md)
  The label of the node.
- [var position: SIMD3<Float>](navigationmeshresource/pathnode/position.md)
  The position of the node.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [NavigationMeshResource.HeightData](navigationmeshresource/heightdata-swift.struct.md)
  A container for the detailed height data of the NavigationMeshResource.
- [NavigationMeshResource.Layer](navigationmeshresource/layer-swift.struct.md)
  An identifier for a Navigation Mesh, used by a [`NavigationComponent`](navigationcomponent.md) to select a specific Navigation Mesh for pathfinding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/pathnode)*