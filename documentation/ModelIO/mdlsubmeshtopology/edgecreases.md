# edgeCreases

**Framework**: Model I/O  
**Kind**: property

A buffer containing sharpness values to be applied to edges during surface subdivision.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var edgeCreases: (any MDLMeshBuffer)? { get set }
```

#### Discussion

Each entry in this buffer corresponds to a pair of entries in the [`edgeCreaseIndices`](mdlsubmeshtopology/edgecreaseindices.md) buffer that identifies a crease. The value of each entry determines the amount of smoothing to apply to the crease during surface subdivision—a value of zero completely smooths out the edge, and a value of one leaves the edge completely sharp.

Because the number of entries in this buffer is likely to be different than the number of entries in any other vertex buffer, it shouldn’t be interleaved with other data in the mesh.

## See Also

- [var edgeCreaseIndices: (any MDLMeshBuffer)?](mdlsubmeshtopology/edgecreaseindices.md)
  A buffer containing vertex indices that describe edges to be treated as creases during surface subdivision.
- [var edgeCreaseCount: Int](mdlsubmeshtopology/edgecreasecount.md)
  The number of entries in the edge creases buffers.
- [var vertexCreaseIndices: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreaseindices.md)
  A buffer containing vertex indices to be treated as creases during surface subdivision.
- [var vertexCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreases.md)
  A buffer containing sharpness values to be applied to points during surface subdivision.
- [var vertexCreaseCount: Int](mdlsubmeshtopology/vertexcreasecount.md)
  The number of entries in the vertex creases buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology/edgecreases)*