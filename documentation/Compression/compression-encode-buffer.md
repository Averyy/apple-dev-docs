# compression_encode_buffer(_:_:_:_:_:_:)

**Framework**: Compression  
**Kind**: func

Compresses the contents of a source buffer into a destination buffer.

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
func compression_encode_buffer(_ dst_buffer: UnsafeMutablePointer<UInt8>, _ dst_size: Int, _ src_buffer: UnsafePointer<UInt8>, _ src_size: Int, _ scratch_buffer: UnsafeMutableRawPointer?, _ algorithm: compression_algorithm) -> Int
```

#### Return Value

The number of bytes written to the destination buffer after compressing the input. If the funtion can’t compress the entire input to fit into the provided destination buffer, or an error occurs, 0 is returned.

#### Discussion

If the input is successfully compressed, the function writes the compressed data to dst_buffer.

## Parameters

- `dst_buffer`: Pointer to the buffer that receives the compressed data.
- `dst_size`: Size of the destination buffer in bytes.
- `src_buffer`: Pointer to a buffer containing all of the source data.
- `src_size`: Size of the data in the source buffer in bytes.
- `scratch_buffer`: If   is nil, the function creates and manages its own scratch space, but with a possible performance hit.
- `algorithm`: Set to the desired algorithm:  ,  ,  , or  .

## See Also

- [Compressing and decompressing data with buffer compression](../Accelerate/compressing-and-decompressing-data-with-buffer-compression.md)
  Compress a string, write it to the file system, and decompress the same file using buffer compression.
- [func compression_encode_scratch_buffer_size(compression_algorithm) -> Int](compression_encode_scratch_buffer_size(_:).md)
  Returns the required compression scratch buffer size for the selected algorithm.
- [func compression_decode_scratch_buffer_size(compression_algorithm) -> Int](compression_decode_scratch_buffer_size(_:).md)
  Returns the required decompression scratch buffer size for the selected algorithm.
- [func compression_decode_buffer(UnsafeMutablePointer<UInt8>, Int, UnsafePointer<UInt8>, Int, UnsafeMutableRawPointer?, compression_algorithm) -> Int](compression_decode_buffer(_:_:_:_:_:_:).md)
  Decompresses the contents of a source buffer into a destination buffer.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_encode_buffer(_:_:_:_:_:_:))*