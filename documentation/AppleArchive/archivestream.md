# ArchiveStream

**Framework**: Apple Archive  
**Kind**: class

An archive stream that reads from and writes to data blobs

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
class ArchiveStream
```

## Topics

### Creating an Archive Stream
- [init(object: _AAOptionalObjectWrapperWithFilter<_AAArchiveStreamTraits>.AAType?, owned: Bool, messageProc: ArchiveHeader._EntryFilterWrapper?)](archivestream/init(object:owned:messageproc:).md)
  Returns a new archive stream from the specified traits and entry message processing callback.
### Writing Directory Contents
- [func writeDirectoryContents(archiveFrom: FilePath, path: FilePath?, keySet: ArchiveHeader.FieldKeySet, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) throws](archivestream/writedirectorycontents(archivefrom:path:keyset:selectusing:flags:threadcount:).md)
  Writes all entries from a directory to the archive stream.
### Extracting Data
- [static func extractStream(extractingTo: FilePath, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) -> ArchiveStream?](archivestream/extractstream(extractingto:selectusing:flags:threadcount:).md)
  Opens an extract output archive stream.
- [static func withExtractStream<E>(extractingTo: FilePath, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int, (ArchiveStream) throws -> E) throws -> E](archivestream/withextractstream(extractingto:selectusing:flags:threadcount:_:).md)
  Calls the given closure with an extract output archive stream.
### Encoding Data
- [static func encodeStream(writingTo: ArchiveByteStream, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) -> ArchiveStream?](archivestream/encodestream(writingto:selectusing:flags:threadcount:).md)
  Opens an encode output archive stream.
- [static func withEncodeStream<E>(writingTo: ArchiveByteStream, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int, (ArchiveStream) throws -> E) throws -> E](archivestream/withencodestream(writingto:selectusing:flags:threadcount:_:).md)
  Calls the given closure with an encode output archive stream.
### Decoding Data
- [static func decodeStream(readingFrom: ArchiveByteStream, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) -> ArchiveStream?](archivestream/decodestream(readingfrom:selectusing:flags:threadcount:).md)
  Opens a decode input archive stream.
- [static func withDecodeStream<E>(readingFrom: ArchiveByteStream, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int, (ArchiveStream) throws -> E) throws -> E](archivestream/withdecodestream(readingfrom:selectusing:flags:threadcount:_:).md)
  Calls the given closure with a decode input archive stream.
### Converting Data
- [static func convertStream(writingTo: ArchiveStream, insertKeySet: ArchiveHeader.FieldKeySet, removeKeySet: ArchiveHeader.FieldKeySet, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) -> ArchiveStream?](archivestream/convertstream(writingto:insertkeyset:removekeyset:selectusing:flags:threadcount:).md)
  Opens a convert output archive stream.
- [static func withConvertStream<E>(writingTo: ArchiveStream, insertKeySet: ArchiveHeader.FieldKeySet, removeKeySet: ArchiveHeader.FieldKeySet, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int, (ArchiveStream) throws -> E) throws -> E](archivestream/withconvertstream(writingto:insertkeyset:removekeyset:selectusing:flags:threadcount:_:).md)
  Calls the given closure with a convert output archive stream.
### Processing Data
- [static func process(readingFrom: ArchiveStream, writingTo: ArchiveStream, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) throws -> Int](archivestream/process(readingfrom:writingto:selectusing:flags:threadcount:).md)
  Processes archive elements between two archive streams.
### Using Custom Streams
- [static func customStream<C>(instance: C) -> ArchiveStream?](archivestream/customstream(instance:).md)
  Returns a new archive stream instance mapped to an object that conforms to the archive stream protocol.
- [static func withStream<C, E>(wrapping: C, (ArchiveStream) throws -> E) throws -> E](archivestream/withstream(wrapping:_:).md)
  Calls the given closure with an archive stream instance mapped to an object that conforms to the archive stream protocol.

## Relationships

### Conforms To
- [ArchiveStreamProtocol](archivestreamprotocol.md)

## See Also

- [protocol ArchiveStreamProtocol](archivestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to data blobs.
- [protocol ArchiveByteStreamProtocol](archivebytestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to buffers.
- [class ArchiveByteStream](archivebytestream.md)
  An archive stream that reads from and writes to buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream)*