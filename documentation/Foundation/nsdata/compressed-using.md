# compressed(using:)

**Framework**: Foundation  
**Kind**: method

Returns a new data object by compressing the data object’s bytes.

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
func compressed(using algorithm: NSData.CompressionAlgorithm) throws -> Self
```

#### Return Value

An [`NSData`](nsdata.md) instance that contains the compressed buffer data.

#### Discussion

Use this method to compress in-memory data when you want to reduce memory usage and can afford the time to compress and decompress it. If your data object is already in a compressed format, such as media formats like JPEG images or AAC audio, additional compression may provide minimal or no reduction in memory usage.

To restore this data, use [`decompressed(using:)`](nsdata/decompressed(using:).md), and specify the algorithm originally used to compress the data.

The following example shows how to compress the data from a string and prints the sizes of the data instances to illustrate the amount of compression:

```swift
var string = "NSData and its mutable subclass NSMutableData provide data objects, or object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Foundation objects."
let data = Data(string.utf8) as NSData
print ("original data size: \(data.count) bytes")
do {
    let compressedData = try data.compressed(using: .zlib)
    print("zlib compressed size: \(compressedData.count) bytes")
} catch {
    print ("Compression error: \(error)")
}
// Prints:
//  original data size: 241 bytes
//  zlib compressed size: 158 bytes
```

## Parameters

- `algorithm`: An algorithm used to compress the data. For a list of available algorithms, see  .

## See Also

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
- [var NSDecompressionFailedError: Int](nsdecompressionfailederror-swift.var.md)
  An error code value that indicates a failure to decompress data using the provided algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/compressed(using:))*