# LowLevelMesh.PartsCollection

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that holds a mutable collection low-level mesh parts.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct PartsCollection
```

## Topics

### Updating collection contents
- [func append(LowLevelMesh.PartsCollection.Element)](./partscollection/append%28_%29.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](./partscollection/append%28contentsof%29.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func replaceAll<S>(S)](./partscollection/replaceall%28_%29.md)
  Replaces all mesh parts in this collection with those from the new sequence.
- [func removeAll()](./partscollection/removeall%28%29.md)
  Removes all mesh parts from this collection.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [MutableCollection](../../Swift/mutablecollection.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sequence](../../Swift/sequence.md)

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
- [LowLevelMesh.Part](./part.md)
  An object that describes a range of primitives to display, and their material index.
- [LowLevelMesh.Layout](./layout.md)
  An object that describes a set of attributes that share a buffer index, offset, and stride.
- [LowLevelMesh.Attribute](./attribute.md)
  An object that determines how to store vertex attribute data in memory and map it to RealityKit shader attributes.
- [LowLevelMesh.VertexSemantic](./vertexsemantic.md)
  Designates the intended usage of a vertex attribute.
- [class LowLevelBuffer](../lowlevelbuffer.md)
- [class LowLevelInstanceData](../lowlevelinstancedata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/partscollection)*