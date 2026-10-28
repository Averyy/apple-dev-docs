# count

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The number of voxels in the array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var count: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger count;
```

## Discussion

This property measures the number of grid positions in the array for which voxel data exists, not the total number of grid positions within the voxel array’s extent.

## See Also

### Examining Voxels
- [var voxelIndexExtent: MDLVoxelIndexExtent](./voxelindexextent.md)
  The indexes that define the corners of the three-dimensional voxel grid.
- [func voxelExists(atIndex: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool](./voxelexists%28atindex,allowanyx,allowanyy,allowanyz,allowanyshell%29.md)
  Returns a Boolean value indicating whether the voxel array contains voxel data for the specified index.
- [func voxels(within: MDLVoxelIndexExtent) -> Data?](./voxels%28within%29.md)
  Returns a data object containing all voxels within the specified volume.
- [func voxelIndices() -> Data?](./voxelindices%28%29.md)
  Returns a data object containing all voxels within the voxel array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/count)*