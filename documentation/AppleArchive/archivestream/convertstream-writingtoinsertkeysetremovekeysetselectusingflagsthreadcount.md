# convertStream(writingTo:insertKeySet:removeKeySet:selectUsing:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Opens a convert output archive stream.

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
static func convertStream(writingTo stream: ArchiveStream, insertKeySet: ArchiveHeader.FieldKeySet, removeKeySet: ArchiveHeader.FieldKeySet, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveStream?
```

#### Return Value

A new archive stream.

## Parameters

- `stream`: The stream that receives the converted archive stream.
- `insertKeySet`: A set of keys to fields that the operation inserts into the converted archive.
- `removeKeySet`: A set of keys to fields that the operation removes from the converted archive.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func withConvertStream<E>(writingTo: ArchiveStream, insertKeySet: ArchiveHeader.FieldKeySet, removeKeySet: ArchiveHeader.FieldKeySet, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int, (ArchiveStream) throws -> E) throws -> E](archivestream/withconvertstream(writingto:insertkeyset:removekeyset:selectusing:flags:threadcount:_:).md)
  Calls the given closure with a convert output archive stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/convertstream(writingto:insertkeyset:removekeyset:selectusing:flags:threadcount:))*