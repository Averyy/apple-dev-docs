# NSData.CompressionAlgorithm

**Framework**: Foundation  
**Kind**: enum

An algorithm that indicates how to compress or decompress data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum CompressionAlgorithm
```

#### Overview

Choose an algorithm that best suits the needs of your app:

- [`NSData.CompressionAlgorithm.lzfse`](nsdata/compressionalgorithm/lzfse.md) — The algorithm offers faster speed and generally achieves better compression than   [`NSData.CompressionAlgorithm.zlib`](nsdata/compressionalgorithm/zlib.md). However, it is slower than [`NSData.CompressionAlgorithm.lz4`](nsdata/compressionalgorithm/lz4.md) and doesn’t compress as well as [`NSData.CompressionAlgorithm.lzma`](nsdata/compressionalgorithm/lzma.md).
- [`NSData.CompressionAlgorithm.zlib`](nsdata/compressionalgorithm/zlib.md) — Use this algorithm if your app requires interoperability with non-Apple devices. For example, if you are transferering data to another device where it needs to be compressed or decompressed.
- [`NSData.CompressionAlgorithm.lz4`](nsdata/compressionalgorithm/lz4.md) — Use this algorithm if speed is critical, and you’re willing to sacrifice compression ratio to achieve it.
- [`NSData.CompressionAlgorithm.lzma`](nsdata/compressionalgorithm/lzma.md) — Use this algorithm if compression ratio is critical, and you’re willing to sacrifice speed to achieve it. It is an order of magnitude slower for both compression and decompression than other choices.

## Topics

### Algorithms
- [NSData.CompressionAlgorithm.lz4](nsdata/compressionalgorithm/lz4.md)
  The LZ4 compression algorithm, recommended for fast compression.
- [NSData.CompressionAlgorithm.lzfse](nsdata/compressionalgorithm/lzfse.md)
  The LZFSE compression algorithm, recommended for use on Apple platforms.
- [NSData.CompressionAlgorithm.lzma](nsdata/compressionalgorithm/lzma.md)
  The LZMA compression algorithm, recommended for high-compression ratio.
- [NSData.CompressionAlgorithm.zlib](nsdata/compressionalgorithm/zlib.md)
  The zlib compression algorithm, recommended for cross-platform compression.
### Initializers
- [init?(rawValue: Int)](nsdata/compressionalgorithm/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func compressed(using: NSData.CompressionAlgorithm) throws -> Self](nsdata/compressed(using:).md)
  Returns a new data object by compressing the data object’s bytes.
- [func decompressed(using: NSData.CompressionAlgorithm) throws -> Self](nsdata/decompressed(using:).md)
  Returns a new data object by decompressing data object’s bytes.
- [var NSCompressionErrorMaximum: Int](nscompressionerrormaximum-swift.var.md)
  The end of the range of error codes reserved for compression errors.
- [var NSCompressionErrorMinimum: Int](nscompressionerrorminimum-swift.var.md)
  The start of the range of error codes reserved for compression errors.
- [var NSCompressionFailedError: Int](nscompressionfailederror-swift.var.md)
  An error code value that indicates a failure to compress data using the provided algorithm.
- [var NSDecompressionFailedError: Int](nsdecompressionfailederror-swift.var.md)
  An error code value that indicates a failure to decompress data using the provided algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/compressionalgorithm)*