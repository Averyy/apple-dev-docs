# LowLevelMeshResource.VertexSemantic

**Framework**: RealityKit  
**Kind**: enum

The intended usage of a vertex attribute.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum VertexSemantic
```

#### Overview

The renderer consults the vertex semantic when interpreting the data in a `LowLevelMeshResource`. For example, an attribute with the semantic value of [`LowLevelMeshResource.VertexSemantic.position`](lowlevelmeshresource/vertexsemantic/position.md) determines the position of a vertex.

## Topics

### Identifying geometric attributes
- [LowLevelMeshResource.VertexSemantic.position](lowlevelmeshresource/vertexsemantic/position.md)
  The semantic for vertex position data.
- [LowLevelMeshResource.VertexSemantic.normal](lowlevelmeshresource/vertexsemantic/normal.md)
  The semantic for surface normal data.
- [LowLevelMeshResource.VertexSemantic.tangent](lowlevelmeshresource/vertexsemantic/tangent.md)
  The semantic for surface tangent vector data.
- [LowLevelMeshResource.VertexSemantic.bitangent](lowlevelmeshresource/vertexsemantic/bitangent.md)
  The semantic for surface bitangent vector data.
- [LowLevelMeshResource.VertexSemantic.color](lowlevelmeshresource/vertexsemantic/color.md)
  The semantic for per-vertex color data.
### Identifying texture coordinates
- [LowLevelMeshResource.VertexSemantic.uv0](lowlevelmeshresource/vertexsemantic/uv0.md)
  The semantic for the first UV channel (UV0).
- [LowLevelMeshResource.VertexSemantic.uv1](lowlevelmeshresource/vertexsemantic/uv1.md)
  The semantic for the second UV channel (UV1). A shader can access this generic data.
- [LowLevelMeshResource.VertexSemantic.uv2](lowlevelmeshresource/vertexsemantic/uv2.md)
  The semantic for the third UV channel (UV2). A shader can access this generic data.
- [LowLevelMeshResource.VertexSemantic.uv3](lowlevelmeshresource/vertexsemantic/uv3.md)
  The semantic for the fourth UV channel (UV3). A shader can access this generic data.
- [LowLevelMeshResource.VertexSemantic.uv4](lowlevelmeshresource/vertexsemantic/uv4.md)
  The semantic for the fifth UV channel (UV4). A shader can access this generic data.
- [LowLevelMeshResource.VertexSemantic.uv5](lowlevelmeshresource/vertexsemantic/uv5.md)
  The semantic for the sixth UV channel (UV5). A shader can access this generic data.
- [LowLevelMeshResource.VertexSemantic.uv6](lowlevelmeshresource/vertexsemantic/uv6.md)
  The semantic for the seventh UV channel (UV6). A shader can access this generic data.
- [LowLevelMeshResource.VertexSemantic.uv7](lowlevelmeshresource/vertexsemantic/uv7.md)
  The semantic for the eighth UV channel (UV7). A shader can access this generic data.
### Handling unspecified semantics
- [LowLevelMeshResource.VertexSemantic.unspecified](lowlevelmeshresource/vertexsemantic/unspecified.md)
  A semantic that doesn’t specify the role of the vertex.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var descriptor: LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.property.md)
  The descriptor used to create this mesh resource.
- [LowLevelMeshResource.Descriptor](lowlevelmeshresource/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMeshResource.Layout](lowlevelmeshresource/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMeshResource.Attribute](lowlevelmeshresource/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit custom shader attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshresource/vertexsemantic)*