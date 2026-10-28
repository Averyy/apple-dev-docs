# withCompressionStream(appendingTo:flags:threadCount:_:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Type Method

Reopens a compression sequential output stream and calls the given closure.

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
static func withCompressionStream<E>(appendingTo compressedStream: ArchiveByteStream, flags: ArchiveFlags = [], threadCount: Int = 0, _ body: (ArchiveByteStream) throws -> E) throws -> E
```

## Return Value

The result of the closure.

## Discussion

This function opens a stream created by [`compressionStream(appendingTo:flags:threadCount:)`](./compressionstream%28appendingto,flags,threadcount%29.md), calls the specified closure, and closes the stream.

## Parameters

- `compressedStream`: The output stream that the function reopens and receives the compressed data.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to `0` for default.
- `body`: A closure with the archive byte stream passed as a parameter.

## See Also

### Compressing Data
- [static func compressionStream(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./compressionstream%28using,writingto,blocksize,flags,threadcount%29.md)
  Creates a compression sequential output stream.
- [static func withCompressionStream<E>(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](./withcompressionstream%28using,writingto,blocksize,flags,threadcount,_%29.md)
  Calls the given closure with a compression sequential output stream.
- [static func compressionStream(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./compressionstream%28appendingto,flags,threadcount%29.md)
  Reopens a compression sequential output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/withcompressionstream(appendingto:flags:threadcount:_:))*