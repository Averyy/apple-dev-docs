# randomAccessDecompressionStream(readingFrom:allocationLimit:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Creates a decompression random-access input stream.

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
static func randomAccessDecompressionStream(readingFrom compressedStream: ArchiveByteStream, allocationLimit: Int = Int.max, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

#### Discussion

The operation reads compressed data from the suppled archive byte stream, `compressedStream`. The stream that the function returns implements read and seek methods.

Pass `allocationLimit` as a hint to control the stream’s memory allocation for in-out buffers for each thread and cache for uncompressed data. The stream creation adjusts both the actual number of decompression threads and the cache size to attempt to satisfy the allocation request.

## Parameters

- `compressedStream`: An input stream that provides compressed data.
- `allocationLimit`: The requested memory allocation size, in bytes. Set to   for lowest memory footprint or   for best performance.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func decompressionStream(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/decompressionstream(readingfrom:flags:threadcount:).md)
  Creates a decompression sequential input stream.
- [static func withDecompressionStream<E>(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withdecompressionstream(readingfrom:flags:threadcount:_:).md)
  Calls the given closure with a decompression sequential input stream.
- [static func withRandomAccessDecompressionStream<E>(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withrandomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:_:).md)
  Calls the given closure with a decompression random access input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/randomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:))*