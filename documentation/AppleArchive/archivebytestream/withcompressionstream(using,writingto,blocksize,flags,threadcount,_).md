# withCompressionStream(using:writingTo:blockSize:flags:threadCount:_:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Type Method

Calls the given closure with a compression sequential output stream.

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
static func withCompressionStream<E>(using compressionAlgorithm: ArchiveCompression, writingTo compressedStream: ArchiveByteStream, blockSize: Int = (1<<20), flags: ArchiveFlags = [], threadCount: Int = 0, _ body: (ArchiveByteStream) throws -> E) throws -> E
```

#### Return Value

The result of the closure.

## Parameters

- `compressionAlgorithm`: The compression algorithm.
- `compressedStream`: An output stream that receives compressed data, the operation only calls write methods.
- `blockSize`: The compression block size, in bytes.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to `0` for default.
- `body`: A closure with the archive byte stream passed as a parameter.

## See Also

### Compressing Data
- [static func compressionStream(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./compressionstream%28using,writingto,blocksize,flags,threadcount%29.md)
  Creates a compression sequential output stream.
- [static func compressionStream(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./compressionstream%28appendingto,flags,threadcount%29.md)
  Reopens a compression sequential output stream.
- [static func withCompressionStream<E>(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](./withcompressionstream%28appendingto,flags,threadcount,_%29.md)
  Reopens a compression sequential output stream and calls the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/withcompressionstream(using:writingto:blocksize:flags:threadcount:_:))*