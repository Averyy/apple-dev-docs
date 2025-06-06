# state

**Framework**: Compression  
**Kind**: property

The stream state object of the compression stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var state: UnsafeMutableRawPointer?
```

#### Discussion

You should not directly access this field.

## See Also

- [var dst_ptr: UnsafeMutablePointer<UInt8>](compression_stream/dst_ptr.md)
  A pointer to the first byte of the destination buffer.
- [var dst_size: Int](compression_stream/dst_size.md)
  The size, in bytes, of the destination buffer.
- [var src_ptr: UnsafePointer<UInt8>](compression_stream/src_ptr.md)
  A pointer to the first byte of the source buffer.
- [var src_size: Int](compression_stream/src_size.md)
  The size, in bytes, of the source buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_stream/state)*