# setVoxelsFor(_:divisions:interiorShells:exteriorShells:patchRadius:)

**Framework**: Model I/O  
**Kind**: method

Sets voxel values in the array to model the volume of the specified mesh and creates the specified number of voxel shells.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func setVoxelsFor(_ mesh: MDLMesh, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)
```

#### Discussion

When you add a mesh to a voxel array, Model I/O analyzes the mesh to determine the volume of the 3D object it models. This method discretizes that volume by dividing the mesh’s [`boundingBox`](mdlasset/boundingbox.md) coordinates into a three-dimensional grid. The `divisions` parameter determines the height of the grid in voxels. A single voxel is a cubic unit, so the width and depth of the grid in voxels is proportional to its height and the bounding box of the mesh.

After dividing the bounding box into a grid, Model I/O generates a shell of voxels at the grid positions corresponding to points on the mesh’s surface. Each voxel is a [`MDLVoxelIndex`](mdlvoxelindex.md) value whose x, y, and z coordinates locate the voxel in the grid, and whose w coordinate value is 0, indicating that the voxel is on the surface of the object.

If you pass a value greater than zero for the `interiorShells` or `exteriorShells` parameter, this method also generates voxel data for the grid positions within or outside of the surface. For example, if you pass an `interiorShells` value of `1`, Model I/O generates a single concentric shell of voxels inside the surface. For those voxels, the w coordinate indicates how many shells lie between that voxel and the surface shell.

After generating voxel data for the specified mesh, this method adds that data to any existing voxel data in the voxel array.

## Parameters

- `mesh`: A mesh whose volume is to be modeled as voxels.
- `divisions`: The number of divisions to create along the y-axis of the mesh’s bounding box; that is, the height in voxels of the resulting portion of the voxel array.
- `interiorShells`: The number of concentric shells of voxels to generate inside the object’s surface.
- `exteriorShells`: The number of concentric shells of voxels to generate outside the object’s surface.
- `patchRadius`: The largest radius, in world space units, of patches to apply to create closed volumes from the mesh.

## See Also

- [func setVoxelAtIndex(MDLVoxelIndex)](mdlvoxelarray/setvoxelatindex(_:).md)
  Sets voxel characteristics at the specified index in the array.
- [func setVoxelsFor(MDLMesh, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)](mdlvoxelarray/setvoxelsfor(_:divisions:interiornbwidth:exteriornbwidth:patchradius:).md)
  Sets voxel values in the array to model the volume of the specified mesh and creates voxel shells for the specified distances from the object’s surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/setvoxelsfor(_:divisions:interiorshells:exteriorshells:patchradius:))*