# LowLevelMesh.Part

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that describes a range of primitives to display, and their material index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Part
```

## Topics

### Creating a low-level mesh part
- [init(indexOffset: Int, indexCount: Int, topology: MTLPrimitiveType, materialIndex: Int, bounds: BoundingBox)](./part/init%28indexoffset,indexcount,topology,materialindex,bounds%29.md)
  Creates a low-level mesh part.
### Describing a low-level mesh part
- [var indexOffset: Int](./part/indexoffset.md)
  The offset, in bytes, of the first index.
- [var indexCount: Int](./part/indexcount.md)
  The number of indices to use for this part.
- [var topology: MTLPrimitiveType](./part/topology.md)
  The geometric primitive to use when rendering this part.
- [var materialIndex: Int](./part/materialindex.md)
  The material index this part associates with.
- [var bounds: BoundingBox](./part/bounds.md)
  The model-space bounding box of this part.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Updatable meshes
- [Integrating virtual objects with your environment](../integrating-virtual-objects-with-your-environment.md)
  Create an immersive game using native anchor support, environmental blending, model manipulation, and mesh instance duplication.
- [Creating a spatial drawing app with RealityKit](../creating-a-spatial-drawing-app-with-realitykit.md)
  Use low-level mesh and texture APIs to achieve fast updates to a person’s brush strokes by integrating RealityKit with ARKit and SwiftUI.
- [Creating a plane with low-level mesh](../creating-a-plane-with-low-level-mesh.md)
  Create a low-level mesh and set its vertex positions and normals to form a plane.
- [class LowLevelMesh](../lowlevelmesh.md)
  A container for vertex data that you can use to create and update meshes using your own format.
- [LowLevelMesh.Descriptor](./descriptor-swift.struct.md)
  An object that describes the data format and layout of the buffers in a low-level mesh.
- [LowLevelMesh.Layout](./layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMesh.Attribute](./attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.VertexSemantic](./vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [LowLevelMesh.PartsCollection](./partscollection.md)
  An object that holds a mutable collection low-level mesh parts.
- [class LowLevelBuffer](../lowlevelbuffer.md)
- [class LowLevelInstanceData](../lowlevelinstancedata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/part)*