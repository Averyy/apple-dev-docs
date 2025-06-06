# withEncodeStream(writingTo:selectUsing:flags:threadCount:_:)

**Framework**: Apple Archive  
**Kind**: method

Calls the given closure with an encode output archive stream.

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
static func withEncodeStream<E>(writingTo stream: ArchiveByteStream, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0, _ body: (ArchiveStream) throws -> E) throws -> E
```

#### Return Value

The result of the closure.

#### Discussion

This function opens a stream created by [`encodeStream(writingTo:selectUsing:flags:threadCount:)`](archivestream/encodestream(writingto:selectusing:flags:threadcount:).md), calls the specified closure, and closes the stream.

## Parameters

- `stream`: The byte stream that receives the encoded data.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.
- `body`: A closure with the archive stream passed as a parameter.

## See Also

- [static func encodeStream(writingTo: ArchiveByteStream, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) -> ArchiveStream?](archivestream/encodestream(writingto:selectusing:flags:threadcount:).md)
  Opens an encode output archive stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/withencodestream(writingto:selectusing:flags:threadcount:_:))*