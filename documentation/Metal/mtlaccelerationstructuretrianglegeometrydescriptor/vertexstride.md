# vertexStride

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The stride, in bytes, between vertices in the vertex buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var vertexStride: Int { get set }
```

```objc
@property (nonatomic) NSUInteger vertexStride;
```

## Discussion

The stride needs to be at least 12 bytes and needs to be a multiple of 4 bytes. The default value is 12 bytes.

## See Also

### Configuring vertex data
- [var vertexFormat: MTLAttributeFormat](./vertexformat.md)
  The format of each vertex position in the vertex buffer property.
- [var vertexBuffer: (any MTLBuffer)?](./vertexbuffer.md)
  A buffer that contains vertex data.
- [var vertexBufferOffset: Int](./vertexbufferoffset.md)
  The offset, in bytes, for the first vertex in the vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride)*