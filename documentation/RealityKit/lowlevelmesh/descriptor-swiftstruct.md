# LowLevelMesh.Descriptor

**Framework**: RealityKit  
**Kind**: struct

An object that describes the data format and layout of the buffers in a low-level mesh.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a low-level mesh descriptor
- [init(vertexCapacity: Int, vertexAttributes: [LowLevelMesh.Attribute], vertexLayouts: [LowLevelMesh.Layout], indexCapacity: Int, indexType: MTLIndexType)](lowlevelmesh/descriptor-swift.struct/init(vertexcapacity:vertexattributes:vertexlayouts:indexcapacity:indextype:).md)
  Creates a descriptor for a low-level mesh.
### Defining the descriptor’s contents
- [var indexType: MTLIndexType](lowlevelmesh/descriptor-swift.struct/indextype.md)
  The data type of the indices that the index buffer stores.
- [var vertexAttributes: [LowLevelMesh.Attribute]](lowlevelmesh/descriptor-swift.struct/vertexattributes.md)
  An array that describes the vertex input attributes to a vertex function.
- [var vertexLayouts: [LowLevelMesh.Layout]](lowlevelmesh/descriptor-swift.struct/vertexlayouts.md)
  The list of layouts.
- [var vertexBufferCount: Int](lowlevelmesh/descriptor-swift.struct/vertexbuffercount.md)
  The number of buffers this descriptor uses.
### Defining the descriptor’s limits
- [var vertexCapacity: Int](lowlevelmesh/descriptor-swift.struct/vertexcapacity.md)
  The number of vertices to allocate space for.
- [var indexCapacity: Int](lowlevelmesh/descriptor-swift.struct/indexcapacity.md)
  The number of indices to allocate space for.
- [static let maxVertexBufferCount: Int](lowlevelmesh/descriptor-swift.struct/maxvertexbuffercount.md)
  The maximum number of separate buffers the system supports.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Integrating virtual objects with your environment](integrating-virtual-objects-with-your-environment.md)
  Create an immersive game using native anchor support, environmental blending, model manipulation, and mesh instance duplication.
- [Creating a spatial drawing app with RealityKit](creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Creating a plane with low-level mesh](creating-a-plane-with-low-level-mesh.md)
  Create a low-level mesh and set its vertex positions and normals to form a plane.
- [class LowLevelMesh](lowlevelmesh.md)
  A container for vertex data that you can use to create and update meshes using your own format.
- [LowLevelMesh.Part](lowlevelmesh/part.md)
  An object that describes a range of primitives to display, and their material index.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/descriptor-swift.struct)*