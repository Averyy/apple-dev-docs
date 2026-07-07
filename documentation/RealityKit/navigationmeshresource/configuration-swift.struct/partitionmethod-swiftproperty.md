# partitionMethod

**Framework**: RealityKit  
**Kind**: property

The partitioning method to use when creating the polygon regions of the Navigation Mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var partitionMethod: NavigationMeshResource.Configuration.PartitionMethod
```

## See Also

- [NavigationMeshResource.Configuration.PartitionMethod](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum.md)
  The partitioning method to use for creating the polygons of the mesh.
- [var minimumCellsPerRegion: Int](navigationmeshresource/configuration-swift.struct/minimumcellsperregion.md)
  The minimum number of cells allowed to generate isolated regions or islands in the Navigation Mesh.
- [var minimumCellsToMergeRegions: Int](navigationmeshresource/configuration-swift.struct/minimumcellstomergeregions.md)
  The number of walkable cells in a region below which the region will be merged with nearby regions to simplify the Navigation Mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct/partitionmethod-swift.property)*