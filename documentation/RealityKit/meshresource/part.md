# MeshResource.Part

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A part of a model consisting of a single material.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Part
```

## Topics

### Initializers
- [init(id: String, materialIndex: Int)](./part/init%28id,materialindex%29.md)
  Create a new part.
### Instance Properties
- [var jointInfluences: MeshResource.JointInfluences?](./part/jointinfluences.md)
  A buffer of vertex-joint influences which defines how the mesh deforms in response to the skeleton that it is bound to. Each vertex may be influenced by one or more joints defined by the skeleton.
- [var materialIndex: Int](./part/materialindex.md)
  Material index for the part.
- [var skeletonID: String?](./part/skeletonid.md)
  Identifier of the skeleton that this mesh part is bound to (if it is skinned).
- [var triangleIndices: MeshBuffers.TriangleIndices?](./part/triangleindices.md)
  Index buffer for triangles.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)
- [MeshBufferContainer](../meshbuffercontainer.md)

## See Also

### Mesh resource data
- [MeshResource.Contents](./contents-swift.struct.md)
  Value of the contents of the resource.
- [MeshResource.Instance](./instance.md)
  An object that transforms a model to a location.
- [MeshResource.Model](./model.md)
  A model consists of a list of parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/part)*