# LowLevelMeshResource.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that describes the data format and layout of the buffers in a low-level mesh.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Descriptor
```

## Overview

The descriptor is analogous to `MTLVertexDescriptor`, with additional semantics that make vertex data available in shaders.

## Topics

### Creating a descriptor
- [init(vertexCapacity: Int, vertexAttributes: [LowLevelMeshResource.Attribute], vertexLayouts: [LowLevelMeshResource.Layout], indexCapacity: Int, indexType: MTLIndexType, instanceCapacity: Int)](./descriptor-swift.struct/init%28vertexcapacity,vertexattributes,vertexlayouts,indexcapacity,indextype,instancecapacity%29.md)
  Creates a mesh descriptor with the given vertex capacity, attributes, layouts, index capacity, index type, and instance capacity.
### Configuring instancing
- [var instanceCapacity: Int](./descriptor-swift.struct/instancecapacity.md)
  The maximum number of instances the mesh supports when using per-instance vertex data.
### Instance Properties
- [var indexCapacity: Int](./descriptor-swift.struct/indexcapacity.md)
  The maximum number of indices to allocate space for.
- [var indexType: MTLIndexType](./descriptor-swift.struct/indextype.md)
  The data type of the values stored in the index buffer.
- [var vertexAttributes: [LowLevelMeshResource.Attribute]](./descriptor-swift.struct/vertexattributes.md)
  The vertex input attributes.
- [var vertexBufferCount: Int](./descriptor-swift.struct/vertexbuffercount.md)
  The number of buffers this descriptor uses.
- [var vertexCapacity: Int](./descriptor-swift.struct/vertexcapacity.md)
  The maximum number of vertices to allocate space for.
- [var vertexLayouts: [LowLevelMeshResource.Layout]](./descriptor-swift.struct/vertexlayouts.md)
  The vertex buffer layouts.
### Type Properties
- [static let maxVertexBufferCount: Int](./descriptor-swift.struct/maxvertexbuffercount.md)
  The maximum number of separate vertex buffers the renderer supports.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing the mesh layout
- [var descriptor: LowLevelMeshResource.Descriptor](./descriptor-swift.property.md)
  The descriptor used to create this mesh resource.
- [LowLevelMeshResource.Layout](./layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMeshResource.Attribute](./attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit custom shader attributes.
- [LowLevelMeshResource.VertexSemantic](./vertexsemantic.md)
  The intended usage of a vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/descriptor-swift.struct)*