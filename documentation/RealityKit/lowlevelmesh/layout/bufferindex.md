# bufferIndex

**Framework**: RealityKit  
**Kind**: property

The index of the buffer to use for this layout.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var bufferIndex: Int
```

#### Discussion

Most usage scenarios only use one buffer. Use a buffer index that is less than [`vertexBufferCount`](lowlevelmesh/descriptor-swift.struct/vertexbuffercount.md).

## See Also

- [var bufferOffset: Int](lowlevelmesh/layout/bufferoffset.md)
  The byte offset into the buffer for the first byte of this layout.
- [var bufferStride: Int](lowlevelmesh/layout/bufferstride.md)
  The distance, in bytes, between consecutive vertices for attributes using this layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/layout/bufferindex)*