# ArchiveHeader.EntryMessageStatus

**Framework**: Apple Archive  
**Kind**: struct

Statuses that you return from an archive stream operation’s entry selection and status closure.

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
struct EntryMessageStatus
```

## Topics

### Entry Message Statuses
- [static let cancel: ArchiveHeader.EntryMessageStatus](archiveheader/entrymessagestatus/cancel.md)
  An entry message status that indicates the operation cancels processing as soon as possible.
- [static let ok: ArchiveHeader.EntryMessageStatus](archiveheader/entrymessagestatus/ok.md)
  An entry message status that indicates the operation keeps the entry.
- [static let skip: ArchiveHeader.EntryMessageStatus](archiveheader/entrymessagestatus/skip.md)
  An entry message status that indicates the operation skips the entry.
### Instance Properties
- [var description: String](archiveheader/entrymessagestatus/description.md)
  A textual representation of this instance.
### Raw Values
- [var rawValue: Int32](archiveheader/entrymessagestatus/rawvalue.md)
- [init(rawValue: Int32)](archiveheader/entrymessagestatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

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
- [ArchiveHeader.EntryFilterData](archiveheader/entryfilterdata.md)
  Enumerations that represent entry filter data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entrymessagestatus)*