# voxelIndexExtent

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The indexes that define the corners of the three-dimensional voxel grid.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var voxelIndexExtent: MDLVoxelIndexExtent { get }
```

```objc
@property (nonatomic, readonly) MDLVoxelIndexExtent voxelIndexExtent;
```

#### Discussion

This property determines which [`MDLVoxelIndex`](../mdlvoxelindex.md) values are valid for referring to the contents of the voxel array using methods such as [`setVoxelAtIndex(_:)`](./setvoxelatindex%28_%29.md) or [`voxelBoundingBox(atIndex:)`](./voxelboundingbox%28atindex%29.md). For example, if the minimum extent is `{0, 0, 0, 0}` and the maximum extent is `{10, 10, 10, 0}`, the voxel index `{5, 5, 5, 0}` lies within the array but the voxel index `{0, 20, 10, 0}` does not.

## See Also

### Examining Voxels
- [var count: Int](./count.md)
  The number of voxels in the array.
- [func voxelExists(atIndex: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool](./voxelexists%28atindex,allowanyx,allowanyy,allowanyz,allowanyshell%29.md)
  Returns a Boolean value indicating whether the voxel array contains voxel data for the specified index.
- [func voxels(within: MDLVoxelIndexExtent) -> Data?](./voxels%28within%29.md)
  Returns a data object containing all voxels within the specified volume.
- [func voxelIndices() -> Data?](./voxelindices%28%29.md)
  Returns a data object containing all voxels within the voxel array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/voxelindexextent)*