# decodeStream(readingFrom:selectUsing:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Opens a decode input archive stream.

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
static func decodeStream(readingFrom stream: ArchiveByteStream, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveStream?
```

#### Return Value

A new archive stream.

## Parameters

- `stream`: The byte stream that provides the encoded data.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func withDecodeStream<E>(readingFrom: ArchiveByteStream, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int, (ArchiveStream) throws -> E) throws -> E](archivestream/withdecodestream(readingfrom:selectusing:flags:threadcount:_:).md)
  Calls the given closure with a decode input archive stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/decodestream(readingfrom:selectusing:flags:threadcount:))*