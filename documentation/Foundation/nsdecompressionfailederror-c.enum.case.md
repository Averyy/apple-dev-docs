# NSDecompressionFailedError

**Framework**: Foundation  
**Kind**: case  
**Role**: Enumeration Case

An error code value that indicates a failure to decompress data using the provided algorithm.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```c
NSDecompressionFailedError
```

## See Also

### Compressing and Decompressing Data
- [func compress(using: NSData.CompressionAlgorithm) throws](./nsmutabledata/compress%28using%29.md)
  Compresses the data object’s bytes using an algorithm that you specify.
- [func decompress(using: NSData.CompressionAlgorithm) throws](./nsmutabledata/decompress%28using%29.md)
  Decompresses the data object’s bytes.
- [NSData.CompressionAlgorithm](./nsdata/compressionalgorithm.md)
  An algorithm that indicates how to compress or decompress data.
- [NSCompressionErrorMaximum](./nscompressionerrormaximum-c.enum.case.md)
  The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](./nscompressionerrorminimum-c.enum.case.md)
  The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](./nscompressionfailederror-c.enum.case.md)
  An error code value that indicates a failure to compress data using the provided algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecompressionfailederror-c.enum.case)*