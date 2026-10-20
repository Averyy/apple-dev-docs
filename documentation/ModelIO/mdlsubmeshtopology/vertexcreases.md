# vertexCreases

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

A buffer containing sharpness values to be applied to points during surface subdivision.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var vertexCreases: (any MDLMeshBuffer)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MDLMeshBuffer> vertexCreases;
```

#### Discussion

Each entry in this buffer corresponds to an entry in the [`vertexCreaseIndices`](./vertexcreaseindices.md) buffer that identifies a crease. The value of each entry determines the amount of smoothing to apply to the crease during surface subdivision—a value of zero completely smooths out the point, and a value of one leaves the point completely sharp.

Because the number of entries in this buffer is likely to be different than the number of entries in any other vertex buffer, it shouldn’t be interleaved with other data in the mesh.

## See Also

### Identifying Creases
- [var edgeCreaseIndices: (any MDLMeshBuffer)?](./edgecreaseindices.md)
  A buffer containing vertex indices that describe edges to be treated as creases during surface subdivision.
- [var edgeCreases: (any MDLMeshBuffer)?](./edgecreases.md)
  A buffer containing sharpness values to be applied to edges during surface subdivision.
- [var edgeCreaseCount: Int](./edgecreasecount.md)
  The number of entries in the edge creases buffers.
- [var vertexCreaseIndices: (any MDLMeshBuffer)?](./vertexcreaseindices.md)
  A buffer containing vertex indices to be treated as creases during surface subdivision.
- [var vertexCreaseCount: Int](./vertexcreasecount.md)
  The number of entries in the vertex creases buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlsubmeshtopology/vertexcreases)*