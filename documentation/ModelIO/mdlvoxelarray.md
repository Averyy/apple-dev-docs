# MDLVoxelArray

**Framework**: Model I/O  
**Kind**: class

A model of a 3D object’s solid volume as a collection of , or cubic units.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLVoxelArray
```

#### Overview

Unlike a mesh, which models only surface topology, a voxel array models the solid volume of a 3D object. Voxels are useful for modeling volumetric phenomena (such as clouds and fire), performing solid geometry operations (such as intersection and union), and preparing a 3D design for real-world physical production.

## Topics

### Creating a Voxel Array
- [init(asset: MDLAsset, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)](mdlvoxelarray/init(asset:divisions:interiorshells:exteriorshells:patchradius:).md)
  Initializes a voxel array that models the volume of 3D objects in the specified asset and creates the specified number of voxel shells.
- [init(asset: MDLAsset, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)](mdlvoxelarray/init(asset:divisions:interiornbwidth:exteriornbwidth:patchradius:).md)
  Initializes a voxel array that models the volume of 3D objects in the specified asset, creating voxel shells for the specified distances from the object’s surface.
- [init(data: Data, boundingBox: MDLAxisAlignedBoundingBox, voxelExtent: Float)](mdlvoxelarray/init(data:boundingbox:voxelextent:).md)
  Initializes a voxel array with the specified voxel data.
### Examining Voxels
- [var count: Int](mdlvoxelarray/count.md)
  The number of voxels in the array.
- [var voxelIndexExtent: MDLVoxelIndexExtent](mdlvoxelarray/voxelindexextent.md)
  The indexes that define the corners of the three-dimensional voxel grid.
- [func voxelExists(atIndex: MDLVoxelIndex, allowAnyX: Bool, allowAnyY: Bool, allowAnyZ: Bool, allowAnyShell: Bool) -> Bool](mdlvoxelarray/voxelexists(atindex:allowanyx:allowanyy:allowanyz:allowanyshell:).md)
  Returns a Boolean value indicating whether the voxel array contains voxel data for the specified index.
- [func voxels(within: MDLVoxelIndexExtent) -> Data?](mdlvoxelarray/voxels(within:).md)
  Returns a data object containing all voxels within the specified volume.
- [func voxelIndices() -> Data?](mdlvoxelarray/voxelindices.md)
  Returns a data object containing all voxels within the voxel array.
### Modifying Voxels
- [func setVoxelAtIndex(MDLVoxelIndex)](mdlvoxelarray/setvoxelatindex(_:).md)
  Sets voxel characteristics at the specified index in the array.
- [func setVoxelsFor(MDLMesh, divisions: Int32, interiorNBWidth: Float, exteriorNBWidth: Float, patchRadius: Float)](mdlvoxelarray/setvoxelsfor(_:divisions:interiornbwidth:exteriornbwidth:patchradius:).md)
  Sets voxel values in the array to model the volume of the specified mesh and creates voxel shells for the specified distances from the object’s surface.
- [func setVoxelsFor(MDLMesh, divisions: Int32, interiorShells: Int32, exteriorShells: Int32, patchRadius: Float)](mdlvoxelarray/setvoxelsfor(_:divisions:interiorshells:exteriorshells:patchradius:).md)
  Sets voxel values in the array to model the volume of the specified mesh and creates the specified number of voxel shells.
### Performing Constructive Solid Geometry Operations
- [func union(with: MDLVoxelArray)](mdlvoxelarray/union(with:).md)
  Extends the voxel array to also cover the volume of the specified voxel array.
- [func intersect(with: MDLVoxelArray)](mdlvoxelarray/intersect(with:).md)
  Reduces the voxel array to cover only the volume within both it and another voxel array.
- [func difference(with: MDLVoxelArray)](mdlvoxelarray/difference(with:).md)
  Reduces the voxel array to cover only the portion of its volume not covered by another voxel array.
### Relating Voxels to Scene Space
- [var boundingBox: MDLAxisAlignedBoundingBox](mdlvoxelarray/boundingbox.md)
  The extent of the voxel array’s volume in world coordinate space.
- [func index(ofSpatialLocation: vector_float3) -> MDLVoxelIndex](mdlvoxelarray/index(ofspatiallocation:).md)
  Returns voxel information corresponding to the specified point in the world coordinate space of the asset from which the voxel array was created.
- [func spatialLocation(ofIndex: MDLVoxelIndex) -> vector_float3](mdlvoxelarray/spatiallocation(ofindex:).md)
  Returns the location of the specified voxel in world coordinate space.
- [func voxelBoundingBox(atIndex: MDLVoxelIndex) -> MDLAxisAlignedBoundingBox](mdlvoxelarray/voxelboundingbox(atindex:).md)
  Returns the extent of the specified voxel’s volume in the world coordinate space of the asset from which the voxel array was created.
### Creating a Mesh from Voxels
- [func mesh(using: (any MDLMeshBufferAllocator)?) -> MDLMesh?](mdlvoxelarray/mesh(using:).md)
  Generates a closed polygon mesh around the volume of space the voxel array describes.
### Constants
- [typealias MDLVoxelIndex](mdlvoxelindex.md)
  A 4-component vector encoding the location of a voxel in a voxel array and describing its relation to an object’s volume.
- [struct MDLVoxelIndexExtent](mdlvoxelindexextent.md)
  The corner voxel indices defining a solid rectangular volume of voxels. Used by the [`voxelIndexExtent`](mdlvoxelarray/voxelindexextent.md) property and [`voxels(within:)`](mdlvoxelarray/voxels(within:).md) method.
### Initializers
- [init(asset: MDLAsset, divisions: Int32, patchRadius: Float)](mdlvoxelarray/init(asset:divisions:patchradius:).md)
### Instance Properties
- [var isValidSignedShellField: Bool](mdlvoxelarray/isvalidsignedshellfield.md)
- [var shellFieldExteriorThickness: Float](mdlvoxelarray/shellfieldexteriorthickness.md)
- [var shellFieldInteriorThickness: Float](mdlvoxelarray/shellfieldinteriorthickness.md)
### Instance Methods
- [func coarseMesh() -> MDLMesh?](mdlvoxelarray/coarsemesh.md)
- [func coarseMesh(using: (any MDLMeshBufferAllocator)?) -> MDLMesh?](mdlvoxelarray/coarsemesh(using:).md)
- [func convertToSignedShellField()](mdlvoxelarray/converttosignedshellfield.md)
- [func setVoxelsFor(MDLMesh, divisions: Int32, patchRadius: Float)](mdlvoxelarray/setvoxelsfor(_:divisions:patchradius:).md)

## Relationships

### Inherits From
- [MDLObject](mdlobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray)*