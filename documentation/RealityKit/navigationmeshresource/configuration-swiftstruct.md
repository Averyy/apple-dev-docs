# NavigationMeshResource.Configuration

**Framework**: RealityKit  
**Kind**: struct

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
- [var characterRadius: Double](navigationmeshresource/configuration-swift.struct/characterradius.md)
- [var walkableSlopeAngle: Double](navigationmeshresource/configuration-swift.struct/walkableslopeangle.md)
- [var walkableClimb: Double](navigationmeshresource/configuration-swift.struct/walkableclimb.md)
### Configuring voxelization
- [var cellSize: Double](navigationmeshresource/configuration-swift.struct/cellsize.md)
- [var cellHeight: Double](navigationmeshresource/configuration-swift.struct/cellheight.md)
### Configuring region generation
- [var partitionMethod: NavigationMeshResource.Configuration.PartitionMethod](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.property.md)
- [NavigationMeshResource.Configuration.PartitionMethod](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum.md)
- [var minimumCellsPerRegion: Int](navigationmeshresource/configuration-swift.struct/minimumcellsperregion.md)
- [var minimumCellsToMergeRegions: Int](navigationmeshresource/configuration-swift.struct/minimumcellstomergeregions.md)
### Configuring contour meshing
- [var maximumEdgeLength: Double](navigationmeshresource/configuration-swift.struct/maximumedgelength.md)
- [var maximumSimplificationError: Double](navigationmeshresource/configuration-swift.struct/maximumsimplificationerror.md)
- [var maximumVerticesPerPolygon: Int](navigationmeshresource/configuration-swift.struct/maximumverticesperpolygon.md)
### Configuring detail mesh
- [var detailSampleDistance: Double](navigationmeshresource/configuration-swift.struct/detailsampledistance.md)
- [var detailSampleMaximumError: Double](navigationmeshresource/configuration-swift.struct/detailsamplemaximumerror.md)

## See Also

- [NavigationMeshResource.Area](navigationmeshresource/area.md)
- [NavigationMeshResource.Flag](navigationmeshresource/flag.md)
- [NavigationMeshResource.FlagGroup](navigationmeshresource/flaggroup.md)
- [NavigationMeshResource.OffMeshConnection](navigationmeshresource/offmeshconnection.md)
- [NavigationMeshResource.HeightData](navigationmeshresource/heightdata-swift.struct.md)
- [NavigationMeshResource.Layer](navigationmeshresource/layer-swift.struct.md)
- [NavigationMeshResource.PathNode](navigationmeshresource/pathnode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct)*