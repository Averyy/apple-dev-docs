# compression_stream_process(_:_:)

**Framework**: Compression  
**Kind**: func

Performs compression or decompression using an initialized compression stream structure.

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
func compression_stream_process(_ stream: UnsafeMutablePointer<compression_stream>, _ flags: Int32) -> compression_status
```

##### Return Value

A value of type [`compression_status`](compression_status.md), which you interpret as follows:

- [`COMPRESSION_STATUS_OK`](compression_status_ok.md) indicates success, but the stream might produce more output. Call the function again with updated parameters.
- [`COMPRESSION_STATUS_END`](compression_status_end.md) indicates success, and the stream produces no more output. When encoding, the function returns this status only after it reads all input from the source, writes all output (including an end-of-stream marker) to the destination, and you set `flags` to [`COMPRESSION_STREAM_FINALIZE`](compression_stream_finalize.md). When decoding, the function returns this status as soon as it reads the end-of-stream marker from the source and writes all output to the destination; the source buffer can still contain additional data.
- [`COMPRESSION_STATUS_ERROR`](compression_status_error.md) indicates an error.

#### Discussion

Each time you call [`compression_stream_process(_:_:)`](compression_stream_process(_:_:).md) successfully, the function consumes data from the source buffer and writes data into the destination buffer, until it reaches the end of one of the buffers and returns either [`COMPRESSION_STATUS_OK`](compression_status_ok.md) or [`COMPRESSION_STATUS_END`](compression_status_end.md).

After a successful call, the function updates the buffer parameters in the stream object; it increments `src_ptr` (and decrements `src_size`) by the number of input bytes it consumes. Likewise, it increments `dst_ptr` (and decrements `dst_size`) by the number of output bytes it produces. The sum (`src_ptr + src_size`) remains unchanged, and so does (`dst_ptr + dst_size`). At this point, either `src_size` or `dst_size` is 0, indicating that the source buffer is empty or the destination buffer is full.

If the source buffer is empty, you can refill it with more data and adjust the parameters, or point to a different buffer for the next call. If you don’t provide any more input data, set `flags` to [`COMPRESSION_STREAM_FINALIZE`](compression_stream_finalize.md) and call again.

If the destination buffer is full and the return value isn’t [`COMPRESSION_STATUS_END`](compression_status_end.md), input might still remain for processing. To continue, grow the buffer, move the pointer back to reuse the buffer, or point to a new destination buffer, and then call the function again.

When you decode a valid stream, the decoder detects the end of the stream from the contents of the input and returns [`COMPRESSION_STATUS_END`](compression_status_end.md), even when you don’t set `COMPRESSION_STREAM_FINALIZE` or you provide more input.

When the decoder detects corruption in the input, it returns `COMPRESSION_STATUS_ERROR`. The decoder can’t always detect corruption or truncation, though; without an end-of-stream marker, it consumes the available input and returns `COMPRESSION_STATUS_OK` to request more because it hasn’t reached the end of the stream. Setting `COMPRESSION_STREAM_FINALIZE` tells the decoder that no more input is coming, so it finishes the stream instead of requesting more data — which keeps your client code from calling `compression_stream_process` repeatedly with the same state in an infinite loop. Set `COMPRESSION_STREAM_FINALIZE` whenever you expect no more input, for both encoding and decoding.

## Parameters

- `stream`: A pointer to an allocated and fully initialized [`compression_stream`](compression_stream.md) structure.
- `flags`: A constant of type [`compression_stream_flags`](compression_stream_flags.md). Pass [`COMPRESSION_STREAM_FINALIZE`](compression_stream_finalize.md) when no further input data remains, or `0` otherwise.

## See Also

- [struct compression_stream](compression_stream.md)
  A structure representing a compression stream.
- [func compression_stream_init(UnsafeMutablePointer<compression_stream>, compression_stream_operation, compression_algorithm) -> compression_status](compression_stream_init(_:_:_:).md)
  Initializes a compression stream for either compression or decompression.
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

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_stream_process(_:_:))*