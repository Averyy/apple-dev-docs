# layouts

**Framework**: Model I/O  
**Kind**: property

The list of vertex buffer layouts described by the vertex descriptor.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var layouts: NSMutableArray { get set }
```

#### Discussion

A [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object describes the layout of data in one of the vertex buffers of a of a [`MDLMesh`](mdlmesh.md) object.

For meshes whose vertex data is split into multiple vertex buffers (a  design), the order of objects in this array reflects the order of buffers in the mesh’s [`vertexBuffers`](mdlmesh/vertexbuffers.md) array, which in turn parallels the order of vertex attributes in the descriptor’s [`attributes`](mdlvertexdescriptor/attributes.md) array. If a mesh contains interleaved data in a single vertex buffer (an  design), the descriptor contains only one [`MDLVertexBufferLayout`](mdlvertexbufferlayout.md) object, which describes the offset between entries for consecutive vertices in the buffer.

## See Also

- [func setPackedStrides()](mdlvertexdescriptor/setpackedstrides.md)
  Sets the stride for each vertex layout to the minimum value to pack vertex data together in a single buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexdescriptor/layouts)*