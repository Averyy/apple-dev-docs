# init(data:boundingBox:voxelExtent:)

**Framework**: Model I/O  
**Kind**: init

Initializes a voxel array with the specified voxel data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(data voxelData: Data, boundingBox: MDLAxisAlignedBoundingBox, voxelExtent: Float)
```

#### Return Value

A new voxel array.

#### Discussion

The `boundingBox` parameter relates the integer grid of the newly created voxel array to a continuous Cartesian space. The methods listed in Relating Voxels to Scene Space and Creating a Mesh from Voxels operate with respect to this bounding volume.

## Parameters

- `voxelData`: A data object containing an array of   values, each of which describes the locations of voxels within the specified volume as well as their volumetric relationship to the object modeled by the voxel array.
- `boundingBox`: The extent of the voxel array’s volume in world coordinate space.
- `voxelExtent`: The size of a single voxel in world coordinate space.

## See Also

- [init(asset: MDLAsset, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)](mdlvoxelarray/init(asset:divisions:interiorshells:exteriorshells:patchradius:).md)
  Initializes a voxel array that models the volume of 3D objects in the specified asset and creates the specified number of voxel shells.
- [init(asset: MDLAsset, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)](mdlvoxelarray/init(asset:divisions:interiornbwidth:exteriornbwidth:patchradius:).md)
  Initializes a voxel array that models the volume of 3D objects in the specified asset, creating voxel shells for the specified distances from the object’s surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/init(data:boundingbox:voxelextent:))*