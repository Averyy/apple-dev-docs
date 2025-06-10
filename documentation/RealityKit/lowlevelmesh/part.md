# LowLevelMesh.Part

**Framework**: RealityKit  
**Kind**: struct

An object that describes a range of primitives to display, and their material index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct Part
```

## Topics

### Creating a low-level mesh part
- [init(indexOffset: Int, indexCount: Int, topology: MTLPrimitiveType, materialIndex: Int, bounds: BoundingBox)](lowlevelmesh/part/init(indexoffset:indexcount:topology:materialindex:bounds:).md)
  Creates a low-level mesh part.
### Describing a low-level mesh part
- [var indexOffset: Int](lowlevelmesh/part/indexoffset.md)
  The offset, in bytes, of the first index.
- [var indexCount: Int](lowlevelmesh/part/indexcount.md)
  The number of indices to use for this part.
- [var topology: MTLPrimitiveType](lowlevelmesh/part/topology.md)
  The geometric primitive to use when rendering this part.
- [var materialIndex: Int](lowlevelmesh/part/materialindex.md)
  The material index this part associates with.
- [var bounds: BoundingBox](lowlevelmesh/part/bounds.md)
  The model-space bounding box of this part.

## Relationships

### Conforms To
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
- [LowLevelMesh.Layout](lowlevelmesh/layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMesh.Attribute](lowlevelmesh/attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.VertexSemantic](lowlevelmesh/vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelMesh.PartsCollection](lowlevelmesh/partscollection.md)
  An object that holds a mutable collection low-level mesh parts.
- [class LowLevelBuffer](lowlevelbuffer.md)
- [class LowLevelInstanceData](lowlevelinstancedata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/part)*