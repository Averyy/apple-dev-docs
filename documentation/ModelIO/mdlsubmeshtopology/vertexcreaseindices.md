# vertexCreaseIndices

**Framework**: Model I/O  
**Kind**: property

A buffer containing vertex indices to be treated as creases during surface subdivision.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var vertexCreaseIndices: (any MDLMeshBuffer)? { get set }
```

#### Discussion

Each of entry in this buffer identifies a vertex that is to be treated as a crease or point during surface subdivision. The buffer is sparse, containing only those vertex indices to be treated as creases. The corresponding entry in the [`vertexCreases`](mdlsubmeshtopology/vertexcreases.md) buffer provides a sharpness value for the crease.

Because the number of entries in this buffer is likely to be different than the number of entries in any other vertex buffer, it shouldn’t be interleaved with other data in the mesh.

## See Also

- [var edgeCreaseIndices: (any MDLMeshBuffer)?](mdlsubmeshtopology/edgecreaseindices.md)
  A buffer containing vertex indices that describe edges to be treated as creases during surface subdivision.
- [var edgeCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/edgecreases.md)
  A buffer containing sharpness values to be applied to edges during surface subdivision.
- [var edgeCreaseCount: Int](mdlsubmeshtopology/edgecreasecount.md)
  The number of entries in the edge creases buffers.
- [var vertexCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreases.md)
  A buffer containing sharpness values to be applied to points during surface subdivision.
- [var vertexCreaseCount: Int](mdlsubmeshtopology/vertexcreasecount.md)
  The number of entries in the vertex creases buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology/vertexcreaseindices)*