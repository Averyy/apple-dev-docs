# Algorithm

**Framework**: Compression  
**Kind**: enum

Algorithms used for compression or decompression.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
enum Algorithm
```

## Topics

### Enumeration Cases
- [Algorithm.brotli](algorithm/brotli.md)
  The Brotli compression algorithm, which is recommended for text compression.
- [Algorithm.lz4](algorithm/lz4.md)
  The LZ4 compression algorithm, which is recommended for fast compression.
- [Algorithm.lzbitmap](algorithm/lzbitmap.md)
  The LZBITMAP compression algorithm, which is designed to exploit the vector instruction set of current CPUs.
- [Algorithm.lzfse](algorithm/lzfse.md)
  The LZFSE compression algorithm, which is recommended for use on Apple platforms.
- [Algorithm.lzma](algorithm/lzma.md)
  The LZMA compression algorithm, which is recommended for high-compression ratio.
- [Algorithm.zlib](algorithm/zlib.md)
  The zlib compression algorithm, which is recommended for cross-platform compression.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [Compressing and decompressing data with input and output filters](../Accelerate/compressing-and-decompressing-data-with-input-and-output-filters.md)
  Compress and decompress streamed or from-memory data, using input and output filters.
- [Compressing and decompressing files with stream compression](../Accelerate/compressing-and-decompressing-files-with-stream-compression.md)
  Perform compression for all files and decompression for files with supported extension types.
- [class InputFilter](inputfilter.md)
  An encoder-decoder that reads input data from a stream.
- [class OutputFilter](outputfilter.md)
  An encoder-decoder that writes output data to a stream.
- [enum FilterError](filtererror.md)
  Errors that occur during compression.
- [enum FilterOperation](filteroperation.md)
  Operations that define whether input and output filters compress or decompress data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/algorithm)*