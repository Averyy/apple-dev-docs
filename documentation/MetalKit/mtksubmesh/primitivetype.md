# primitiveType

**Framework**: MetalKit  
**Kind**: property

The primitive type with which to draw the submesh object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var primitiveType: MTLPrimitiveType { get }
```

#### Discussion

Use this value for the `primitiveType` parameter in a call to [`drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:)`](https://developer.apple.com/documentation/Metal/MTLRenderCommandEncoder/drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:)).

## See Also

- [var indexBuffer: MTKMeshBuffer](mtksubmesh/indexbuffer.md)
  The index buffer used to render the submesh object.
- [var indexCount: Int](mtksubmesh/indexcount.md)
  The number of indices in the index buffer.
- [var indexType: MTLIndexType](mtksubmesh/indextype.md)
  The type of index data in the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtksubmesh/primitivetype)*