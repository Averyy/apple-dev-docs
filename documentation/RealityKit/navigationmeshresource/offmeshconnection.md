# NavigationMeshResource.OffMeshConnection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A container for the data associated with an off-mesh connection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct OffMeshConnection
```

## Topics

### Creating a connection
- [init(startPoint: SIMD3<Float>, endPoint: SIMD3<Float>, radius: Float, isBidirectional: Bool, label: String)](./offmeshconnection/init%28startpoint,endpoint,radius,isbidirectional,label%29.md)
### Defining the path
- [var startPoint: SIMD3<Float>](./offmeshconnection/startpoint.md)
  The start point of the off-mesh connection.
- [var endPoint: SIMD3<Float>](./offmeshconnection/endpoint.md)
  The end point of the off-mesh connection.
- [var isBidirectional: Bool](./offmeshconnection/isbidirectional.md)
  Whether the connection is bidirectional. If false, pathfinds will only allow going from startPoint to endPoint. If true, pathfinds will allow going in both directions.
### Instance Properties
- [var label: String](./offmeshconnection/label.md)
  The label on the connection for other systems to know what type of movement should occur here.
- [var radius: Float](./offmeshconnection/radius.md)
  The distance to the connection that counts as being close enough to use it.

## See Also

### Supporting types
- [NavigationMeshResource.Configuration](./configuration-swift.struct.md)
  The NavigationMeshResource configuration that defines how the mesh is created.
- [NavigationMeshResource.Area](./area.md)
  An identifier for different areas on a Navigation Mesh.
- [NavigationMeshResource.Flag](./flag.md)
  An identifier for different flags on a Navigation Mesh.
- [NavigationMeshResource.FlagGroup](./flaggroup.md)
  A collection of Flags.
- [NavigationMeshResource.HeightData](./heightdata-swift.struct.md)
  A container for the detailed height data of the NavigationMeshResource.
- [NavigationMeshResource.Layer](./layer-swift.struct.md)
  An identifier for a Navigation Mesh, used by a [`NavigationComponent`](../navigationcomponent.md) to select a specific Navigation Mesh for pathfinding.
- [NavigationMeshResource.PathNode](./pathnode.md)
  A container for the path node data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/offmeshconnection)*