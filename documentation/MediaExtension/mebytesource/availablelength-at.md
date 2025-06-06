# availableLength(at:)

**Framework**: MediaExtension  
**Kind**: method

Gets the number of available bytes from the offset within the byte source.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func availableLength(at offset: Int64) -> Int64
```

#### Return Value

An integer that specifies the number of available bytes.

## Parameters

- `offset`: The offset in bytes from the beginning of the byte source.

## See Also

- [func byteSourceForRelatedFileName(String) throws -> MEByteSource](mebytesource/bytesourceforrelatedfilename(_:).md)
  Creates a new byte source for a related file.
- [func read(length: Int, from: Int64, completionHandler: (Data?, (any Error)?) -> Void)](mebytesource/read(length:from:completionhandler:).md)
  Reads bytes from a byte source into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/availablelength(at:))*