# process(readingFrom:writingTo:selectUsing:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Processes archive elements between two archive streams.

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
static func process(readingFrom input: ArchiveStream, writingTo output: ArchiveStream, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0) throws -> Int
```

#### Return Value

The number of processed bytes.

## Parameters

- `input`: The input stream.
- `output`: The output stream.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/process(readingfrom:writingto:selectusing:flags:threadcount:))*