# ArchiveByteStreamProtocol

**Framework**: Apple Archive  
**Kind**: protocol  
**Role**: Protocol

A set of methods that defines the interface for using an archive stream that reads from and writes to buffers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
protocol ArchiveByteStreamProtocol
```

## Topics

### Reading and Writing Data
- [func read(into: UnsafeMutableRawBufferPointer) throws -> Int](./archivebytestreamprotocol/read%28into%29.md)
  Reads data to the specified buffer, not exceeding the buffer’s previously allocated size.
- [func read(into: UnsafeMutableRawBufferPointer, atOffset: Int64) throws -> Int](./archivebytestreamprotocol/read%28into,atoffset%29.md)
  Reads data at the supplied offset to the specified buffer, not exceeding the buffer’s previously allocated size.
- [func write(from: UnsafeRawBufferPointer) throws -> Int](./archivebytestreamprotocol/write%28from%29.md)
  Writes data from the specified buffer, not exceeding the buffer’s allocated size.
- [func write(from: UnsafeRawBufferPointer, atOffset: Int64) throws -> Int](./archivebytestreamprotocol/write%28from,atoffset%29.md)
  Writes data at the supplied offset from the specified buffer, not exceeding the buffer’s allocated size.
### Using Archive Byte Streams
- [func seek(toOffset: Int64, relativeTo: FileDescriptor.SeekOrigin) throws -> Int64](./archivebytestreamprotocol/seek%28tooffset,relativeto%29.md)
  Updates the internal stream position to the specified offset relative to the specified origin.
- [func cancel()](./archivebytestreamprotocol/cancel%28%29.md)
  Cancels stream operations.
- [func close() throws](./archivebytestreamprotocol/close%28%29.md)
  Closes the stream and releases associated resources.

## Relationships

### Conforming Types
- [ArchiveByteStream](./archivebytestream.md)

## See Also

### Apple Archive streams
- [protocol ArchiveStreamProtocol](./archivestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to data blobs.
- [class ArchiveStream](./archivestream.md)
  An archive stream that reads from and writes to data blobs
- [class ArchiveByteStream](./archivebytestream.md)
  An archive stream that reads from and writes to buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol)*