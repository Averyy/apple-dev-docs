# compression_decode_buffer(_:_:_:_:_:_:)

**Framework**: Compression  
**Kind**: func

Decompresses the contents of a source buffer into a destination buffer.

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
func compression_decode_buffer(_ dst_buffer: UnsafeMutablePointer<UInt8>, _ dst_size: Int, _ src_buffer: UnsafePointer<UInt8>, _ src_size: Int, _ scratch_buffer: UnsafeMutableRawPointer?, _ algorithm: compression_algorithm) -> Int
```

#### Return Value

The number of bytes written to the destination buffer after decompressing the input.  If there is not enough space in the destination buffer to hold the entire decompressed output, the function writes the first `dst_size` bytes to the buffer and returns `dst_size`. Note that this behavior differs from that of [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md).

#### Discussion

The function writes the decompressed data to `dst_buffer`.

## Parameters

- `dst_buffer`: Pointer to the buffer that receives the decompressed data.
- `dst_size`: Size of the destination buffer in bytes.
- `src_buffer`: Pointer to a buffer containing all of the compressed source data.
- `src_size`: Size of the data in the source buffer in bytes.
- `scratch_buffer`: If   is  , the function creates and manages its own scratch space, but with a possible performance hit.
- `algorithm`: Set to the desired algorithm:  ,  ,  , or  .

## See Also

- [Compressing and decompressing data with buffer compression](../Accelerate/compressing-and-decompressing-data-with-buffer-compression.md)
  Compress a string, write it to the file system, and decompress the same file using buffer compression.
- [func compression_encode_scratch_buffer_size(compression_algorithm) -> Int](compression_encode_scratch_buffer_size(_:).md)
  Returns the required compression scratch buffer size for the selected algorithm.
- [func compression_encode_buffer(UnsafeMutablePointer<UInt8>, Int, UnsafePointer<UInt8>, Int, UnsafeMutableRawPointer?, compression_algorithm) -> Int](compression_encode_buffer(_:_:_:_:_:_:).md)
  Compresses the contents of a source buffer into a destination buffer.
- [func compression_decode_scratch_buffer_size(compression_algorithm) -> Int](compression_decode_scratch_buffer_size(_:).md)
  Returns the required decompression scratch buffer size for the selected algorithm.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_decode_buffer(_:_:_:_:_:_:))*