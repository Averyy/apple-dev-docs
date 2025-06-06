# withExtractStream(extractingTo:selectUsing:flags:threadCount:_:)

**Framework**: Apple Archive  
**Kind**: method

Calls the given closure with an extract output archive stream.

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
static func withExtractStream<E>(extractingTo directory: FilePath, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0, _ body: (ArchiveStream) throws -> E) throws -> E
```

#### Return Value

The result of the closure.

#### Discussion

This function opens a stream created by [`extractStream(extractingTo:selectUsing:flags:threadCount:)`](archivestream/extractstream(extractingto:selectusing:flags:threadcount:).md), calls the specified closure, and closes the stream.

## Parameters

- `directory`: The directory that the archive stream writes the extracted entries to.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.
- `body`: A closure with the archive stream passed as a parameter.

## See Also

- [static func extractStream(extractingTo: FilePath, selectUsing: ArchiveHeader.EntryFilter?, flags: ArchiveFlags, threadCount: Int) -> ArchiveStream?](archivestream/extractstream(extractingto:selectusing:flags:threadcount:).md)
  Opens an extract output archive stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/withextractstream(extractingto:selectusing:flags:threadcount:_:))*