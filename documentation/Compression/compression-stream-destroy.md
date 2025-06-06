# compression_stream_destroy(_:)

**Framework**: Compression  
**Kind**: func

Frees any memory allocated by stream initialization function.

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
func compression_stream_destroy(_ stream: UnsafeMutablePointer<compression_stream>) -> compression_status
```

##### Return Value

A value of type [`compression_status`](compression_status.md), interpreted as follows:

- [`COMPRESSION_STATUS_OK`](compression_status_ok.md) means that the function successfully destroyed the stream.
- [`COMPRESSION_STATUS_ERROR`](compression_status_error.md) means an error occurred.

#### Discussion

Note that [`compression_stream_destroy(_:)`](compression_stream_destroy(_:).md) doesn’t free the stream object or the buffers allocated by the caller.

## Parameters

- `stream`: A pointer to an allocated and initialized   structure.

## See Also

- [struct compression_stream](compression_stream.md)
  A structure representing a compression stream.
- [func compression_stream_init(UnsafeMutablePointer<compression_stream>, compression_stream_operation, compression_algorithm) -> compression_status](compression_stream_init(_:_:_:).md)
  Initializes a compression stream for either compression or decompression.
- [func compression_stream_process(UnsafeMutablePointer<compression_stream>, Int32) -> compression_status](compression_stream_process(_:_:).md)
  Performs compression or decompression using an initialized compression stream structure.
- [struct compression_status](compression_status.md)
  A set of values used to represent the status of stream compression.
- [struct compression_stream_flags](compression_stream_flags.md)
  A set of values used to represent stream compression flags.
- [struct compression_stream_operation](compression_stream_operation.md)
  A set of values used to represent a stream compression operation.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_stream_destroy(_:))*