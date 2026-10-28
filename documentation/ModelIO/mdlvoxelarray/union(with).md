# union(with:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Extends the voxel array to also cover the volume of the specified voxel array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func union(with voxels: MDLVoxelArray)
```

```objc
- (void) unionWithVoxels:(MDLVoxelArray *) voxels;
```

## Discussion

After a union operation, the voxel array contains voxels that were present either in the original array or in the specified array. That is, a union operation creates a voxel array that combines two volumes.

Performing a union, intersection, or difference operation clears out shell level information from all voxels in the array. (That is, the w component of every [`MDLVoxelIndex`](../mdlvoxelindex.md) value in the voxel array is reset to 0.)

## Parameters

- `voxels`: The voxel array to combine with this voxel array.

## See Also

### Performing Constructive Solid Geometry Operations
- [func intersect(with: MDLVoxelArray)](./intersect%28with%29.md)
  Reduces the voxel array to cover only the volume within both it and another voxel array.
- [func difference(with: MDLVoxelArray)](./difference%28with%29.md)
  Reduces the voxel array to cover only the portion of its volume not covered by another voxel array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/union(with:))*