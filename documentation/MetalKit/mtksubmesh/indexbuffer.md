# indexBuffer

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The index buffer used to render the submesh object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var indexBuffer: MTKMeshBuffer { get }
```

```objc
@property (nonatomic, readonly, nonnull) MTKMeshBuffer * indexBuffer;
```

## Discussion

Use this object for the `indexBuffer` parameter in a call to [`drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:)`](../../Metal/mtlrendercommandencoder/drawindexedprimitives%28type,indexcount,indextype,indexbuffer,indexbufferoffset%29.md).

## See Also

### Properties used to Draw Indexed Primitives
- [var indexCount: Int](./indexcount.md)
  The number of indices in the index buffer.
- [var indexType: MTLIndexType](./indextype.md)
  The type of index data in the index buffer.
- [var primitiveType: MTLPrimitiveType](./primitivetype.md)
  The primitive type with which to draw the submesh object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtksubmesh/indexbuffer)*