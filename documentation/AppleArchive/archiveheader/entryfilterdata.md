# ArchiveHeader.EntryFilterData

**Framework**: Apple Archive  
**Kind**: enum

Enumerations that represent entry filter data.

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
enum EntryFilterData
```

## Topics

### Enumeration Cases
- [case entryAttributes(ArchiveHeader.EntryAttributes)](archiveheader/entryfilterdata/entryattributes(_:).md)
  An enumeration that represents entry attributes.
- [ArchiveHeader.EntryFilterData.entryXAT(_:)](archiveheader/entryfilterdata/entryxat(_:).md)
  An enumeration that represents extended attributes.
- [ArchiveHeader.EntryFilterData.header(_:)](archiveheader/entryfilterdata/header(_:).md)
  An enumeration that represents an archive header.

## See Also

- [ArchiveHeader.EntryAttributes](archiveheader/entryattributes.md)
  An object that describes archive entry attributes.
- [ArchiveHeader.EntryXATBlob](archiveheader/entryxatblob.md)
  An object that describes the extended attributes of an archive entry.
- [var entryType: ArchiveHeader.EntryType?](archiveheader/entrytype-swift.property.md)
  The entry type from `TYP` field, or `nil` if missing or invalid.
- [ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct.md)
  Constants that specify the filesystem entry types.
- [ArchiveHeader.EntryFilter](archiveheader/entryfilter.md)
  A type alias for the parameters passed to an archive stream operation’s entry selection and status closure.
- [ArchiveHeader.EntryMessage](archiveheader/entrymessage.md)
  Constants that represent message values for the entry message filters.
- [ArchiveHeader.EntryMessageStatus](archiveheader/entrymessagestatus.md)
  Statuses that you return from an archive stream operation’s entry selection and status closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryfilterdata)*