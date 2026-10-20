# index(ofSpatialLocation:)

**Framework**: Model I/O  
**Kind**: method

Returns voxel information corresponding to the specified point in the world coordinate space of the asset from which the voxel array was created.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func index(ofSpatialLocation location: vector_float3) -> MDLVoxelIndex
```

#### Return Value

An index describing both the location of the voxel within the three-dimensional grid of the voxel array and its relationship to the volume of the object modeled by the voxel array.

#### Discussion

The coordinate space for spatial locations of voxels is the world space of the asset from which the voxel array was created, or for voxel arrays created with the [`init(data:boundingBox:voxelExtent:)`](mdlvoxelarray/init(data:boundingbox:voxelextent:).md) initializer, the bounding box specified at initialization.

## Parameters

- `location`: A point in the world coordinate space of the asset from which the voxel array was created.

## See Also

- [var boundingBox: MDLAxisAlignedBoundingBox](mdlvoxelarray/boundingbox.md)
  The extent of the voxel array’s volume in world coordinate space.
- [func spatialLocation(ofIndex: MDLVoxelIndex) -> vector_float3](mdlvoxelarray/spatiallocation(ofindex:).md)
  Returns the location of the specified voxel in world coordinate space.
- [func voxelBoundingBox(atIndex: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox](mdlvoxelarray/voxelboundingbox(atindex:).md)
  Returns the extent of the specified voxel’s volume in the world coordinate space of the asset from which the voxel array was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/index(ofspatiallocation:))*