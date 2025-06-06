# indexType

**Framework**: MetalKit  
**Kind**: property

The type of index data in the index buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var indexType: MTLIndexType { get }
```

#### Discussion

Use this value for the `indexType` parameter in a call to [`drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:)`](https://developer.apple.com/documentation/Metal/MTLRenderCommandEncoder/drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:)).

## See Also

- [var indexBuffer: MTKMeshBuffer](mtksubmesh/indexbuffer.md)
  The index buffer used to render the submesh object.
- [var indexCount: Int](mtksubmesh/indexcount.md)
  The number of indices in the index buffer.
- [var primitiveType: MTLPrimitiveType](mtksubmesh/primitivetype.md)
  The primitive type with which to draw the submesh object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtksubmesh/indextype)*