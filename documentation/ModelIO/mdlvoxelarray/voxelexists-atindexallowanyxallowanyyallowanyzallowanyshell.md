# voxelExists(atIndex:allowAnyX:allowAnyY:allowAnyZ:allowAnyShell:)

**Framework**: Model I/O  
**Kind**: method

Returns a Boolean value indicating whether the voxel array contains voxel data for the specified index.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func voxelExists(atIndex index: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the voxel array contains at least one voxel index matching the specified parameters; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Use the `allowAnyX`, `allowAnyY`, `allowAnyZ`, and `allowAnyShell` parameters to perform wildcard searches. For example:

## Parameters

- `index`: An index describing both the location of the voxel within the three-dimensional grid of the voxel array and its relationship to the volume of the object modeled by the voxel array.
- `allowAnyX`: If  , this method treats the x component of the index parameter as a wildcard. If  , this method requires an exact match for the x component.
- `allowAnyY`: If  , this method treats the y component of the index parameter as a wildcard. If  , this method requires an exact match for the y component.
- `allowAnyZ`: If  , this method treats the z component of the index parameter as a wildcard. If  , this method requires an exact match for the z component.
- `allowAnyShell`: If  , this method treats the w (shell level) component of the index parameter as a wildcard. If  , this method requires an exact match for the shell level component.

## See Also

- [var count: Int](mdlvoxelarray/count.md)
  The number of voxels in the array.
- [var voxelIndexExtent: MDLVoxelIndexExtent](mdlvoxelarray/voxelindexextent.md)
  The indexes that define the corners of the three-dimensional voxel grid.
- [func voxels(within: MDLVoxelIndexExtent) -> Data?](mdlvoxelarray/voxels(within:).md)
  Returns a data object containing all voxels within the specified volume.
- [func voxelIndices() -> Data?](mdlvoxelarray/voxelindices.md)
  Returns a data object containing all voxels within the voxel array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/voxelexists(atindex:allowanyx:allowanyy:allowanyz:allowanyshell:))*