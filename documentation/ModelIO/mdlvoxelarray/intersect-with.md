# intersect(with:)

**Framework**: Model I/O  
**Kind**: method

Reduces the voxel array to cover only the volume within both it and another voxel array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func intersect(with voxels: MDLVoxelArray)
```

#### Discussion

After an intersection operation, the voxel array contains only those voxels that were present in both the original array and the specified array. That is, an intersection operation creates a voxel array representing only the space where two volumes overlap.

Performing a union, intersection, or difference operation clears out shell level information from all voxels in the array. (That is, the w component of every [`MDLVoxelIndex`](mdlvoxelindex.md) value in the voxel array is reset to 0.)

## Parameters

- `voxels`: The voxel array to intersect with this voxel array.

## See Also

- [func union(with: MDLVoxelArray)](mdlvoxelarray/union(with:).md)
  Extends the voxel array to also cover the volume of the specified voxel array.
- [func difference(with: MDLVoxelArray)](mdlvoxelarray/difference(with:).md)
  Reduces the voxel array to cover only the portion of its volume not covered by another voxel array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/intersect(with:))*