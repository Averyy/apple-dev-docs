# spatialLocation(ofIndex:)

**Framework**: Model I/O  
**Kind**: method

Returns the location of the specified voxel in world coordinate space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func spatialLocation(ofIndex index: MDLVoxelIndex) -> vector_float3
```

#### Return Value

The center point for the single voxel at the specified location, in the world coordinate space of the asset from which the voxel array was created.

#### Discussion

The coordinate space for spatial locations of voxels is the world space of the asset from which the voxel array was created, or for voxel arrays created with the [`init(data:boundingBox:voxelExtent:)`](mdlvoxelarray/init(data:boundingbox:voxelextent:).md) initializer, the bounding box specified at initialization.

## Parameters

- `index`: An index describing the location of a voxel within the three-dimensional grid of the voxel array. (The w component is ignored for this query.)

## See Also

- [var boundingBox: MDLAxisAlignedBoundingBox](mdlvoxelarray/boundingbox.md)
  The extent of the voxel array’s volume in world coordinate space.
- [func index(ofSpatialLocation: vector_float3) -> MDLVoxelIndex](mdlvoxelarray/index(ofspatiallocation:).md)
  Returns voxel information corresponding to the specified point in the world coordinate space of the asset from which the voxel array was created.
- [func voxelBoundingBox(atIndex: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox](mdlvoxelarray/voxelboundingbox(atindex:).md)
  Returns the extent of the specified voxel’s volume in the world coordinate space of the asset from which the voxel array was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/spatiallocation(ofindex:))*