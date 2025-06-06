# init(asset:divisions:interiorShells:exteriorShells:patchRadius:)

**Framework**: Model I/O  
**Kind**: init

Initializes a voxel array that models the volume of 3D objects in the specified asset and creates the specified number of voxel shells.

**Availability**:
- macOS 10.11+

## Declaration

```swift
init(asset: MDLAsset, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)
```

#### Return Value

A new voxel array.

#### Discussion

When you create a voxel array from an asset, Model I/O analyzes any meshes contained in the asset to determine the volume of the 3D objects modeled by those meshes. This initializer discretizes that volume by dividing the asset’s [`boundingBox`](mdlasset/boundingbox.md) coordinates into a three-dimensional grid. The `divisions` parameter determines the height of the grid in voxels. Because single voxel is a cubic unit, the width and depth of the grid in voxels is proportional to its height and the bounding box of the asset.

After dividing the bounding box into a grid, Model I/O generates a shell of voxels at the grid positions corresponding to points on the mesh’s surface. Each voxel is a [`MDLVoxelIndex`](mdlvoxelindex.md) value whose x, y, and z coordinates locate the voxel in the grid and whose w coordinate value is 0, indicating that the voxel is on the surface of the object.

If you pass a value greater than zero for the `interiorShells` or `exteriorShells` parameter, this initializer also generates voxel data for the grid positions within or outside of the surface. For example, if you pass an `interiorShells` value of `1`, Model I/O generates a single concentric shell of voxels inside the surface. For those voxels, the w coordinate indicates how many shells lie between that voxel and the surface shell.

## Parameters

- `asset`: An asset containing meshes whose volume is to be modeled as voxels.
- `divisions`: The number of divisions to create along the y-axis of the asset’s bounding box; that is, the height in voxels of the resulting voxel array.
- `interiorShells`: The number of concentric shells of voxels to generate inside the object’s surface.
- `exteriorShells`: The number of concentric shells of voxels to generate outside the object’s surface.
- `patchRadius`: The largest radius, in world space units, of patches to apply to create closed volumes from meshes in the asset.

## See Also

- [init(asset: MDLAsset, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)](mdlvoxelarray/init(asset:divisions:interiornbwidth:exteriornbwidth:patchradius:).md)
  Initializes a voxel array that models the volume of 3D objects in the specified asset, creating voxel shells for the specified distances from the object’s surface.
- [init(data: Data, boundingBox: MDLAxisAlignedBoundingBox, voxelExtent: Float)](mdlvoxelarray/init(data:boundingbox:voxelextent:).md)
  Initializes a voxel array with the specified voxel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/init(asset:divisions:interiorshells:exteriorshells:patchradius:))*