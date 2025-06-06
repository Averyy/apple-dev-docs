# voxelIndices()

**Framework**: Model I/O  
**Kind**: method

Returns a data object containing all voxels within the voxel array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func voxelIndices() -> Data?
```

#### Return Value

A data object containing [`MDLVoxelIndex`](mdlvoxelindex.md) values.

#### Discussion

The returned [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object contains an array of [`MDLVoxelIndex`](mdlvoxelindex.md) values describing the locations of voxels within the voxel array as well as their volumetric relationship to the object modeled by the voxel array.

Calling this method is equivalent to calling the [`voxels(within:)`](mdlvoxelarray/voxels(within:).md) method with the value of the [`voxelIndexExtent`](mdlvoxelarray/voxelindexextent.md) property.

## See Also

- [var count: Int](mdlvoxelarray/count.md)
  The number of voxels in the array.
- [var voxelIndexExtent: MDLVoxelIndexExtent](mdlvoxelarray/voxelindexextent.md)
  The indexes that define the corners of the three-dimensional voxel grid.
- [func voxelExists(atIndex: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool](mdlvoxelarray/voxelexists(atindex:allowanyx:allowanyy:allowanyz:allowanyshell:).md)
  Returns a Boolean value indicating whether the voxel array contains voxel data for the specified index.
- [func voxels(within: MDLVoxelIndexExtent) -> Data?](mdlvoxelarray/voxels(within:).md)
  Returns a data object containing all voxels within the specified volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/voxelindices())*