# decompressed(using:)

**Framework**: Foundation  
**Kind**: method

Returns a new data object by decompressing data object’s bytes.

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
func decompressed(using algorithm: NSData.CompressionAlgorithm) throws -> Self
```

#### Return Value

An [`NSData`](nsdata.md) instance that contains the decompressed buffer data.

#### Discussion

Use this method to inflate in-memory data when you need uncompressed bytes. Specify the same algorithm used to compress the data to successfully decompress it.

The following example shows how to create a new [`NSData`](nsdata.md) instance from data compressed with the [`NSData.CompressionAlgorithm.zlib`](nsdata/compressionalgorithm/zlib.md) algorithm:

```swift
do {
    let uncompressedData = try compressedData.decompressed(using: .zlib)
} catch {
    print ("Decompression error: \(error)")
}
```

## Parameters

- `algorithm`: An algorithm used to decompress the data. For a list of available algorithms, see  .

## See Also

- [func compressed(using: NSData.CompressionAlgorithm) throws -> Self](nsdata/compressed(using:).md)
  Returns a new data object by compressing the data object’s bytes.
- [NSData.CompressionAlgorithm](nsdata/compressionalgorithm.md)
  An algorithm that indicates how to compress or decompress data.
- [var NSCompressionErrorMaximum: Int](nscompressionerrormaximum-swift.var.md)
  The end of the range of error codes reserved for compression errors.
- [var NSCompressionErrorMinimum: Int](nscompressionerrorminimum-swift.var.md)
  The start of the range of error codes reserved for compression errors.
- [var NSCompressionFailedError: Int](nscompressionfailederror-swift.var.md)
  An error code value that indicates a failure to compress data using the provided algorithm.
- [var NSDecompressionFailedError: Int](nsdecompressionfailederror-swift.var.md)
  An error code value that indicates a failure to decompress data using the provided algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/decompressed(using:))*