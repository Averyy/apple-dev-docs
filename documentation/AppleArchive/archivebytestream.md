# ArchiveByteStream

**Framework**: Apple Archive  
**Kind**: class  
**Role**: Class

An archive stream that reads from and writes to buffers.

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
class ArchiveByteStream
```

## Topics

### Creating an Archive Byte Stream
- [init(object: _AAOptionalObjectWrapper<_AAByteStreamTraits>.AAType?, owned: Bool)](./archivebytestream/init%28object,owned%29.md)
  Returns a new archive byte stream from the specified traits and entry message processing callback.
### Using Archive Byte Streams
- [func close(updatingContext: ArchiveEncryptionContext) throws](./archivebytestream/close%28updatingcontext%29.md)
  Closes the stream, releases associated resources, and writes the sealed container attributes to the specified encryption context.
### Compressing Data
- [static func compressionStream(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./archivebytestream/compressionstream%28using,writingto,blocksize,flags,threadcount%29.md)
  Creates a compression sequential output stream.
- [static func withCompressionStream<E>(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](./archivebytestream/withcompressionstream%28using,writingto,blocksize,flags,threadcount,_%29.md)
  Calls the given closure with a compression sequential output stream.
- [static func compressionStream(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./archivebytestream/compressionstream%28appendingto,flags,threadcount%29.md)
  Reopens a compression sequential output stream.
- [static func withCompressionStream<E>(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](./archivebytestream/withcompressionstream%28appendingto,flags,threadcount,_%29.md)
  Reopens a compression sequential output stream and calls the given closure.
### Decompressing Data
- [static func decompressionStream(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./archivebytestream/decompressionstream%28readingfrom,flags,threadcount%29.md)
  Creates a decompression sequential input stream.
- [static func withDecompressionStream<E>(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](./archivebytestream/withdecompressionstream%28readingfrom,flags,threadcount,_%29.md)
  Calls the given closure with a decompression sequential input stream.
- [static func randomAccessDecompressionStream(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./archivebytestream/randomaccessdecompressionstream%28readingfrom,allocationlimit,flags,threadcount%29.md)
  Creates a decompression random-access input stream.
- [static func withRandomAccessDecompressionStream<E>(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](./archivebytestream/withrandomaccessdecompressionstream%28readingfrom,allocationlimit,flags,threadcount,_%29.md)
  Calls the given closure with a decompression random access input stream.
### Encrypting Data
- [static func encryptionStream(appendingTo: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./archivebytestream/encryptionstream%28appendingto,encryptioncontext,flags,threadcount%29.md)
  Reopens an existing encryption sequential output stream.
- [static func encryptionStream(writingTo: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./archivebytestream/encryptionstream%28writingto,encryptioncontext,flags,threadcount%29.md)
  Creates a encryption sequential input stream.
### Decrypting Data
- [static func decryptionStream(readingFrom: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./archivebytestream/decryptionstream%28readingfrom,encryptioncontext,flags,threadcount%29.md)
  Creates a decryption sequential input stream.
- [static func randomAccessDecryptionStream(readingFrom: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./archivebytestream/randomaccessdecryptionstream%28readingfrom,encryptioncontext,allocationlimit,flags,threadcount%29.md)
  Creates a decryption random access input stream.
### Processing Data
- [static func process(readingFrom: ArchiveByteStream, writingTo: ArchiveByteStream) throws -> Int64](./archivebytestream/process%28readingfrom,writingto%29.md)
  Processes data between two byte streams.
### File Streaming
- [static func fileStream(fd: FileDescriptor, automaticClose: Bool) -> ArchiveByteStream?](./archivebytestream/filestream%28fd,automaticclose%29.md)
  Creates a stream from an open file descriptor.
- [static func withFileStream<E>(fd: FileDescriptor, automaticClose: Bool, (ArchiveByteStream) throws -> E) throws -> E](./archivebytestream/withfilestream%28fd,automaticclose,_%29.md)
  Calls the given closure with a file stream created from the specified file descriptor.
- [static func fileStream(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions) -> ArchiveByteStream?](./archivebytestream/filestream%28path,mode,options,permissions%29.md)
  Opens a new file descriptor using the given path and parameters, and creates a stream from the file descriptor.
- [static func withFileStream<E>(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions, (ArchiveByteStream) throws -> E) throws -> E](./archivebytestream/withfilestream%28path,mode,options,permissions,_%29.md)
  Calls the given closure with a file stream.
- [static func temporaryFileStream() -> ArchiveByteStream?](./archivebytestream/temporaryfilestream%28%29.md)
  Creates a new temporary file stream.
- [static func withTemporaryFileStream<E>((ArchiveByteStream) throws -> E) throws -> E](./archivebytestream/withtemporaryfilestream%28_%29.md)
  Calls the given closure with a temporary file stream.
### Streaming with Custom Streams
- [static func customStream<C>(instance: C) -> ArchiveByteStream?](./archivebytestream/customstream%28instance%29.md)
  Returns a new archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.
- [static func withStream<C, E>(wrapping: C, (ArchiveByteStream) throws -> E) throws -> E](./archivebytestream/withstream%28wrapping,_%29.md)
  Calls the given closure with an archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.
- [static func sharedBufferPipe(capacity: Int) -> (output: ArchiveByteStream, input: ArchiveByteStream)?](./archivebytestream/sharedbufferpipe%28capacity%29.md)
  Creates a pair of streams and links them by a shared buffer.

## Relationships

### Conforms To
- [ArchiveByteStreamProtocol](./archivebytestreamprotocol.md)

## See Also

### Apple Archive streams
- [protocol ArchiveStreamProtocol](./archivestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to data blobs.
- [class ArchiveStream](./archivestream.md)
  An archive stream that reads from and writes to data blobs
- [protocol ArchiveByteStreamProtocol](./archivebytestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream)*