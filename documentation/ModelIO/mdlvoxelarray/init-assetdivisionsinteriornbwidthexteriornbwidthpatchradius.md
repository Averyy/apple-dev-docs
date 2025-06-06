# init(asset:divisions:interiorNBWidth:exteriorNBWidth:patchRadius:)

**Framework**: Model I/O  
**Kind**: init

Initializes a voxel array that models the volume of 3D objects in the specified asset, creating voxel shells for the specified distances from the object’s surface.

**Availability**:
- macOS 10.11+

## Declaration

```swift
init(asset: MDLAsset, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)
```

#### Return Value

A new voxel array.

#### Discussion

When you create a voxel array from an asset, Model I/O analyzes any meshes contained in the asset to determine the volume of the 3D objects modeled by those meshes. This initializer discretizes that volume by dividing the asset’s [`boundingBox`](mdlasset/boundingbox.md) coordinates into a three-dimensional grid. The `divisions` parameter determines the height of the grid in voxels. A single voxel is a cubic unit, so the width and depth of the grid in voxels is proportional to its height and the bounding box of the asset.

After dividing the bounding box into a grid, Model I/O generates a shell of voxels at the grid positions corresponding to points on the mesh’s surface. Each voxel is a [`MDLVoxelIndex`](mdlvoxelindex.md) value whose x, y, and z coordinates locate the voxel in the grid and whose w coordinate value is 0, indicating that the voxel is on the surface of the object.

If you pass a value greater than zero for the `interiorNBWidth` or `exteriorNBWidth` parameter, this initializer also generates voxel data for the grid positions within or outside of the surface. For example, if you pass an `interiorNBWidth` value of `2.5`, Model I/O generates concentric shells of voxels inside the surface such that the distance from each voxel to the surface is no greater than 2.5 units. For those voxels, the w coordinate indicates how many shells lie between that voxel and the surface shell.

## Parameters

- `asset`: An asset containing meshes whose volume is to be modeled as voxels.
- `divisions`: The number of divisions to create along the y-axis of the asset’s bounding box; that is, the height in voxels of the resulting voxel array.
- `interiorNBWidth`: The distance, in units of the asset’s root coordinate space, inside the object’s surface for which to generate additional voxels.
- `exteriorNBWidth`: The distance, in units of the asset’s root coordinate space, outside the object’s surface for which to generate additional voxels.
- `patchRadius`: The largest radius, in world space units, of patches to apply to create closed volumes from meshes in the asset.

## See Also

- [init(asset: MDLAsset, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)](mdlvoxelarray/init(asset:divisions:interiorshells:exteriorshells:patchradius:).md)
  Initializes a voxel array that models the volume of 3D objects in the specified asset and creates the specified number of voxel shells.
- [init(data: Data, boundingBox: MDLAxisAlignedBoundingBox, voxelExtent: Float)](mdlvoxelarray/init(data:boundingbox:voxelextent:).md)
  Initializes a voxel array with the specified voxel data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/init(asset:divisions:interiornbwidth:exteriornbwidth:patchradius:))*