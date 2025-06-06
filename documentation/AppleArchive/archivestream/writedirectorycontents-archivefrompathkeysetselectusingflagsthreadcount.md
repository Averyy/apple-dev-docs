# writeDirectoryContents(archiveFrom:path:keySet:selectUsing:flags:threadCount:)

**Framework**: Apple Archive  
**Kind**: method

Writes all entries from a directory to the archive stream.

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
func writeDirectoryContents(archiveFrom directory: FilePath, path: FilePath? = nil, keySet: ArchiveHeader.FieldKeySet, selectUsing filter: ArchiveHeader.EntryFilter? = nil, flags: ArchiveFlags = [], threadCount: Int = 0) throws
```

## Parameters

- `directory`: The base directory that the operation scans and archives.
- `path`: An optional subdirectory to restrict the scan.
- `keySet`: The fields to include for each entry.
- `filter`: A closure that’s called for each entry that’s received by the stream.
- `flags`: Flags that control the behavior of the operation.
- `threadCount`: The number of worker threads that the operation uses, set to   for default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/writedirectorycontents(archivefrom:path:keyset:selectusing:flags:threadcount:))*