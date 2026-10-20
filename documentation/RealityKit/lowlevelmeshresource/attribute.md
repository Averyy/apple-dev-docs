# LowLevelMeshResource.Attribute

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that determines how to store vertex attribute data in memory and map it to RealityKit custom shader attributes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Attribute
```

## Topics

### Initializers
- [init()](./attribute/init%28%29.md)
  Creates an attribute with all fields set to their zero/default values.
- [init(semantic: LowLevelMeshResource.VertexSemantic, format: MTLVertexFormat, layoutIndex: Int, offset: Int)](./attribute/init%28semantic,format,layoutindex,offset%29.md)
  Creates an attribute with the given semantic, format, layout index, and byte offset.
### Instance Properties
- [var format: MTLVertexFormat](./attribute/format.md)
  The format of the vertex attribute.
- [var layoutIndex: Int](./attribute/layoutindex.md)
  The index of the layout that contains this attribute.
- [var offset: Int](./attribute/offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [var semantic: LowLevelMeshResource.VertexSemantic](./attribute/semantic.md)
  The semantic of the vertex attribute, which describes how you want the renderer to interpret the attribute.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing the mesh layout
- [var descriptor: LowLevelMeshResource.Descriptor](./descriptor-swift.property.md)
  The descriptor used to create this mesh resource.
- [LowLevelMeshResource.Descriptor](./descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMeshResource.Layout](./layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMeshResource.VertexSemantic](./vertexsemantic.md)
  The intended usage of a vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/attribute)*