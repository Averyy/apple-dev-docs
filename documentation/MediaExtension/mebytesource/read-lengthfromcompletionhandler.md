# read(length:from:completionHandler:)

**Framework**: MediaExtension  
**Kind**: method

Reads bytes from a byte source into a data object.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func read(length: Int, from offset: Int64) async throws -> Data
```

## Parameters

- `length`: The number of bytes to read.
- `offset`: The relative offset in bytes from the beginning of the file from which to start reading.
- `completionHandler`: The completion block to execute when the read operation finishes.

## See Also

- [func availableLength(at: Int64) -> Int64](mebytesource/availablelength(at:).md)
  Gets the number of available bytes from the offset within the byte source.
- [func byteSourceForRelatedFileName(String) throws -> MEByteSource](mebytesource/bytesourceforrelatedfilename(_:).md)
  Creates a new byte source for a related file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/read(length:from:completionhandler:))*