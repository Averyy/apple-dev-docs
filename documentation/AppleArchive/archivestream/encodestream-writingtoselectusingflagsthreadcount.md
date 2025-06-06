# encodeStream(writingTo:selectUsing:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Opens an encode output archive stream.

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
static func encodeStream(writingTo stream: ArchiveByteStream, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveStream?
```

#### Return Value

A new archive stream.

## Parameters

- `stream`: The byte stream that recieves the encoded data.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func withEncodeStream<E>(writingTo: ArchiveByteStream, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int, (ArchiveStream) throws -> E) throws -> E](archivestream/withencodestream(writingto:selectusing:flags:threadcount:_:).md)
  Calls the given closure with an encode output archive stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/encodestream(writingto:selectusing:flags:threadcount:))*