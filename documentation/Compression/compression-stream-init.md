# compression_stream_init(_:_:_:)

**Framework**: Compression  
**Kind**: func

Initializes a compression stream for either compression or decompression.

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
func compression_stream_init(_ stream: UnsafeMutablePointer<compression_stream>, _ operation: compression_stream_operation, _ algorithm: compression_algorithm) -> compression_status
```

##### Return Value

A value of type [`compression_status`](compression_status.md), interpreted as follows:

- [`COMPRESSION_STATUS_OK`](compression_status_ok.md) means the stream object was successfully initialized.
- [`COMPRESSION_STATUS_ERROR`](compression_status_error.md) means an error occurred.

#### Discussion

After success of this function, set the `dst_ptr`, `dst_size`, `src_ptr`, and `src_size` fields of the stream structure to their respective values. You can then pass stream structure to the [`compression_stream_process(_:_:)`](compression_stream_process(_:_:).md) function.

## Parameters

- `stream`: Pointer to an allocated   structure.
- `operation`: A constant of type   used to indicate the stream operation.
- `algorithm`: A constant of type   to select the algorithm:  ,  ,  , or  .

## See Also

- [struct compression_stream](compression_stream.md)
  A structure representing a compression stream.
- [func compression_stream_process(UnsafeMutablePointer<compression_stream>, Int32) -> compression_status](compression_stream_process(_:_:).md)
  Performs compression or decompression using an initialized compression stream structure.
- [func compression_stream_destroy(UnsafeMutablePointer<compression_stream>) -> compression_status](compression_stream_destroy(_:).md)
  Frees any memory allocated by stream initialization function.
- [struct compression_status](compression_status.md)
  A set of values used to represent the status of stream compression.
- [struct compression_stream_flags](compression_stream_flags.md)
  A set of values used to represent stream compression flags.
- [struct compression_stream_operation](compression_stream_operation.md)
  A set of values used to represent a stream compression operation.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_stream_init(_:_:_:))*