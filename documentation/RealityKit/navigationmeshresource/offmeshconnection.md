# NavigationMeshResource.OffMeshConnection

**Framework**: RealityKit  
**Kind**: struct

A container for the data associated with an off-mesh connection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct OffMeshConnection
```

## Topics

### Creating a connection
- [init(startPoint: SIMD3<Float>, endPoint: SIMD3<Float>, radius: Float, isBidirectional: Bool, label: String)](navigationmeshresource/offmeshconnection/init(startpoint:endpoint:radius:isbidirectional:label:).md)
### Defining the path
- [var startPoint: SIMD3<Float>](navigationmeshresource/offmeshconnection/startpoint.md)
  The start point of the off-mesh connection.
- [var endPoint: SIMD3<Float>](navigationmeshresource/offmeshconnection/endpoint.md)
  The end point of the off-mesh connection.
- [var isBidirectional: Bool](navigationmeshresource/offmeshconnection/isbidirectional.md)
  Whether the connection is bidirectional. If false, pathfinds will only allow going from startPoint to endPoint. If true, pathfinds will allow going in both directions.
### Instance Properties
- [var label: String](navigationmeshresource/offmeshconnection/label.md)
  The label on the connection for other systems to know what type of movement should occur here.
- [var radius: Float](navigationmeshresource/offmeshconnection/radius.md)
  The distance to the connection that counts as being close enough to use it.

## See Also

- [NavigationMeshResource.Configuration](navigationmeshresource/configuration-swift.struct.md)
  The NavigationMeshResource configuration that defines how the mesh is created.
- [NavigationMeshResource.Area](navigationmeshresource/area.md)
  An identifier for different areas on a Navigation Mesh.
- [NavigationMeshResource.Flag](navigationmeshresource/flag.md)
  An identifier for different flags on a Navigation Mesh.
- [NavigationMeshResource.FlagGroup](navigationmeshresource/flaggroup.md)
  A collection of Flags.
- [NavigationMeshResource.HeightData](navigationmeshresource/heightdata-swift.struct.md)
  A container for the detailed height data of the NavigationMeshResource.
- [NavigationMeshResource.Layer](navigationmeshresource/layer-swift.struct.md)
  An identifier for a Navigation Mesh, used by a [`NavigationComponent`](navigationcomponent.md) to select a specific Navigation Mesh for pathfinding.
- [NavigationMeshResource.PathNode](navigationmeshresource/pathnode.md)
  A container for the path node data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/offmeshconnection)*