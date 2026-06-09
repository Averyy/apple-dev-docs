# LowLevelMeshResource.Attribute

**Framework**: RealityKit  
**Kind**: struct

An object that determines how to store vertex attribute data in memory and map it to RealityKit custom shader attributes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Attribute
```

## Topics

### Initializers
- [init()](lowlevelmeshresource/attribute/init.md)
  Creates an attribute with all fields set to their zero/default values.
- [init(semantic: LowLevelMeshResource.VertexSemantic, format: MTLVertexFormat, layoutIndex: Int, offset: Int)](lowlevelmeshresource/attribute/init(semantic:format:layoutindex:offset:).md)
  Creates an attribute with the given semantic, format, layout index, and byte offset.
### Instance Properties
- [var format: MTLVertexFormat](lowlevelmeshresource/attribute/format.md)
  The format of the vertex attribute.
- [var layoutIndex: Int](lowlevelmeshresource/attribute/layoutindex.md)
  The index of the layout that contains this attribute.
- [var offset: Int](lowlevelmeshresource/attribute/offset.md)
  The location of an attribute in vertex data, determined by the byte offset from the start of the vertex data.
- [var semantic: LowLevelMeshResource.VertexSemantic](lowlevelmeshresource/attribute/semantic.md)
  The semantic of the vertex attribute, which describes how you want the renderer to interpret the attribute.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var descriptor: LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.property.md)
  The descriptor used to create this mesh resource.
- [LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMeshResource.Layout](lowlevelmeshresource/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMeshResource.VertexSemantic](lowlevelmeshresource/vertexsemantic.md)
  The intended usage of a vertex attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/attribute)*