# src_size

**Framework**: Compression  
**Kind**: property  
**Role**: Instance Property

The size, in bytes, of the source buffer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var src_size: Int
```

```c
size_t src_size;
```

## See Also

### Compression Stream Properties
- [var dst_ptr: UnsafeMutablePointer<UInt8>](./dst_ptr.md)
  A pointer to the first byte of the destination buffer.
- [var dst_size: Int](./dst_size.md)
  The size, in bytes, of the destination buffer.
- [var src_ptr: UnsafePointer<UInt8>](./src_ptr.md)
  A pointer to the first byte of the source buffer.
- [var state: UnsafeMutableRawPointer?](./state.md)
  The stream state object of the compression stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_stream/src_size)*