# MEByteSource

**Framework**: MediaExtension  
**Kind**: class

Provides read access to the data in a media asset file.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEByteSource
```

#### Overview

Media Toolbox passes an `MEByteSource` instance for the media asset’s primary file when it initializes an [`MEFormatReader`](meformatreader.md) object. The format reader may call [`byteSourceForRelatedFileName(_:)`](mebytesource/bytesourceforrelatedfilename(_:).md) to request additional byte sources for related files in the same directory as the primary file.

## Topics

### Inspecting a byte source
- [var fileName: String](mebytesource/filename.md)
  The name of the file for the byte source.
- [var fileLength: Int64](mebytesource/filelength.md)
  The length of the byte source file.
- [var contentType: UTType?](mebytesource/contenttype.md)
  The format of the byte source file.
- [var relatedFileNamesInSameDirectory: [String]](mebytesource/relatedfilenamesinsamedirectory.md)
  An array of related file names in the parent directory of the byte source file.
### Performing operations on a byte source
- [func availableLength(at: Int64) -> Int64](mebytesource/availablelength(at:).md)
  Gets the number of available bytes from the offset within the byte source.
- [func byteSourceForRelatedFileName(String) throws -> MEByteSource](mebytesource/bytesourceforrelatedfilename(_:).md)
  Creates a new byte source for a related file.
- [func read(length: Int, from: Int64, completionHandler: (Data?, (any Error)?) -> Void)](mebytesource/read(length:from:completionhandler:).md)
  Reads bytes from a byte source into a data object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource)*