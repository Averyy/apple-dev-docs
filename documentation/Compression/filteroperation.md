# FilterOperation

**Framework**: Compression  
**Kind**: enum

Operations that define whether input and output filters compress or decompress data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
enum FilterOperation
```

## Topics

### Enumeration Cases
- [FilterOperation.compress](filteroperation/compress.md)
  An operation that compresses data.
- [FilterOperation.decompress](filteroperation/decompress.md)
  An operation that decompresses data.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)

## See Also

- [Compressing and decompressing data with input and output filters](../accelerate/compressing-and-decompressing-data-with-input-and-output-filters.md)
  Compress and decompress streamed or from-memory data, using input and output filters.
- [Compressing and decompressing files with stream compression](../accelerate/compressing-and-decompressing-files-with-stream-compression.md)
  Perform compression for all files and decompression for files with supported extension types.
- [class InputFilter](inputfilter.md)
  An encoder-decoder that reads input data from a stream.
- [class OutputFilter](outputfilter.md)
  An encoder-decoder that writes output data to a stream.
- [enum Algorithm](algorithm.md)
  Algorithms used for compression or decompression.
- [enum FilterError](filtererror.md)
  Errors that occur during compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/filteroperation)*