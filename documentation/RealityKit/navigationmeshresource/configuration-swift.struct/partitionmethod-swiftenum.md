# NavigationMeshResource.Configuration.PartitionMethod

**Framework**: RealityKit  
**Kind**: enum

The partitioning method to use for creating the polygons of the mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum PartitionMethod
```

## Topics

### Choosing a partition method
- [NavigationMeshResource.Configuration.PartitionMethod.watershed](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/watershed.md)
  The default method. Watershed is usually the slowest but creates the best-looking meshes.
- [NavigationMeshResource.Configuration.PartitionMethod.monotone](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/monotone.md)
  The fastest method. On large, empty areas it tends to create long, thin polygons, so it is not ideal for generating the mesh offline or with large open regions in the geometry.
- [NavigationMeshResource.Configuration.PartitionMethod.layer](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum/layer.md)
  A fast method, but slower than Monotone. It can create poor-looking meshes when used on large open regions, similar to Monotone, but will still generally create better-looking meshes than Monotone.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var partitionMethod: NavigationMeshResource.Configuration.PartitionMethod](navigationmeshresource/configuration-swift.struct/partitionmethod-swift.property.md)
  The partitioning method to use when creating the polygon regions of the Navigation Mesh.
- [var minimumCellsPerRegion: Int](navigationmeshresource/configuration-swift.struct/minimumcellsperregion.md)
  The minimum number of cells allowed to generate isolated regions or islands in the Navigation Mesh.
- [var minimumCellsToMergeRegions: Int](navigationmeshresource/configuration-swift.struct/minimumcellstomergeregions.md)
  The number of walkable cells in a region below which the region will be merged with nearby regions to simplify the Navigation Mesh.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/navigationmeshresource/configuration-swift.struct/partitionmethod-swift.enum)*