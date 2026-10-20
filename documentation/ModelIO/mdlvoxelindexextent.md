# MDLVoxelIndexExtent

**Framework**: Model I/O  
**Kind**: struct  
**Role**: Structure

The corner voxel indices defining a solid rectangular volume of voxels. Used by the [`voxelIndexExtent`](./mdlvoxelarray/voxelindexextent.md) property and [`voxels(within:)`](./mdlvoxelarray/voxels%28within%29.md) method.

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

```c
typedef struct { ... } MDLVoxelIndexExtent;
```

## Topics

### Initializers
- [init()](./mdlvoxelindexextent/init%28%29.md)
- [init(minimumExtent: MDLVoxelIndex, maximumExtent: MDLVoxelIndex)](./mdlvoxelindexextent/init%28minimumextent,maximumextent%29.md)
### Instance Properties
- [var maximumExtent: MDLVoxelIndex](./mdlvoxelindexextent/maximumextent.md)
  The highest x, y, and z coordinates in the volume.
- [var minimumExtent: MDLVoxelIndex](./mdlvoxelindexextent/minimumextent.md)
  The lowest x, y, and z coordinates in the volume.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Constants
- [typealias MDLVoxelIndex](./mdlvoxelindex.md)
  A 4-component vector encoding the location of a voxel in a voxel array and describing its relation to an object’s volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelindexextent)*