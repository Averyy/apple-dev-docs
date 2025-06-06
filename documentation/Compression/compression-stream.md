# compression_stream

**Framework**: Compression  
**Kind**: struct

A structure representing a compression stream.

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
struct compression_stream
```

#### Overview

The basic workflow for using the stream interface is as follows:

1. Initialize the state of your [`compression_stream`](compression_stream.md) structure by calling [`compression_stream_init(_:_:_:)`](compression_stream_init(_:_:_:).md) with the `operation` parameter set to specify whether you are encoding or decoding, and the chosen algorithm specified by the `algorithm` parameter.  This allocates storage for the state that allows you to resume encoding or decoding across calls.
2. Set the `dst_buffer`, `dst_size`, `src_buffer`, and `src_size` fields of the [`compression_stream`](compression_stream.md) object to point to the next blocks that your code processes.
3. Call [`compression_stream_process(_:_:)`](compression_stream_process(_:_:).md).  If no further input will be added to the stream via subsequent calls, `flags` should be [`COMPRESSION_STREAM_FINALIZE`](compression_stream_finalize.md) (otherwise 0). If [`compression_stream_process(_:_:)`](compression_stream_process(_:_:).md) returns [`COMPRESSION_STATUS_END`](compression_status_end.md), there is no further output from the stream.
4. Repeat steps 2 and 3 as necessary to process the entire stream.
5. Call [`compression_stream_destroy(_:)`](compression_stream_destroy(_:).md) to free the state object in the stream structure.

## Topics

### Initializers
- [init(dst_ptr: UnsafeMutablePointer<UInt8>, dst_size: Int, src_ptr: UnsafePointer<UInt8>, src_size: Int, state: UnsafeMutableRawPointer?)](compression_stream/init(dst_ptr:dst_size:src_ptr:src_size:state:).md)
  Returns a new compression stream structure.
### Compression Stream Properties
- [var dst_ptr: UnsafeMutablePointer<UInt8>](compression_stream/dst_ptr.md)
  A pointer to the first byte of the destination buffer.
- [var dst_size: Int](compression_stream/dst_size.md)
  The size, in bytes, of the destination buffer.
- [var src_ptr: UnsafePointer<UInt8>](compression_stream/src_ptr.md)
  A pointer to the first byte of the source buffer.
- [var src_size: Int](compression_stream/src_size.md)
  The size, in bytes, of the source buffer.
- [var state: UnsafeMutableRawPointer?](compression_stream/state.md)
  The stream state object of the compression stream.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func compression_stream_init(UnsafeMutablePointer<compression_stream>, compression_stream_operation, compression_algorithm) -> compression_status](compression_stream_init(_:_:_:).md)
  Initializes a compression stream for either compression or decompression.
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

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_stream)*