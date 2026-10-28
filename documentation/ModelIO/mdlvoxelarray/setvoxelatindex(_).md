# setVoxelAtIndex(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Sets voxel characteristics at the specified index in the array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setVoxelAtIndex(_ index: MDLVoxelIndex)
```

```objc
- (void) setVoxelAtIndex:(MDLVoxelIndex) index;
```

## Discussion

A [`MDLVoxelIndex`](../mdlvoxelindex.md) value describes both a location in the voxel array and the characteristics of the volume at that location. To set characteristics at a location, pass a [`MDLVoxelIndex`](../mdlvoxelindex.md) value whose first three components are the x, y, and z coordinates of that location and whose w coordinate specifies the *shell level* at that location.

Shell level describes the relationship of that location’s volume to the object modeled by the voxel array: 0 for a voxel on the object’s surface, a positive value for voxels outside of the object’s volume, and a negative value for voxels inside the object’s volume. For voxels inside or outside the object, the magnitude of shell level indicates the number of voxels between the index and a voxel on the surface of the object.

## Parameters

- `index`: A voxel index to update in the array.

## See Also

### Modifying Voxels
- [func setVoxelsFor(MDLMesh, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)](./setvoxelsfor%28_,divisions,interiornbwidth,exteriornbwidth,patchradius%29.md)
  Sets voxel values in the array to model the volume of the specified mesh and creates voxel shells for the specified distances from the object’s surface.
- [func setVoxelsFor(MDLMesh, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)](./setvoxelsfor%28_,divisions,interiorshells,exteriorshells,patchradius%29.md)
  Sets voxel values in the array to model the volume of the specified mesh and creates the specified number of voxel shells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/setvoxelatindex(_:))*