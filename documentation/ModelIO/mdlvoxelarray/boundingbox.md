# boundingBox

**Framework**: Model I/O  
**Kind**: property

The extent of the voxel array’s volume in world coordinate space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBox: MDLAxisAlignedBoundingBox { get }
```

#### Discussion

The coordinate space for the bounding box is the world space of the asset from which the voxel array was created, or for voxel arrays created with the [`init(data:boundingBox:voxelExtent:)`](mdlvoxelarray/init(data:boundingbox:voxelextent:).md) initializer, the bounding box specified at initialization.

## See Also

- [func index(ofSpatialLocation: vector_float3) -> MDLVoxelIndex](mdlvoxelarray/index(ofspatiallocation:).md)
  Returns voxel information corresponding to the specified point in the world coordinate space of the asset from which the voxel array was created.
- [func spatialLocation(ofIndex: MDLVoxelIndex) -> vector_float3](mdlvoxelarray/spatiallocation(ofindex:).md)
  Returns the location of the specified voxel in world coordinate space.
- [func voxelBoundingBox(atIndex: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox](mdlvoxelarray/voxelboundingbox(atindex:).md)
  Returns the extent of the specified voxel’s volume in the world coordinate space of the asset from which the voxel array was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/boundingbox)*