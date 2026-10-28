# voxels(within:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSData *) voxelsWithinExtent:(MDLVoxelIndexExtent) extent;
```

## Return Value

A data object containing [`MDLVoxelIndex`](../mdlvoxelindex.md) values.

## Discussion

The returned [`NSData`](../../Foundation/nsdata.md) object contains an array of [`MDLVoxelIndex`](../mdlvoxelindex.md) values describing the locations of voxels within the specified volume as well as their volumetric relationship to the object modeled by the voxel array.

## Parameters

- `extent`: The minimum and maximum corners of the volume for which to retrieve voxel data.

## See Also

### Examining Voxels
- [var count: Int](./count.md)
  The number of voxels in the array.
- [var voxelIndexExtent: MDLVoxelIndexExtent](./voxelindexextent.md)
  The indexes that define the corners of the three-dimensional voxel grid.
- [func voxelExists(atIndex: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool](./voxelexists%28atindex,allowanyx,allowanyy,allowanyz,allowanyshell%29.md)
  Returns a Boolean value indicating whether the voxel array contains voxel data for the specified index.
- [func voxelIndices() -> Data?](./voxelindices%28%29.md)
  Returns a data object containing all voxels within the voxel array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/voxels(within:))*