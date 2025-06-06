# NSDecompressionFailedError

**Framework**: Foundation  
**Kind**: var

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

```swift
var NSDecompressionFailedError: Int { get }
```

## See Also

- [func compressed(using: NSData.CompressionAlgorithm) throws -> Self](nsdata/compressed(using:).md)
  Returns a new data object by compressing the data object’s bytes.
- [func decompressed(using: NSData.CompressionAlgorithm) throws -> Self](nsdata/decompressed(using:).md)
  Returns a new data object by decompressing data object’s bytes.
- [NSData.CompressionAlgorithm](nsdata/compressionalgorithm.md)
  An algorithm that indicates how to compress or decompress data.
- [var NSCompressionErrorMaximum: Int](nscompressionerrormaximum-swift.var.md)
  The end of the range of error codes reserved for compression errors.
- [var NSCompressionErrorMinimum: Int](nscompressionerrorminimum-swift.var.md)
  The start of the range of error codes reserved for compression errors.
- [var NSCompressionFailedError: Int](nscompressionfailederror-swift.var.md)
  An error code value that indicates a failure to compress data using the provided algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecompressionfailederror-swift.var)*