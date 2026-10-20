# withRandomAccessDecompressionStream(readingFrom:allocationLimit:flags:threadCount:_:)

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Type Method

Calls the given closure with a decompression random access input stream.

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
static func withRandomAccessDecompressionStream<E>(readingFrom compressedStream: ArchiveByteStream, allocationLimit: Int = Int.max, flags: ArchiveFlags = [], threadCount: Int = 0, _ body: (ArchiveByteStream) throws -> E) throws -> E
```

#### Return Value

The result of the closure.

#### Discussion

This function opens a stream created by [`randomAccessDecompressionStream(readingFrom:allocationLimit:flags:threadCount:)`](./randomaccessdecompressionstream%28readingfrom,allocationlimit,flags,threadcount%29.md), calls the specified closure, and closes the stream.

## Parameters

- `compressedStream`: An input stream that provides compressed data.
- `allocationLimit`: The requested memory allocation size, in bytes. Set to `0` for lowest memory footprint or [`max`](../../Swift/int/max.md) for best performance.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to `0` for default.
- `body`: A closure with the archive byte stream passed as a parameter.

## See Also

### Decompressing Data
- [static func decompressionStream(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./decompressionstream%28readingfrom,flags,threadcount%29.md)
  Creates a decompression sequential input stream.
- [static func withDecompressionStream<E>(readingFrom: ArchiveByteStream, flags: ArchiveFlags, threadCount: Int, (ArchiveByteStream) throws -> E) throws -> E](./withdecompressionstream%28readingfrom,flags,threadcount,_%29.md)
  Calls the given closure with a decompression sequential input stream.
- [static func randomAccessDecompressionStream(readingFrom: ArchiveByteStream, allocationLimit: Int, flags: ArchiveFlags, threadCount: Int) -> ArchiveByteStream?](./randomaccessdecompressionstream%28readingfrom,allocationlimit,flags,threadcount%29.md)
  Creates a decompression random-access input stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/withrandomaccessdecompressionstream(readingfrom:allocationlimit:flags:threadcount:_:))*