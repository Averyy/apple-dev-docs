# ArchiveStreamProtocol

**Framework**: Apple Archive  
**Kind**: protocol

A set of methods that defines the interface for using an archive stream that reads from and writes to data blobs.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
protocol ArchiveStreamProtocol
```

## Topics

### Reading and Writing Blobs
- [func readBlob(key: ArchiveHeader.FieldKey, into: UnsafeMutableRawBufferPointer) throws](archivestreamprotocol/readblob(key:into:).md)
  Reads the current entry blob data.
- [func writeBlob(key: ArchiveHeader.FieldKey, from: UnsafeRawBufferPointer) throws](archivestreamprotocol/writeblob(key:from:).md)
  Writes an entry blob data.
### Reading and Writing Headers
- [func readHeader() throws -> ArchiveHeader?](archivestreamprotocol/readheader.md)
  Reads the next entry header.
- [func writeHeader(ArchiveHeader) throws](archivestreamprotocol/writeheader(_:).md)
  Writes an entry header.
### Using Archive Streams
- [func cancel()](archivestreamprotocol/cancel.md)
  Cancels stream operations.
- [func close() throws](archivestreamprotocol/close.md)
  Closes the stream and releases associated resources.

## Relationships

### Conforming Types
- [ArchiveStream](archivestream.md)

## See Also

- [class ArchiveStream](archivestream.md)
  An archive stream that reads from and writes to data blobs
- [protocol ArchiveByteStreamProtocol](archivebytestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to buffers.
- [class ArchiveByteStream](archivebytestream.md)
  An archive stream that reads from and writes to buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestreamprotocol)*