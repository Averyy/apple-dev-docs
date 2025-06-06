# decompressionStream(readingFrom:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Creates a decompression sequential input stream.

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
static func decompressionStream(readingFrom compressedStream: ArchiveByteStream, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveByteStream?
```

#### Return Value

A new archive byte stream.

## Parameters

- `compressedStream`: An input stream that provides compressed data, the operation only calls   and  .
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func withDecompressionStream<E>(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withdecompressionstream(readingfrom:flags:threadcount:_:).md)
  Calls the given closure with a decompression sequential input stream.
- [static func randomAccessDecompressionStream(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/randomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:).md)
  Creates a decompression random-access input stream.
- [static func withRandomAccessDecompressionStream<E>(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withrandomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:_:).md)
  Calls the given closure with a decompression random access input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/decompressionstream(readingfrom:flags:threadcount:))*