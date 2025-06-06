# MDLVoxelIndexExtent

**Framework**: Model I/O  
**Kind**: struct

The corner voxel indices defining a solid rectangular volume of voxels. Used by the [`voxelIndexExtent`](mdlvoxelarray/voxelindexextent.md) property and [`voxels(within:)`](mdlvoxelarray/voxels(within:).md) method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MDLVoxelIndexExtent
```

## Topics

### Initializers
- [init()](mdlvoxelindexextent/init.md)
- [init(minimumExtent: MDLVoxelIndex, maximumExtent: MDLVoxelIndex)](mdlvoxelindexextent/init(minimumextent:maximumextent:).md)
### Instance Properties
- [var maximumExtent: MDLVoxelIndex](mdlvoxelindexextent/maximumextent.md)
  The highest x, y, and z coordinates in the volume.
- [var minimumExtent: MDLVoxelIndex](mdlvoxelindexextent/minimumextent.md)
  The lowest x, y, and z coordinates in the volume.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias MDLVoxelIndex](mdlvoxelindex.md)
  A 4-component vector encoding the location of a voxel in a voxel array and describing its relation to an object’s volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelindexextent)*