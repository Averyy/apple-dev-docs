# MeshResource.Part

**Framework**: RealityKit  
**Kind**: struct

A part of a model consisting of a single material.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
struct Part
```

## Topics

### Initializers
- [init(id:materialIndex:)](meshresource/part-4ge48/init(id:materialindex:).md)
  Create a new part.
### Instance Properties
- [var jointInfluences: MeshResource.JointInfluences?](meshresource/part-3q1vw/jointinfluences.md)
  A buffer of vertex-joint influences which defines how the mesh deforms in response to the skeleton that it is bound to. Each vertex may be influenced by one or more joints defined by the skeleton.
- [var materialIndex: Int](meshresource/part-3q1vw/materialindex.md)
  Material index for the part.
- [var skeletonID: String?](meshresource/part-3q1vw/skeletonid.md)
  Identifier of the skeleton that this mesh part is bound to (if it is skinned).
- [var triangleIndices: MeshBuffers.TriangleIndices?](meshresource/part-3q1vw/triangleindices.md)
  Index buffer for triangles.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [MeshBufferContainer](meshbuffercontainer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/part-3q1vw)*