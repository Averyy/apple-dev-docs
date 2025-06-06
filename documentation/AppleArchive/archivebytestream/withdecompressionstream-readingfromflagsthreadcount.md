# withDecompressionStream(readingFrom:flags:threadCount:_:)

**Framework**: Apple Archive  
**Kind**: method

Calls the given closure with a decompression sequential input stream.

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
static func withDecompressionStream<E>(readingFrom compressedStream: ArchiveByteStream, flags: ArchiveFlags = [], threadCount: Int = 0, _ body: (ArchiveByteStream) throws -> E) throws -> E
```

#### Return Value

The result of the closure.

#### Discussion

This function opens a stream created by [`decompressionStream(readingFrom:flags:threadCount:)`](archivebytestream/decompressionstream(readingfrom:flags:threadcount:).md), calls the specified closure, and closes the stream.

## Parameters

- `compressedStream`: An input stream that provides compressed data, the operation only calls   and  .
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.
- `body`: A closure with the archive byte stream passed as a parameter.

## See Also

- [static func decompressionStream(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/decompressionstream(readingfrom:flags:threadcount:).md)
  Creates a decompression sequential input stream.
- [static func randomAccessDecompressionStream(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](archivebytestream/randomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:).md)
  Creates a decompression random-access input stream.
- [static func withRandomAccessDecompressionStream<E>(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withrandomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:_:).md)
  Calls the given closure with a decompression random access input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/withdecompressionstream(readingfrom:flags:threadcount:_:))*