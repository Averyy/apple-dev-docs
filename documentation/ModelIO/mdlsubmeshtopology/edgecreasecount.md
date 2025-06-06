# edgeCreaseCount

**Framework**: Model I/O  
**Kind**: property

The number of entries in the edge creases buffers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var edgeCreaseCount: Int { get set }
```

#### Discussion

The [`edgeCreases`](mdlsubmeshtopology/edgecreases.md) buffer contains this number of crease values. Because each edge is composed of two vertices, the [`edgeCreaseIndices`](mdlsubmeshtopology/edgecreaseindices.md) buffer contains twice this number of vertex indices.

## See Also

- [var edgeCreaseIndices: (any MDLMeshBuffer)?](mdlsubmeshtopology/edgecreaseindices.md)
  A buffer containing vertex indices that describe edges to be treated as creases during surface subdivision.
- [var edgeCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/edgecreases.md)
  A buffer containing sharpness values to be applied to edges during surface subdivision.
- [var vertexCreaseIndices: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreaseindices.md)
  A buffer containing vertex indices to be treated as creases during surface subdivision.
- [var vertexCreases: (any MDLMeshBuffer)?](mdlsubmeshtopology/vertexcreases.md)
  A buffer containing sharpness values to be applied to points during surface subdivision.
- [var vertexCreaseCount: Int](mdlsubmeshtopology/vertexcreasecount.md)
  The number of entries in the vertex creases buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology/edgecreasecount)*