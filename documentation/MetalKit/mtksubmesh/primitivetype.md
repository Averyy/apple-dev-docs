# primitiveType

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) MTLPrimitiveType primitiveType;
```

#### Discussion

Use this value for the `primitiveType` parameter in a call to [`drawIndexedPrimitives(type:indexCount:indexType:indexBuffer:indexBufferOffset:)`](../../Metal/mtlrendercommandencoder/drawindexedprimitives%28type,indexcount,indextype,indexbuffer,indexbufferoffset%29.md).

## See Also

### Properties used to Draw Indexed Primitives
- [var indexBuffer: MTKMeshBuffer](./indexbuffer.md)
  The index buffer used to render the submesh object.
- [var indexCount: Int](./indexcount.md)
  The number of indices in the index buffer.
- [var indexType: MTLIndexType](./indextype.md)
  The type of index data in the index buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtksubmesh/primitivetype)*