# NavigationMeshResource.Configuration

**Framework**: RealityKit  
**Kind**: struct

The NavigationMeshResource configuration that defines how the mesh is created.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(cellSize: Double, cellHeight: Double, walkableSlopeAngle: Double, characterHeight: Double, walkableClimb: Double, characterRadius: Double)](navigationmeshresource/configuration-swift.struct/init(cellsize:cellheight:walkableslopeangle:characterheight:walkableclimb:characterradius:).md)
### Configuring agent movement
- [var characterHeight: Double](navigationmeshresource/configuration-swift.struct/characterheight.md)
  The height of characters using this Navigation Mesh, representing the minimum height of obstacles above a surface to allow it to be walkable, in meters.
- [var characterRadius: Double](navigationmeshresource/configuration-swift.struct/characterradius.md)
  The radius of characters using this Navigation Mesh, representing the minimum distance from edges or obstacles that can still be walkable, in meters.
- [var walkableSlopeAngle: Double](navigationmeshresource/configuration-swift.struct/walkableslopeangle.md)
  The maximum slope angle that will allow a surface to be walkable, in degrees.
- [var walkableClimb: Double](navigationmeshresource/configuration-swift.struct/walkableclimb.md)
  The maximum height difference between two surfaces that a character can walk through, in meters.
### Configuring voxelization
- [var cellSize: Double](navigationmeshresource/configuration-swift.struct/cellsize.md)
  The x-z size of a cell, in meters.
- [var cellHeight: Double](navigationmeshresource/configuration-swift.struct/cellheight.md)
  The height of a cell, in meters.
### Configuring region generation
- [var partitionMethod: NavigationMeshResource.Configuration.PartitionMethod](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.property.md)
  The partitioning method to use when creating the polygon regions of the Navigation Mesh.
- [NavigationMeshResource.Configuration.PartitionMethod](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum.md)
  The partitioning method to use for creating the polygons of the mesh.
- [var minimumCellsPerRegion: Int](navigationmeshresource/configuration-swift.struct/minimumcellsperregion.md)
  The minimum number of cells allowed to generate isolated regions or islands in the Navigation Mesh.
- [var minimumCellsToMergeRegions: Int](navigationmeshresource/configuration-swift.struct/minimumcellstomergeregions.md)
  The number of walkable cells in a region below which the region will be merged with nearby regions to simplify the Navigation Mesh.
### Configuring contour meshing
- [var maximumEdgeLength: Double](navigationmeshresource/configuration-swift.struct/maximumedgelength.md)
  The maximum length of polygon edges in the generated Navigation Mesh, in meters. This value can help modify the resulting Navigation Mesh to have better-looking polygons on maps with long, uninterrupted edges.
- [var maximumSimplificationError: Double](navigationmeshresource/configuration-swift.struct/maximumsimplificationerror.md)
  The maximum deviation that the contours of a generated Navigation Mesh can have from the original mesh, in meters.
- [var maximumVerticesPerPolygon: Int](navigationmeshresource/configuration-swift.struct/maximumverticesperpolygon.md)
  The maximum vertices per polygon used when creating the Navigation Mesh.
### Configuring detail mesh
- [var detailSampleDistance: Double](navigationmeshresource/configuration-swift.struct/detailsampledistance.md)
  The sampling distance used when generating the detailed Navigation Mesh heightmap, in meters.
- [var detailSampleMaximumError: Double](navigationmeshresource/configuration-swift.struct/detailsamplemaximumerror.md)
  The maximum deviation from the original heightfield data allowed when creating the detailed heightmap, in meters.

## See Also

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
- [NavigationMeshResource.PathNode](navigationmeshresource/pathnode.md)
  A container for the path node data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct)*