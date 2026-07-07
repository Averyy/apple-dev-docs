# LowLevelMeshResource.Descriptor

**Framework**: RealityKit  
**Kind**: struct

An object that describes the data format and layout of the buffers in a low-level mesh.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

#### Overview

The descriptor is analogous to `MTLVertexDescriptor`, with additional semantics that make vertex data available in shaders.

## Topics

### Creating a descriptor
- [init(vertexCapacity: Int, vertexAttributes: [LowLevelMeshResource.Attribute], vertexLayouts: [LowLevelMeshResource.Layout], indexCapacity: Int, indexType: MTLIndexType, instanceCapacity: Int)](lowlevelmeshresource/descriptor-swift.struct/init(vertexcapacity:vertexattributes:vertexlayouts:indexcapacity:indextype:instancecapacity:).md)
  Creates a mesh descriptor with the given vertex capacity, attributes, layouts, index capacity, index type, and instance capacity.
### Configuring instancing
- [var instanceCapacity: Int](lowlevelmeshresource/descriptor-swift.struct/instancecapacity.md)
  The maximum number of instances the mesh supports when using per-instance vertex data.
### Instance Properties
- [var indexCapacity: Int](lowlevelmeshresource/descriptor-swift.struct/indexcapacity.md)
  The maximum number of indices to allocate space for.
- [var indexType: MTLIndexType](lowlevelmeshresource/descriptor-swift.struct/indextype.md)
  The data type of the values stored in the index buffer.
- [var vertexAttributes: [LowLevelMeshResource.Attribute]](lowlevelmeshresource/descriptor-swift.struct/vertexattributes.md)
  The vertex input attributes.
- [var vertexBufferCount: Int](lowlevelmeshresource/descriptor-swift.struct/vertexbuffercount.md)
  The number of buffers this descriptor uses.
- [var vertexCapacity: Int](lowlevelmeshresource/descriptor-swift.struct/vertexcapacity.md)
  The maximum number of vertices to allocate space for.
- [var vertexLayouts: [LowLevelMeshResource.Layout]](lowlevelmeshresource/descriptor-swift.struct/vertexlayouts.md)
  The vertex buffer layouts.
### Type Properties
- [static let maxVertexBufferCount: Int](lowlevelmeshresource/descriptor-swift.struct/maxvertexbuffercount.md)
  The maximum number of separate vertex buffers the renderer supports.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var descriptor: LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.property.md)
  The descriptor used to create this mesh resource.
- [LowLevelMeshResource.Layout](lowlevelmeshresource/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMeshResource.Attribute](lowlevelmeshresource/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit custom shader attributes.
- [LowLevelMeshResource.VertexSemantic](lowlevelmeshresource/vertexsemantic.md)
  The intended usage of a vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/descriptor-swift.struct)*