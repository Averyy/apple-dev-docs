# withCompressionStream(appendingTo:flags:threadCount:_:)

**Framework**: Apple Archive  
**Kind**: method

Reopens a compression sequential output stream and calls the given closure.

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
static func withCompressionStream<E>(appendingTo compressedStream: ArchiveByteStream, flags: ArchiveFlags = [], threadCount: Int = 0, _ body: (ArchiveByteStream) throws -> E) throws -> E
```

#### Return Value

The result of the closure.

#### Discussion

This function opens a stream created by [`compressionStream(appendingTo:flags:threadCount:)`](archivebytestream/compressionstream(appendingto:flags:threadcount:).md), calls the specified closure, and closes the stream.

## Parameters

- `compressedStream`: The output stream that the function reopens and receives the compressed data.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.
- `body`: A closure with the archive byte stream passed as a parameter.

## See Also

- [static func compressionStream(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/compressionstream(using:writingto:blocksize:flags:threadcount:).md)
  Creates a compression sequential output stream.
- [static func withCompressionStream<E>(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withcompressionstream(using:writingto:blocksize:flags:threadcount:_:).md)
  Calls the given closure with a compression sequential output stream.
- [static func compressionStream(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/compressionstream(appendingto:flags:threadcount:).md)
  Reopens a compression sequential output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/withcompressionstream(appendingto:flags:threadcount:_:))*