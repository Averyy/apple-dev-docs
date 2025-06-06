# ArchiveByteStream

**Framework**: Apple Archive  
**Kind**: class

An archive stream that reads from and writes to buffers.

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
class ArchiveByteStream
```

## Topics

### Creating an Archive Byte Stream
- [init(object: _AAOptionalObjectWrapper<_AAByteStreamTraits>.AAType?, owned: Bool)](archivebytestream/init(object:owned:).md)
  Returns a new archive byte stream from the specified traits and entry message processing callback.
### Using Archive Byte Streams
- [func close(updatingContext: ArchiveEncryptionContext) throws](archivebytestream/close(updatingcontext:).md)
  Closes the stream, releases associated resources, and writes the sealed container attributes to the specified encryption context.
### Compressing Data
- [static func compressionStream(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/compressionstream(using:writingto:blocksize:flags:threadcount:).md)
  Creates a compression sequential output stream.
- [static func withCompressionStream<E>(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withcompressionstream(using:writingto:blocksize:flags:threadcount:_:).md)
  Calls the given closure with a compression sequential output stream.
- [static func compressionStream(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/compressionstream(appendingto:flags:threadcount:).md)
  Reopens a compression sequential output stream.
- [static func withCompressionStream<E>(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withcompressionstream(appendingto:flags:threadcount:_:).md)
  Reopens a compression sequential output stream and calls the given closure.
### Decompressing Data
- [static func decompressionStream(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/decompressionstream(readingfrom:flags:threadcount:).md)
  Creates a decompression sequential input stream.
- [static func withDecompressionStream<E>(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withdecompressionstream(readingfrom:flags:threadcount:_:).md)
  Calls the given closure with a decompression sequential input stream.
- [static func randomAccessDecompressionStream(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/randomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:).md)
  Creates a decompression random-access input stream.
- [static func withRandomAccessDecompressionStream<E>(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withrandomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:_:).md)
  Calls the given closure with a decompression random access input stream.
### Encrypting Data
- [static func encryptionStream(appendingTo: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/encryptionstream(appendingto:encryptioncontext:flags:threadcount:).md)
  Reopens an existing encryption sequential output stream.
- [static func encryptionStream(writingTo: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/encryptionstream(writingto:encryptioncontext:flags:threadcount:).md)
  Creates a encryption sequential input stream.
### Decrypting Data
- [static func decryptionStream(readingFrom: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/decryptionstream(readingfrom:encryptioncontext:flags:threadcount:).md)
  Creates a decryption sequential input stream.
- [static func randomAccessDecryptionStream(readingFrom: ArchiveByteStream, encryptionContext: ArchiveEncryptionContext, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/randomaccessdecryptionstream(readingfrom:encryptioncontext:allocationlimit:flags:threadcount:).md)
  Creates a decryption random access input stream.
### Processing Data
- [static func process(readingFrom: ArchiveByteStream, writingTo: ArchiveByteStream) throws -> Int64](archivebytestream/process(readingfrom:writingto:).md)
  Processes data between two byte streams.
### File Streaming
- [static func fileStream(fd: FileDescriptor, automaticClose: Bool) -> ArchiveByteStream?](archivebytestream/filestream(fd:automaticclose:).md)
  Creates a stream from an open file descriptor.
- [static func withFileStream<E>(fd: FileDescriptor, automaticClose: Bool, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withfilestream(fd:automaticclose:_:).md)
  Calls the given closure with a file stream created from the specified file descriptor.
- [static func fileStream(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions) -> ArchiveByteStream?](archivebytestream/filestream(path:mode:options:permissions:).md)
  Opens a new file descriptor using the given path and parameters, and creates a stream from the file descriptor.
- [static func withFileStream<E>(path: FilePath, mode: FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withfilestream(path:mode:options:permissions:_:).md)
  Calls the given closure with a file stream.
- [static func temporaryFileStream() -> ArchiveByteStream?](archivebytestream/temporaryfilestream.md)
  Creates a new temporary file stream.
- [static func withTemporaryFileStream<E>((ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withtemporaryfilestream(_:).md)
  Calls the given closure with a temporary file stream.
### Streaming with Custom Streams
- [static func customStream<C>(instance: C) -> ArchiveByteStream?](archivebytestream/customstream(instance:).md)
  Returns a new archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.
- [static func withStream<C, E>(wrapping: C, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withstream(wrapping:_:).md)
  Calls the given closure with an archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.
- [static func sharedBufferPipe(capacity: Int) -> (output: ArchiveByteStream, input: ArchiveByteStream)?](archivebytestream/sharedbufferpipe(capacity:).md)
  Creates a pair of streams and links them by a shared buffer.

## Relationships

### Conforms To
- [ArchiveByteStreamProtocol](archivebytestreamprotocol.md)

## See Also

- [protocol ArchiveStreamProtocol](archivestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to data blobs.
- [class ArchiveStream](archivestream.md)
  An archive stream that reads from and writes to data blobs
- [protocol ArchiveByteStreamProtocol](archivebytestreamprotocol.md)
  A set of methods that defines the interface for using an archive stream that reads from and writes to buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream)*