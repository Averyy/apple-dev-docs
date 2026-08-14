# compression_algorithm

**Framework**: Compression  
**Kind**: struct

A structure for values that represent compression algorithms.

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
struct compression_algorithm
```

#### Overview

Choose an algorithm according to the following guidelines:

- If speed and compression ratio are important, use [`COMPRESSION_LZMESH`](compression_lzmesh.md).
- If you require interoperability with non-Apple devices, use [`COMPRESSION_ZLIB`](compression_zlib.md).
- If speed is critical, and you’re willing to sacrifice compression ratio to achieve it, use [`COMPRESSION_LZ4`](compression_lz4.md).
- If compression ratio is critical, and you can sacrifice speed to achieve it, use [`COMPRESSION_LZRAVEN`](compression_lzraven.md). Note that [`COMPRESSION_LZRAVEN`](compression_lzraven.md) is an order of magnitude slower for both compression and decompression than other choices.

[`COMPRESSION_LZMESH`](compression_lzmesh.md) is faster than [`COMPRESSION_ZLIB`](compression_zlib.md) and generally achieves a better compression ratio. However, it’s slower than [`COMPRESSION_LZ4`](compression_lz4.md) and doesn’t compress as well as [`COMPRESSION_LZRAVEN`](compression_lzraven.md).

[`COMPRESSION_LZBITMAP`](compression_lzbitmap.md) provides a compression-ratio that’s between [`COMPRESSION_LZ4`](compression_lz4.md) and [`COMPRESSION_LZMESH`](compression_lzmesh.md). When compression ratio and performance are equally important, use [`COMPRESSION_LZMESH`](compression_lzmesh.md) to favor compression ratio and [`COMPRESSION_LZBITMAP`](compression_lzbitmap.md) to favor performance.

## Topics

### Algorithm Constants
- [var COMPRESSION_LZFSE: compression_algorithm](compression_lzfse.md)
  The LZFSE compression algorithm, which is recommended for use on Apple platforms.
- [var COMPRESSION_LZ4: compression_algorithm](compression_lz4.md)
  The LZ4 compression algorithm for fast compression.
- [var COMPRESSION_LZ4_RAW: compression_algorithm](compression_lz4_raw.md)
  The LZ4 compression algorithm, without frame headers.
- [var COMPRESSION_LZMA: compression_algorithm](compression_lzma.md)
  The LZMA compression algorithm, which is recommended for high-compression ratio.
- [var COMPRESSION_ZLIB: compression_algorithm](compression_zlib.md)
  The zlib compression algorithm, which is recommended for cross-platform compression.
- [var COMPRESSION_BROTLI: compression_algorithm](compression_brotli.md)
  The Brotli compression algorithm, which is recommended for text compression.
- [var COMPRESSION_LZBITMAP: compression_algorithm](compression_lzbitmap.md)
  The LZBITMAP compression algorithm, which is designed to exploit the vector instruction set of current CPUs.
- [var COMPRESSION_LZMESH: compression_algorithm](compression_lzmesh.md)
  The LZMESH compression algorithm, which is recommended for fast, general-purpose compression on Apple platforms.
- [var COMPRESSION_LZRAVEN: compression_algorithm](compression_lzraven.md)
  The LZRAVEN compression algorithm, which is recommended for high-compression ratio with fast decoding on Apple platforms.
### Initializers
- [init(UInt32)](compression_algorithm/init(_:).md)
  Creates a new constant from the given raw value.
- [init(rawValue: UInt32)](compression_algorithm/init(rawvalue:).md)
  Creates a new constant from the given raw value.
### Instance Properties
- [var rawValue: UInt32](compression_algorithm/rawvalue.md)
  The raw value of the constant.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)

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
- [struct compression_stream_flags](compression_stream_flags.md)
  A set of values used to represent stream compression flags.
- [struct compression_stream_operation](compression_stream_operation.md)
  A set of values used to represent a stream compression operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_algorithm)*