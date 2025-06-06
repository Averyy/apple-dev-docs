# compression_stream_flags

**Framework**: Compression  
**Kind**: struct

A set of values used to represent stream compression flags.

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
struct compression_stream_flags
```

## Topics

### Flag Constants
- [var COMPRESSION_STREAM_FINALIZE: compression_stream_flags](compression_stream_finalize.md)
  Indicates that the operation will add no further input blocks to the stream.
### Initializers
- [init(UInt32)](compression_stream_flags/init(_:).md)
  Creates a new constant from the given raw value.
- [init(rawValue: UInt32)](compression_stream_flags/init(rawvalue:).md)
  Creates a new constant from the given raw value.
### Instance Properties
- [var rawValue: UInt32](compression_stream_flags/rawvalue.md)
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
- [struct compression_status](compression_status.md)
  A set of values used to represent the status of stream compression.
- [struct compression_stream_operation](compression_stream_operation.md)
  A set of values used to represent a stream compression operation.
- [struct compression_algorithm](compression_algorithm.md)
  A structure for values that represent compression algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_stream_flags)*