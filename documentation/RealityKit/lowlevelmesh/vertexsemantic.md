# LowLevelMesh.VertexSemantic

**Framework**: RealityKit  
**Kind**: enum

Designates the intended usage of a vertex attribute.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
enum VertexSemantic
```

#### Overview

RealityKit consults the vertex semantic when interpreting the data in your [`LowLevelMesh`](lowlevelmesh.md). For example, an attribute with the semantic value of [`LowLevelMesh.VertexSemantic.position`](lowlevelmesh/vertexsemantic/position.md) determines the position of a vertex.

## Topics

### Specifying intended use
- [LowLevelMesh.VertexSemantic.bitangent](lowlevelmesh/vertexsemantic/bitangent.md)
  The semantic for surface bitangent vector data.
- [LowLevelMesh.VertexSemantic.color](lowlevelmesh/vertexsemantic/color.md)
  The semantic for per-vertex color data.
- [LowLevelMesh.VertexSemantic.normal](lowlevelmesh/vertexsemantic/normal.md)
  The semantic for surface normal data.
- [LowLevelMesh.VertexSemantic.position](lowlevelmesh/vertexsemantic/position.md)
  The semantic for vertex position data.
- [LowLevelMesh.VertexSemantic.tangent](lowlevelmesh/vertexsemantic/tangent.md)
  The semantic for surface tangent vector data.
- [LowLevelMesh.VertexSemantic.unspecified](lowlevelmesh/vertexsemantic/unspecified.md)
  The semantic that doesn’t specify the role of the vertex.
- [LowLevelMesh.VertexSemantic.uv0](lowlevelmesh/vertexsemantic/uv0.md)
  The semantic for the first UV channel, also known as UV0.
- [LowLevelMesh.VertexSemantic.uv1](lowlevelmesh/vertexsemantic/uv1.md)
  The semantic for the second UV channel, also known as UV1.
- [LowLevelMesh.VertexSemantic.uv2](lowlevelmesh/vertexsemantic/uv2.md)
  The semantic for the third UV channel, also known as UV2.
- [LowLevelMesh.VertexSemantic.uv3](lowlevelmesh/vertexsemantic/uv3.md)
  The semantic for the fourth UV channel, also known as UV3.
- [LowLevelMesh.VertexSemantic.uv4](lowlevelmesh/vertexsemantic/uv4.md)
  The semantic for the fifth UV channel, also known as UV4.
- [LowLevelMesh.VertexSemantic.uv5](lowlevelmesh/vertexsemantic/uv5.md)
  The semantic for the sixth UV channel, also known as UV5.
- [LowLevelMesh.VertexSemantic.uv6](lowlevelmesh/vertexsemantic/uv6.md)
  The semantic for the seventh UV channel, also known as UV6.
- [LowLevelMesh.VertexSemantic.uv7](lowlevelmesh/vertexsemantic/uv7.md)
  The semantic for the eighth UV channel, also known as UV7.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)
  Create a low-level mesh and set its vertex positions and normals to form a plane.
- [class LowLevelMesh](lowlevelmesh.md)
  A container for vertex data that you can use to create and update meshes using your own format.
- [LowLevelMesh.Descriptor](lowlevelmesh/descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMesh.Part](lowlevelmesh/part.md)
  An object that describes a range of primitives to display, and their material index.
- [LowLevelMesh.Layout](lowlevelmesh/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMesh.Attribute](lowlevelmesh/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.PartsCollection](lowlevelmesh/partscollection.md)
  An object that holds a mutable collection low-level mesh parts.
- [class LowLevelBuffer](lowlevelbuffer.md)
- [class LowLevelInstanceData](lowlevelinstancedata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/vertexsemantic)*