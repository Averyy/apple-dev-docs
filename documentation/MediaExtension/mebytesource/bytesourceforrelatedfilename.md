# byteSourceForRelatedFileName(_:)

**Framework**: MediaExtension  
**Kind**: method

Creates a new byte source for a related file.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func byteSourceForRelatedFileName(_ fileName: String) throws -> MEByteSource
```

#### Return Value

A byte source.

#### Discussion

Requests creation of a new [`MEByteSource`](mebytesource.md) for a file related to the receiving [`MEByteSource`](mebytesource.md). Only file names returned by the [`relatedFileNamesInSameDirectory`](mebytesource/relatedfilenamesinsamedirectory.md) method may be accessed.

## Parameters

- `fileName`: The related file name that exists in the byte source’s parent directory.

## See Also

- [func availableLength(at: Int64) -> Int64](mebytesource/availablelength(at:).md)
  Gets the number of available bytes from the offset within the byte source.
- [func read(length: Int, from: Int64, completionHandler: (Data?, (any Error)?) -> Void)](mebytesource/read(length:from:completionhandler:).md)
  Reads bytes from a byte source into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/bytesourceforrelatedfilename(_:))*