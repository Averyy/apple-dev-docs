# compression_encode_scratch_buffer_size(_:)

**Framework**: Compression  
**Kind**: func

Returns the required compression scratch buffer size for the selected algorithm.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func compression_encode_scratch_buffer_size(_ algorithm: compression_algorithm) -> Int
```

#### Return Value

Size in bytes.

#### Discussion

This function returns the number of bytes to provide in an optional scratch buffer when calling [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md).

## Parameters

- `algorithm`: Set to the desired algorithm:  ,  ,  , or  .

## See Also

- [Compressing and decompressing data with buffer compression](../Accelerate/compressing-and-decompressing-data-with-buffer-compression.md)
  Compress a string, write it to the file system, and decompress the same file using buffer compression.
- [func compression_encode_buffer(UnsafeMutablePointer<UInt8>, Int, UnsafePointer<UInt8>, Int, UnsafeMutableRawPointer?, compression_algorithm) -> Int](compression_encode_buffer(_:_:_:_:_:_:).md)
  Compresses the contents of a source buffer into a destination buffer.
- [func compression_decode_scratch_buffer_size(compression_algorithm) -> Int](compression_decode_scratch_buffer_size(_:).md)
  Returns the required decompression scratch buffer size for the selected algorithm.
- [func compression_decode_buffer(UnsafeMutablePointer<UInt8>, Int, UnsafePointer<UInt8>, Int, UnsafeMutableRawPointer?, compression_algorithm) -> Int](compression_decode_buffer(_:_:_:_:_:_:).md)
  Decompresses the contents of a source buffer into a destination buffer.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_encode_scratch_buffer_size(_:))*