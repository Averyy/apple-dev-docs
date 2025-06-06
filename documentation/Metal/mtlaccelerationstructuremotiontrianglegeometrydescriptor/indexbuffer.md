# indexBuffer

**Framework**: Metal  
**Kind**: property

A buffer that contains indices for the vertices that compose the triangle list.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var indexBuffer: (any MTLBuffer)? { get set }
```

#### Discussion

This property can be `nil`, in which case the vertex data defines the triangle list implicitly. You must store indices in a packed data format.

## See Also

- [var indexType: MTLIndexType](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indextype.md)
  The data type of indices in the index buffer.
- [var indexBufferOffset: Int](mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbufferoffset.md)
  The offset, in bytes, to the first index in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/indexbuffer)*