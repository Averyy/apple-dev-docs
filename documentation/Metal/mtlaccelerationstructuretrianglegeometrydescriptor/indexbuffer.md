# indexBuffer

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A buffer that contains indices for the vertices that compose the triangle list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var indexBuffer: (any MTLBuffer)? { get set }
```

```objc
@property (nonatomic, retain, nullable) id<MTLBuffer> indexBuffer;
```

#### Discussion

This property can be `nil`, in which case the vertex data defines the triangle list implicitly. You need to store indices in a packed data format.

## See Also

### Configuring index data
- [var indexType: MTLIndexType](./indextype.md)
  The data type of indices in the index buffer.
- [var indexBufferOffset: Int](./indexbufferoffset.md)
  The offset, in bytes, to the first index in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/indexbuffer)*