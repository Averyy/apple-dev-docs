# voxelIndexExtent

**Framework**: Model I/O  
**Kind**: property

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

#### Discussion

This property determines which [`MDLVoxelIndex`](mdlvoxelindex.md) values are valid for referring to the contents of the voxel array using methods such as [`setVoxelAtIndex(_:)`](mdlvoxelarray/setvoxelatindex(_:).md) or [`voxelBoundingBox(atIndex:)`](mdlvoxelarray/voxelboundingbox(atindex:).md). For example, if the minimum extent is `{0, 0, 0, 0}` and the maximum extent is `{10, 10, 10, 0}`, the voxel index `{5, 5, 5, 0}` lies within the array but the voxel index `{0, 20, 10, 0}` does not.

## See Also

- [var count: Int](mdlvoxelarray/count.md)
  The number of voxels in the array.
- [func voxelExists(atIndex: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool](mdlvoxelarray/voxelexists(atindex:allowanyx:allowanyy:allowanyz:allowanyshell:).md)
  Returns a Boolean value indicating whether the voxel array contains voxel data for the specified index.
- [func voxels(within: MDLVoxelIndexExtent) -> Data?](mdlvoxelarray/voxels(within:).md)
  Returns a data object containing all voxels within the specified volume.
- [func voxelIndices() -> Data?](mdlvoxelarray/voxelindices.md)
  Returns a data object containing all voxels within the voxel array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/voxelindexextent)*