# compressionStream(using:writingTo:blockSize:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Creates a compression sequential output stream.

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
static func compressionStream(using compressionAlgorithm: ArchiveCompression, writingTo compressedStream: ArchiveByteStream, blockSize: Int = (1<<20), flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

#### Discussion

The new stream writes compressed data to the supplied archive byte stream.

The stream that the function returns only implements [`write(from:)`](archivebytestreamprotocol/write(from:).md) and [`write(from:atOffset:)`](archivebytestreamprotocol/write(from:atoffset:).md).

During compression the operation splits the data into blocks of `blockSize` bytes, compressing each block independently. Larger blocks provide better compression, but require more memory (for compression and decompression) and increase latency in random access.

Good values for `blockSize` are between 256 KB and 16 MB. The 1 MB default value provides a good compromise between compression ratio and memory requirement.

## Parameters

- `compressionAlgorithm`: The compression algorithm.
- `compressedStream`: An output stream that receives compressed data, the operation only calls write methods.
- `blockSize`: The compression block size, in bytes.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func withCompressionStream<E>(using: ArchiveCompression, writingTo: ArchiveByteStream, blockSize: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withcompressionstream(using:writingto:blocksize:flags:threadcount:_:).md)
  Calls the given closure with a compression sequential output stream.
- [static func compressionStream(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/compressionstream(appendingto:flags:threadcount:).md)
  Reopens a compression sequential output stream.
- [static func withCompressionStream<E>(appendingTo: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withcompressionstream(appendingto:flags:threadcount:_:).md)
  Reopens a compression sequential output stream and calls the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/compressionstream(using:writingto:blocksize:flags:threadcount:))*