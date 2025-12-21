# indexBufferOffset

**Framework**: Metal  
**Kind**: property

The offset, in bytes, to the first index in the buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var indexBufferOffset: Int { get set }
```

#### Discussion

Specify an offset that is a multiple of the index data type size and a multiple of the platform’s buffer offset alignment.

## See Also

- [var indexType: MTLIndexType](mtlaccelerationstructuretrianglegeometrydescriptor/indextype.md)
  The data type of indices in the index buffer.
- [var indexBuffer: (any MTLBuffer)?](mtlaccelerationstructuretrianglegeometrydescriptor/indexbuffer.md)
  A buffer that contains indices for the vertices that compose the triangle list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbufferoffset)*