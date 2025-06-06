# ArchiveHeader.EntryFilter

**Framework**: Apple Archive  
**Kind**: typealias

A type alias for the parameters passed to an archive stream operation’s entry selection and status closure.

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
typealias EntryFilter = (ArchiveHeader.EntryMessage, FilePath, ArchiveHeader.EntryFilterData?) -> ArchiveHeader.EntryMessageStatus
```

## See Also

- [ArchiveHeader.EntryAttributes](archiveheader/entryattributes.md)
  An object that describes archive entry attributes.
- [ArchiveHeader.EntryXATBlob](archiveheader/entryxatblob.md)
  An object that describes the extended attributes of an archive entry.
- [var entryType: ArchiveHeader.EntryType?](archiveheader/entrytype-swift.property.md)
  The entry type from `TYP` field, or `nil` if missing or invalid.
- [ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct.md)
  Constants that specify the filesystem entry types.
- [ArchiveHeader.EntryMessage](archiveheader/entrymessage.md)
  Constants that represent message values for the entry message filters.
- [ArchiveHeader.EntryFilterData](archiveheader/entryfilterdata.md)
  Enumerations that represent entry filter data.
- [ArchiveHeader.EntryMessageStatus](archiveheader/entrymessagestatus.md)
  Statuses that you return from an archive stream operation’s entry selection and status closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryfilter)*