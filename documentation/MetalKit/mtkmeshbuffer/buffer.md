# buffer

**Framework**: MetalKit  
**Kind**: property

The Metal buffer backing all vertex and index data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var buffer: any MTLBuffer { get }
```

#### Discussion

Many [`MTKMeshBuffer`](mtkmeshbuffer.md) objects may reference the same [`MTLBuffer`](https://developer.apple.com/documentation/Metal/MTLBuffer) object, in which case each [`MTKMeshBuffer`](mtkmeshbuffer.md) object will have its own unique [`offset`](mtkmeshbuffer/offset.md) value.

## See Also

- [var length: Int](mtkmeshbuffer/length.md)
  The logical size of the Metal buffer, in bytes.
- [var offset: Int](mtkmeshbuffer/offset.md)
  The byte offset of the data within the Metal buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/buffer)*