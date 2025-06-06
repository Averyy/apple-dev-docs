# compression_status

**Framework**: Compression  
**Kind**: struct

A set of values used to represent the status of stream compression.

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
struct compression_status
```

## Topics

### Status Constants
- [var COMPRESSION_STATUS_OK: compression_status](compression_status_ok.md)
  Indicates the stream has consumed all data in the source buffer, or used all space in the destination buffer.
- [var COMPRESSION_STATUS_END: compression_status](compression_status_end.md)
  Indicates the stream has read all input from the source, and written all output to the destination.
- [var COMPRESSION_STATUS_ERROR: compression_status](compression_status_error.md)
  Indicates an error with stream compression.
### Initializers
- [init(Int32)](compression_status/init(_:).md)
  Creates a new constant from the given raw value.
- [init(rawValue: Int32)](compression_status/init(rawvalue:).md)
  Creates a new constant from the given raw value.
### Instance Properties
- [var rawValue: Int32](compression_status/rawvalue.md)
  The raw value of the constant.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct compression_stream](compression_stream.md)
  A structure representing a compression stream.
- [func compression_stream_init(UnsafeMutablePointer<compression_stream>, compression_stream_operation, compression_algorithm) -> compression_status](compression_stream_init(_:_:_:).md)
  Initializes a compression stream for either compression or decompression.
- [func compression_stream_process(UnsafeMutablePointer<compression_stream>, Int32) -> compression_status](compression_stream_process(_:_:).md)
  Performs compression or decompression using an initialized compression stream structure.
- [func compression_stream_destroy(UnsafeMutablePointer<compression_stream>) -> compression_status](compression_stream_destroy(_:).md)
  Frees any memory allocated by stream initialization function.
- [struct compression_stream_flags](compression_stream_flags.md)
  A set of values used to represent stream compression flags.
- [struct compression_stream_operation](compression_stream_operation.md)
  A set of values used to represent a stream compression operation.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_status)*