# InputFilter

**Framework**: Compression  
**Kind**: class

An encoder-decoder that reads input data from a stream.

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
class InputFilter<D> where D : DataProtocol
```

## Topics

### Initializers
- [init(FilterOperation, using: Algorithm, bufferCapacity: Int, readingFrom: (Int) throws -> D?) throws](inputfilter/init(_:using:buffercapacity:readingfrom:).md)
  Creates an input filter that can be used to compress or decompress data.
### Instance Methods
- [func readData(ofLength: Int) throws -> Data?](inputfilter/readdata(oflength:).md)
  Reads processed data from the input filter.

## See Also

- [Compressing and decompressing data with input and output filters](../Accelerate/compressing-and-decompressing-data-with-input-and-output-filters.md)
  Compress and decompress streamed or from-memory data, using input and output filters.
- [Compressing and decompressing files with stream compression](../Accelerate/compressing-and-decompressing-files-with-stream-compression.md)
  Perform compression for all files and decompression for files with supported extension types.
- [class OutputFilter](outputfilter.md)
  An encoder-decoder that writes output data to a stream.
- [enum Algorithm](algorithm.md)
  Algorithms used for compression or decompression.
- [enum FilterError](filtererror.md)
  Errors that occur during compression.
- [enum FilterOperation](filteroperation.md)
  Operations that define whether input and output filters compress or decompress data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/inputfilter)*