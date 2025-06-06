# voxels(within:)

**Framework**: Model I/O  
**Kind**: method

Returns a data object containing all voxels within the specified volume.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func voxels(within extent: MDLVoxelIndexExtent) -> Data?
```

#### Return Value

A data object containing [`MDLVoxelIndex`](mdlvoxelindex.md) values.

#### Discussion

The returned [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object contains an array of [`MDLVoxelIndex`](mdlvoxelindex.md) values describing the locations of voxels within the specified volume as well as their volumetric relationship to the object modeled by the voxel array.

## Parameters

- `extent`: The minimum and maximum corners of the volume for which to retrieve voxel data.

## See Also

- [var count: Int](mdlvoxelarray/count.md)
  The number of voxels in the array.
- [var voxelIndexExtent: MDLVoxelIndexExtent](mdlvoxelarray/voxelindexextent.md)
  The indexes that define the corners of the three-dimensional voxel grid.
- [func voxelExists(atIndex: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool](mdlvoxelarray/voxelexists(atindex:allowanyx:allowanyy:allowanyz:allowanyshell:).md)
  Returns a Boolean value indicating whether the voxel array contains voxel data for the specified index.
- [func voxelIndices() -> Data?](mdlvoxelarray/voxelindices.md)
  Returns a data object containing all voxels within the voxel array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/voxels(within:))*