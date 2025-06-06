# decompress(using:)

**Framework**: Foundation  
**Kind**: method

Decompresses the data object’s bytes.

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
func decompress(using algorithm: NSData.CompressionAlgorithm) throws
```

#### Discussion

Use this method to inflate in-memory data when you need uncompressed bytes. Specify the same algorithm used to compress the data to successfully decompress it.

The following example shows how to inflate an instance of [`NSMutableData`](nsmutabledata.md) compressed with the [`NSData.CompressionAlgorithm.zlib`](nsdata/compressionalgorithm/zlib.md) algorithm:

```swift
do {
    data.decompress(using: .zlib)
} catch {
    print ("Decompression error: \(error)")
}
```

## Parameters

- `algorithm`: The algorithm to use for decompressing the data. For a list of available algorithms, see  .

## See Also

- [func compress(using: NSData.CompressionAlgorithm) throws](nsmutabledata/compress(using:).md)
  Compresses the data object’s bytes using an algorithm that you specify.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledata/decompress(using:))*