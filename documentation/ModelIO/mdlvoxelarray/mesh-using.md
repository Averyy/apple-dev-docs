# mesh(using:)

**Framework**: Model I/O  
**Kind**: method

Generates a closed polygon mesh around the volume of space the voxel array describes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func mesh(using allocator: (any MDLMeshBufferAllocator)?) -> MDLMesh?
```

#### Return Value

A new mesh object.

#### Discussion

Use this method to create a polygon mesh for use in rendering the object described by the voxel array.

The `allocator` parameter controls vertex data allocation for the mesh. For example, to use the MetalKit framework for loading vertex data into GPU buffers for rendering using Metal, pass a [`MTKMeshBufferAllocator`](https://developer.apple.com/documentation/MetalKit/MTKMeshBufferAllocator) object. By specifying an allocator, you can ensure that mesh data is copied a minimal number of times between being generated and being loaded into GPU memory for rendering.

## Parameters

- `allocator`: An object responsible for allocating mesh vertex data. If  , Model I/O uses an internal allocator object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvoxelarray/mesh(using:))*