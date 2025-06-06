# withConvertStream(writingTo:insertKeySet:removeKeySet:selectUsing:flags:threadCount:_:)

**Framework**: Apple Archive  
**Kind**: method

Calls the given closure with a convert output archive stream.

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
static func withConvertStream<E>(writingTo stream: ArchiveStream, insertKeySet: ArchiveHeader.FieldKeySet, removeKeySet: ArchiveHeader.FieldKeySet, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0, _ body: (ArchiveStream) throws -> E) throws -> E
```

#### Return Value

The result of the closure.

#### Discussion

This function opens a stream created by [`convertStream(writingTo:insertKeySet:removeKeySet:selectUsing:flags:threadCount:)`](archivestream/convertstream(writingto:insertkeyset:removekeyset:selectusing:flags:threadcount:).md), calls the specified closure, and closes the stream.

## Parameters

- `stream`: The stream that receives the converted archive stream.
- `insertKeySet`: A set of keys to fields that the operation inserts into the converted archive.
- `removeKeySet`: A set of keys to fields that the operation removes from the converted archive.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.
- `body`: A closure with the archive stream passed as a parameter.

## See Also

- [static func convertStream(writingTo: ArchiveStream, insertKeySet: ArchiveHeader.FieldKeySet, removeKeySet: ArchiveHeader.FieldKeySet, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) -> ArchiveStream?](archivestream/convertstream(writingto:insertkeyset:removekeyset:selectusing:flags:threadcount:).md)
  Opens a convert output archive stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/withconvertstream(writingto:insertkeyset:removekeyset:selectusing:flags:threadcount:_:))*