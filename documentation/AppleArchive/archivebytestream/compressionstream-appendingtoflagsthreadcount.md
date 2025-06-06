# compressionStream(appendingTo:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Reopens a compression sequential output stream.

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
static func compressionStream(appendingTo compressedStream: ArchiveByteStream, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

#### Discussion

The operation writes compressed data to the end of the supplied archive byte stream, `compressedStream`. `compressedStream` must implement [`seek(toOffset:relativeTo:)`](archivebytestreamprotocol/seek(tooffset:relativeto:).md), and the read and write functions.

The stream that the function returns only implements [`write(from:)`](archivebytestreamprotocol/write(from:).md) and [`write(from:atOffset:)`](archivebytestreamprotocol/write(from:atoffset:).md).

## Parameters

- `compressedStream`: The output stream that the function reopens and receives the compressed data.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func compressionStream(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/compressionstream(using:writingto:blocksize:flags:threadcount:).md)
  Creates a compression sequential output stream.
- [static func withCompressionStream<E>(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withcompressionstream(using:writingto:blocksize:flags:threadcount:_:).md)
  Calls the given closure with a compression sequential output stream.
- [static func withCompressionStream<E>(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withcompressionstream(appendingto:flags:threadcount:_:).md)
  Reopens a compression sequential output stream and calls the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/compressionstream(appendingto:flags:threadcount:))*