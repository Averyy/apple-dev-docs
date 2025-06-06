# extractStream(extractingTo:selectUsing:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Opens an extract output archive stream.

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
static func extractStream(extractingTo directory: FilePath, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0) -> ArchiveStream?
```

#### Return Value

A new archive stream.

#### Discussion

For each entry received by the stream, the operation first calls the `filter` closure with the [`extractBegin`](archiveheader/entrymessage/extractbegin.md) message and `data` referencing an [`ArchiveHeader`](archiveheader.md) instance.

If the `filter` closure returns [`skip`](archiveheader/entrymessagestatus/skip.md), the stream discards the entry. Otherwise, the stream extracts the entry, and then executes the closure with the [`extractAttributes`](archiveheader/entrymessage/extractattributes.md), [`extractXAT`](archiveheader/entrymessage/extractxat.md), [`extractACL`](archiveheader/entrymessage/extractacl.md) messages. Following this closure make modifications to the extracted fields before writing to the filesystem.

When the stream fully extracts the entry, it then executes the closure with an [`extractEnd`](archiveheader/entrymessage/extractend.md) message. When the entry extraction fails, the stream executes the closure with [`extractFail`](archiveheader/entrymessage/extractfail.md). If the closure returns [`cancel`](archiveheader/entrymessagestatus/cancel.md), the stream aborts processing. Otherwise, processing continues.

The stream calls [`extractBegin`](archiveheader/entrymessage/extractbegin.md) messages in archive order and are always the first call for a given entry.

The [`extractEnd`](archiveheader/entrymessage/extractend.md) or [`extractFail`](archiveheader/entrymessage/extractfail.md) messages are always the last call for a given entry, and aren’t necessarily called in the same order. In particular, for directories, the stream may call [`extractEnd`](archiveheader/entrymessage/extractend.md) only after extraction of all directory contents is complete.

## Parameters

- `directory`: The directory that the archive stream writes the extracted entries to.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.

## See Also

- [static func withExtractStream<E>(extractingTo: FilePath, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int, (ArchiveStream) throws -> E) throws -> E](archivestream/withextractstream(extractingto:selectusing:flags:threadcount:_:).md)
  Calls the given closure with an extract output archive stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/extractstream(extractingto:selectusing:flags:threadcount:))*