# edgeCreaseIndices

**Framework**: Model I/O  
**Kind**: property

A buffer containing vertex indices that describe edges to be treated as creases during surface subdivision.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var edgeCreaseIndices: (any MDLMeshBuffer)? { get set }
```

#### Discussion

Each pair of entries in this buffer identifies an edge, between two connected vertices in the submesh, that is to be treated as a crease during surface subdivision. The buffer is sparse, containing only those vertex indices to be treated as creases. The corresponding entry in the [`edgeCreases`](mdlsubmeshtopology/edgecreases.md) buffer provides a sharpness value for the crease.

Because the number of entries in this buffer is likely to be different than the number of entries in any other vertex buffer, it shouldn’t be interleaved with other data in the mesh.

## See Also

- [var edgeCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/edgecreases.md)
  A buffer containing sharpness values to be applied to edges during surface subdivision.
- [var edgeCreaseCount: Int](mdlsubmeshtopology/edgecreasecount.md)
  The number of entries in the edge creases buffers.
- [var vertexCreaseIndices: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreaseindices.md)
  A buffer containing vertex indices to be treated as creases during surface subdivision.
- [var vertexCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreases.md)
  A buffer containing sharpness values to be applied to points during surface subdivision.
- [var vertexCreaseCount: Int](mdlsubmeshtopology/vertexcreasecount.md)
  The number of entries in the vertex creases buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology/edgecreaseindices)*