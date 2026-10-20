# NavigationMeshResource

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A representation of a scene’s navigable surfaces that the system uses to compute paths.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class NavigationMeshResource
```

#### Overview

Build a navigation mesh from a model’s geometry or from raw vertex and polygon data, then mark areas and flags to describe where agents can travel and at what cost. Provide the resulting resource to a [`NavigationMeshComponent`](./navigationmeshcomponent.md) so a [`NavigationController`](./navigationcontroller.md) can find paths across it.

## Topics

### Creating a navigation mesh
- [convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](./navigationmeshresource/init%28mesh,offmeshconnections,configuration%29-6xdta.md)
  Creates a NavigationMeshResource from a MeshResource. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(mesh: MeshResource, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](./navigationmeshresource/init%28mesh,offmeshconnections,configuration%29-7mj9i.md)
  Asynchronously creates a NavigationMeshResource from a MeshResource. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](./navigationmeshresource/init%28meshdescriptor,offmeshconnections,configuration%29-3n43t.md)
  Creates a NavigationMeshResource from a MeshDescriptor. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(meshDescriptor: MeshDescriptor, offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](./navigationmeshresource/init%28meshdescriptor,offmeshconnections,configuration%29-6zzvf.md)
  Asynchronously creates a NavigationMeshResource from a MeshDescriptor. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) throws](./navigationmeshresource/init%28triangleindices,vertices,offmeshconnections,configuration%29-2rrq1.md)
  Creates a NavigationMeshResource from triangle indices and vertices. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(triangleIndices: [UInt32], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration) async throws](./navigationmeshresource/init%28triangleindices,vertices,offmeshconnections,configuration%29-480i3.md)
  Asynchronously creates a NavigationMeshResource from triangle indices and vertices. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience init(polygonIndices: [[Int]], vertices: [SIMD3<Float>], offMeshConnections: [NavigationMeshResource.OffMeshConnection], configuration: NavigationMeshResource.Configuration, areas: [NavigationMeshResource.Area], flags: [[NavigationMeshResource.Flag]], heightData: NavigationMeshResource.HeightData) throws](./navigationmeshresource/init%28polygonindices,vertices,offmeshconnections,configuration,areas,flags,heightdata%29.md)
  Creates a NavigationMeshResource through existing Navigation Mesh data. This will not regenerate the Navigation Mesh. It will copy and save the input data to create a Navigation Mesh with this information.
### Marking areas and flags
- [func markAreaInBox(boundingBox: BoundingBox, area: NavigationMeshResource.Area)](./navigationmeshresource/markareainbox%28boundingbox,area%29.md)
  Marks all polygons in this box with an area.
- [func markFlagInBox(boundingBox: BoundingBox, flag: NavigationMeshResource.Flag)](./navigationmeshresource/markflaginbox%28boundingbox,flag%29.md)
  Marks all polygons in this box with a flag.
- [func markAreaInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, area: NavigationMeshResource.Area)](./navigationmeshresource/markareaincylinder%28position,radius,halfheight,area%29.md)
  Marks all polygons in this cylinder with an area.
- [func markFlagInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, flag: NavigationMeshResource.Flag)](./navigationmeshresource/markflagincylinder%28position,radius,halfheight,flag%29.md)
  Marks all polygons in this cylinder with a flag.
- [func markAreaOnPolygons(polygonIndices: [Int], area: NavigationMeshResource.Area)](./navigationmeshresource/markareaonpolygons%28polygonindices,area%29.md)
  Marks the polygons at these indices with an area.
- [func markFlagOnPolygons(polygonIndices: [Int], flag: NavigationMeshResource.Flag)](./navigationmeshresource/markflagonpolygons%28polygonindices,flag%29.md)
  Marks the polygons at these indices with a flag.
- [func markAreaOnOffMeshConnections(offMeshConnectionIndices: [Int], area: NavigationMeshResource.Area)](./navigationmeshresource/markareaonoffmeshconnections%28offmeshconnectionindices,area%29.md)
  Marks the off-mesh connections at these indices with an area.
- [func markFlagOnOffMeshConnections(offMeshConnectionIndices: [Int], flag: NavigationMeshResource.Flag)](./navigationmeshresource/markflagonoffmeshconnections%28offmeshconnectionindices,flag%29.md)
  Marks the off-mesh connections at these indices with a flag.
### Removing areas and flags
- [func removeAreaInBox(boundingBox: BoundingBox, area: NavigationMeshResource.Area)](./navigationmeshresource/removeareainbox%28boundingbox,area%29.md)
  Removes the area from all polygons in this box.
- [func removeFlagInBox(boundingBox: BoundingBox, flag: NavigationMeshResource.Flag)](./navigationmeshresource/removeflaginbox%28boundingbox,flag%29.md)
  Removes the flag from all polygons in this box.
- [func removeAreaInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, area: NavigationMeshResource.Area)](./navigationmeshresource/removeareaincylinder%28position,radius,halfheight,area%29.md)
  Removes the area from all polygons in this cylinder.
- [func removeFlagInCylinder(position: SIMD3<Float>, radius: Float, halfHeight: Float, flag: NavigationMeshResource.Flag)](./navigationmeshresource/removeflagincylinder%28position,radius,halfheight,flag%29.md)
  Removes the flag from all polygons in this cylinder.
- [func removeAreaOnPolygons(polygonIndices: [Int], area: NavigationMeshResource.Area)](./navigationmeshresource/removeareaonpolygons%28polygonindices,area%29.md)
  Removes the area from the polygons at these indices.
- [func removeFlagOnPolygons(polygonIndices: [Int], flag: NavigationMeshResource.Flag)](./navigationmeshresource/removeflagonpolygons%28polygonindices,flag%29.md)
  Removes the flag from the polygons at these indices.
- [func removeAreaOnOffMeshConnections(offMeshConnectionIndices: [Int], area: NavigationMeshResource.Area)](./navigationmeshresource/removeareaonoffmeshconnections%28offmeshconnectionindices,area%29.md)
  Removes the area from the off-mesh connections at these indices.
- [func removeFlagOnOffMeshConnections(offMeshConnectionIndices: [Int], flag: NavigationMeshResource.Flag)](./navigationmeshresource/removeflagonoffmeshconnections%28offmeshconnectionindices,flag%29.md)
  Removes the flag from the off-mesh connections at these indices.
### Accessing mesh data
- [var vertices: [SIMD3<Float>]](./navigationmeshresource/vertices.md)
  The vertices of the generated Navigation Mesh.
- [var polygonIndices: [[Int]]](./navigationmeshresource/polygonindices.md)
  The polygon indices of the generated Navigation Mesh. Polygons may have different numbers of vertices, so each entry in the list is a list of indices into the vertices array for that polygon.
- [var areas: [NavigationMeshResource.Area]](./navigationmeshresource/areas.md)
  The areas associated with each polygon in the generated Navigation Mesh.
- [var flags: [[NavigationMeshResource.Flag]]](./navigationmeshresource/flags.md)
  The flags associated with each polygon in the generated Navigation Mesh.
- [var offMeshConnections: [NavigationMeshResource.OffMeshConnection]](./navigationmeshresource/offmeshconnections.md)
  The off-mesh connections of the generated Navigation Mesh.
- [var heightData: NavigationMeshResource.HeightData](./navigationmeshresource/heightdata-swift.property.md)
  The detailed height data of the generated Navigation Mesh.
- [var layer: NavigationMeshResource.Layer?](./navigationmeshresource/layer-swift.property.md)
  The identification of this NavigationMeshResource, used when entities are searching for a specific NavigationMeshResource in a scene.
- [var configuration: NavigationMeshResource.Configuration](./navigationmeshresource/configuration-swift.property.md)
  The configuration this Navigation Mesh was created with.
### Supporting types
- [NavigationMeshResource.Configuration](./navigationmeshresource/configuration-swift.struct.md)
  The NavigationMeshResource configuration that defines how the mesh is created.
- [NavigationMeshResource.Area](./navigationmeshresource/area.md)
  An identifier for different areas on a Navigation Mesh.
- [NavigationMeshResource.Flag](./navigationmeshresource/flag.md)
  An identifier for different flags on a Navigation Mesh.
- [NavigationMeshResource.FlagGroup](./navigationmeshresource/flaggroup.md)
  A collection of Flags.
- [NavigationMeshResource.OffMeshConnection](./navigationmeshresource/offmeshconnection.md)
  A container for the data associated with an off-mesh connection.
- [NavigationMeshResource.HeightData](./navigationmeshresource/heightdata-swift.struct.md)
  A container for the detailed height data of the NavigationMeshResource.
- [NavigationMeshResource.Layer](./navigationmeshresource/layer-swift.struct.md)
  An identifier for a Navigation Mesh, used by a [`NavigationComponent`](./navigationcomponent.md) to select a specific Navigation Mesh for pathfinding.
- [NavigationMeshResource.PathNode](./navigationmeshresource/pathnode.md)
  A container for the path node data.
### Initializers
- [convenience(mesh:offMeshConnections:configuration:)](./navigationmeshresource/init%28mesh,offmeshconnections,configuration%29.md)
  Asynchronously creates a NavigationMeshResource from a MeshResource. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience(meshDescriptor:offMeshConnections:configuration:)](./navigationmeshresource/init%28meshdescriptor,offmeshconnections,configuration%29.md)
  Asynchronously creates a NavigationMeshResource from a MeshDescriptor. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.
- [convenience(named:in:)](./navigationmeshresource/init%28named,in%29.md)
  Asynchronously creates a NavigationMeshResource by importing an existing one from a Bundle. The name is the path of the NavigationMeshResource within the bundle. The bundle is the app package that contains the NavigationMeshResource. If nothing is specified, then the main bundle is used. This loads an existing Navigation Mesh and will not process and create a new one.
- [convenience(triangleIndices:vertices:offMeshConnections:configuration:)](./navigationmeshresource/init%28triangleindices,vertices,offmeshconnections,configuration%29.md)
  Asynchronously creates a NavigationMeshResource from triangle indices and vertices. This will take the input geometry and configuration and process it into a Navigation Mesh. The input and final geometry of the Navigation Mesh may not match, as it strives to simplify regions and match the configuration to determine what areas are walkable.

## Relationships

### Conforms To
- [Resource](./resource.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Game development
- [Gaming sample code projects](./game-development-sample-code.md)
  Explore a collection of projects relating to game development.
- [Entity animations](./game-development-entity-animations.md)
  Dynamically move, rotate, and scale entities at runtime.
- [Character control, skeletons, and inverse kinematics](./game-development-character-skeletons.md)
  Direct the movements and animation of models.
- [struct NavigationComponent](./navigationcomponent.md)
  A component that defines which areas of a navigation mesh an entity can move through.
- [struct NavigationMeshComponent](./navigationmeshcomponent.md)
  A component that provides the navigation meshes an entity uses to find paths through a scene.
- [struct NavigationController](./navigationcontroller.md)
  An interface for finding paths for an entity moving across a scene’s navigation mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource)*