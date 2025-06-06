# setVoxelsFor(_:divisions:interiorNBWidth:exteriorNBWidth:patchRadius:)

**Framework**: Model I/O  
**Kind**: method

Sets voxel values in the array to model the volume of the specified mesh and creates voxel shells for the specified distances from the object’s surface.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func setVoxelsFor(_ mesh: MDLMesh, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)
```

#### Discussion

When you add a mesh to a voxel array, Model I/O analyzes the mesh to determine the volume of the 3D object it models. This method discretizes that volume by dividing the mesh’s [`boundingBox`](mdlasset/boundingbox.md) coordinates into a three-dimensional grid. The `divisions` parameter determines the height of the grid in voxels. A single voxel is a cubic unit, so the width and depth of the grid in voxels is proportional to its height and the bounding box of the mesh.

After dividing the bounding box into a grid, Model I/O generates a shell of voxels at the grid positions corresponding to points on the mesh’s surface. Each voxel is a [`MDLVoxelIndex`](mdlvoxelindex.md) value whose x, y, and z coordinates locate the voxel in the grid, and whose w coordinate value is 0, indicating that the voxel is on the surface of the object.

If you pass a value greater than zero for the `interiorNBWidth` or `exteriorNBWidth` parameter, this method also generates voxel data for the grid positions within or outside of the surface. For example, if you pass an `interiorNBWidth` value of `2.5`, Model I/O generates concentric shells of voxels inside the surface such that the distance from each voxel to the surface is no greater than 2.5 units. For those voxels, the w coordinate indicates how many shells lie between that voxel and the surface shell.

After generating voxel data for the specified mesh, this method adds that data to any existing voxel data in the voxel array.

## Parameters

- `mesh`: A mesh whose volume is to be modeled as voxels.
- `divisions`: The number of divisions to create along the y-axis of the asset’s bounding box; that is, the height in voxels of the resulting portion of the voxel array.
- `interiorNBWidth`: The distance, in units of the mesh’s parent coordinate space, inside the object’s surface for which to generate additional voxels.
- `exteriorNBWidth`: The distance, in units of the mesh’s parent coordinate space, outside the object’s surface for which to generate additional voxels.
- `patchRadius`: The largest radius, in world space units, of patches to apply to create closed volumes from the mesh.

## See Also

- [func setVoxelAtIndex(MDLVoxelIndex)](mdlvoxelarray/setvoxelatindex(_:).md)
  Sets voxel characteristics at the specified index in the array.
- [func setVoxelsFor(MDLMesh, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)](mdlvoxelarray/setvoxelsfor(_:divisions:interiorshells:exteriorshells:patchradius:).md)
  Sets voxel values in the array to model the volume of the specified mesh and creates the specified number of voxel shells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/setvoxelsfor(_:divisions:interiornbwidth:exteriornbwidth:patchradius:))*