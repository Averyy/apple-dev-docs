# indexType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The data type of indices in the index buffer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var indexType: MTLIndexType { get set }
```

```objc
@property (nonatomic) MTLIndexType indexType;
```

#### Discussion

The index type needs to be [`MTLIndexType.uint16`](../mtlindextype/uint16.md) or [`MTLIndexType.uint32`](../mtlindextype/uint32.md). The default is [`MTLIndexType.uint32`](../mtlindextype/uint32.md).

## See Also

### Specifying index data
- [var indexBuffer: (any MTLBuffer)?](./indexbuffer.md)
  A buffer that contains indices for the vertices that compose the triangle list.
- [var indexBufferOffset: Int](./indexbufferoffset.md)
  The offset, in bytes, to the first index in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype)*