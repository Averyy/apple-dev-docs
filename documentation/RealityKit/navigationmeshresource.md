# NavigationMeshResource

**Framework**: RealityKit  
**Kind**: class

A representation of a scene’s navigable surfaces that the system uses to compute paths.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class NavigationMeshResource
```

#### Overview

Build a navigation mesh from a model’s geometry or from raw vertex and polygon data, then mark areas and flags to describe where agents can travel and at what cost. Provide the resulting resource to a [`NavigationMeshComponent`](navigationmeshcomponent.md) so a [`NavigationController`](navigationcontroller.md) can find paths across it.

## Topics

### Creating a navigation mesh
- [convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](navigationmeshresource/init(mesh:offmeshconnections:configuration:)-6xdta.md)
- [convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](navigationmeshresource/init(mesh:offmeshconnections:configuration:)-7mj9i.md)
- [convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](navigationmeshresource/init(meshdescriptor:offmeshconnections:configuration:)-3n43t.md)
- [convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](navigationmeshresource/init(meshdescriptor:offmeshconnections:configuration:)-6zzvf.md)
- [init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](navigationmeshresource/init(triangleindices:vertices:offmeshconnections:configuration:)-2rrq1.md)
- [convenience init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](navigationmeshresource/init(triangleindices:vertices:offmeshconnections:configuration:)-480i3.md)
- [convenience init(polygonIndices: [[Int]], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration, areas: [NavigationMeshResource.Area], flags: [[NavigationMeshResource.Flag]], heightData: NavigationMeshResource.HeightData) throws](navigationmeshresource/init(polygonindices:vertices:offmeshconnections:configuration:areas:flags:heightdata:).md)
### Marking areas and flags
- [func markAreaInBox(boundingBox: BoundingBox, area: NavigationMeshResource.Area)](navigationmeshresource/markareainbox(boundingbox:area:).md)
- [func markFlagInBox(boundingBox: BoundingBox, flag: NavigationMeshResource.Flag)](navigationmeshresource/markflaginbox(boundingbox:flag:).md)
- [func markAreaInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, area: NavigationMeshResource.Area)](navigationmeshresource/markareaincylinder(position:radius:halfheight:area:).md)
- [func markFlagInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, flag: NavigationMeshResource.Flag)](navigationmeshresource/markflagincylinder(position:radius:halfheight:flag:).md)
- [func markAreaOnPolygons(polygonIndices: [Int], area: NavigationMeshResource.Area)](navigationmeshresource/markareaonpolygons(polygonindices:area:).md)
- [func markFlagOnPolygons(polygonIndices: [Int], flag: NavigationMeshResource.Flag)](navigationmeshresource/markflagonpolygons(polygonindices:flag:).md)
- [func markAreaOnOffMeshConnections(offMeshConnectionIndices: [Int], area: NavigationMeshResource.Area)](navigationmeshresource/markareaonoffmeshconnections(offmeshconnectionindices:area:).md)
- [func markFlagOnOffMeshConnections(offMeshConnectionIndices: [Int], flag: NavigationMeshResource.Flag)](navigationmeshresource/markflagonoffmeshconnections(offmeshconnectionindices:flag:).md)
### Removing areas and flags
- [func removeAreaInBox(boundingBox: BoundingBox, area: NavigationMeshResource.Area)](navigationmeshresource/removeareainbox(boundingbox:area:).md)
- [func removeFlagInBox(boundingBox: BoundingBox, flag: NavigationMeshResource.Flag)](navigationmeshresource/removeflaginbox(boundingbox:flag:).md)
- [func removeAreaInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, area: NavigationMeshResource.Area)](navigationmeshresource/removeareaincylinder(position:radius:halfheight:area:).md)
- [func removeFlagInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, flag: NavigationMeshResource.Flag)](navigationmeshresource/removeflagincylinder(position:radius:halfheight:flag:).md)
- [func removeAreaOnPolygons(polygonIndices: [Int], area: NavigationMeshResource.Area)](navigationmeshresource/removeareaonpolygons(polygonindices:area:).md)
- [func removeFlagOnPolygons(polygonIndices: [Int], flag: NavigationMeshResource.Flag)](navigationmeshresource/removeflagonpolygons(polygonindices:flag:).md)
- [func removeAreaOnOffMeshConnections(offMeshConnectionIndices: [Int], area: NavigationMeshResource.Area)](navigationmeshresource/removeareaonoffmeshconnections(offmeshconnectionindices:area:).md)
- [func removeFlagOnOffMeshConnections(offMeshConnectionIndices: [Int], flag: NavigationMeshResource.Flag)](navigationmeshresource/removeflagonoffmeshconnections(offmeshconnectionindices:flag:).md)
### Accessing mesh data
- [var vertices: [SIMD3<Float>]](navigationmeshresource/vertices.md)
- [var polygonIndices: [[Int]]](navigationmeshresource/polygonindices.md)
- [var areas: [NavigationMeshResource.Area]](navigationmeshresource/areas.md)
- [var flags: [[NavigationMeshResource.Flag]]](navigationmeshresource/flags.md)
- [var offMeshConnections: [NavigationMeshResource.OffMeshConnection]](navigationmeshresource/offmeshconnections.md)
- [var heightData: NavigationMeshResource.HeightData](navigationmeshresource/heightdata-swift.property.md)
- [var layer: NavigationMeshResource.Layer?](navigationmeshresource/layer-swift.property.md)
- [var configuration: NavigationMeshResource.Configuration](navigationmeshresource/configuration-swift.property.md)
### Supporting types
- [NavigationMeshResource.Configuration](navigationmeshresource/configuration-swift.struct.md)
- [NavigationMeshResource.Area](navigationmeshresource/area.md)
- [NavigationMeshResource.Flag](navigationmeshresource/flag.md)
- [NavigationMeshResource.FlagGroup](navigationmeshresource/flaggroup.md)
- [NavigationMeshResource.OffMeshConnection](navigationmeshresource/offmeshconnection.md)
- [NavigationMeshResource.HeightData](navigationmeshresource/heightdata-swift.struct.md)
- [NavigationMeshResource.Layer](navigationmeshresource/layer-swift.struct.md)
- [NavigationMeshResource.PathNode](navigationmeshresource/pathnode.md)
### Initializers
- [convenience(mesh:offMeshConnections:configuration:)](navigationmeshresource/init(mesh:offmeshconnections:configuration:).md)
- [convenience(meshDescriptor:offMeshConnections:configuration:)](navigationmeshresource/init(meshdescriptor:offmeshconnections:configuration:).md)
- [convenience(named:in:)](navigationmeshresource/init(named:in:).md)
- [convenience(triangleIndices:vertices:offMeshConnections:configuration:)](navigationmeshresource/init(triangleindices:vertices:offmeshconnections:configuration:).md)

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Gaming sample code projects](game-development-sample-code.md)
  Explore a collection of projects relating to game development.
- [Entity animations](game-development-entity-animations.md)
  Dynamically move, rotate, and scale entities at runtime.
- [Character control, skeletons, and inverse kinematics](game-development-character-skeletons.md)
  Direct the movements and animation of models.
- [struct NavigationComponent](navigationcomponent.md)
  A component that defines which areas of a navigation mesh an entity can move through.
- [struct NavigationMeshComponent](navigationmeshcomponent.md)
  A component that provides the navigation meshes an entity uses to find paths through a scene.
- [struct NavigationController](navigationcontroller.md)
  An interface for finding paths for an entity moving across a scene’s navigation mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource)*