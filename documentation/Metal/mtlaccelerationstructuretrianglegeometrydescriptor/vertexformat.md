# vertexFormat

**Framework**: Metal  
**Kind**: property

The format of each vertex position in the vertex buffer property.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var vertexFormat: MTLAttributeFormat { get set }
```

#### Discussion

Set this property to a value that represents the pixel format of the data you assign to the [`vertexBuffer`](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer.md) property. The property’s default is [`MTLAttributeFormat.float3`](mtlattributeformat/float3.md).

## See Also

- [var vertexBuffer: (any MTLBuffer)?](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbuffer.md)
  A buffer that contains vertex data.
- [var vertexBufferOffset: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexbufferoffset.md)
  The offset, in bytes, for the first vertex in the vertex buffer.
- [var vertexStride: Int](mtlaccelerationstructuretrianglegeometrydescriptor/vertexstride.md)
  The stride, in bytes, between vertices in the vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuretrianglegeometrydescriptor/vertexformat)*