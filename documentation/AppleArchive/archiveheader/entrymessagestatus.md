# ArchiveHeader.EntryMessageStatus

**Framework**: Apple Archive  
**Kind**: struct  
**Role**: Structure

Statuses that you return from an archive stream operation’s entry selection and status closure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
struct EntryMessageStatus
```

## Topics

### Entry Message Statuses
- [static let cancel: ArchiveHeader.EntryMessageStatus](./entrymessagestatus/cancel.md)
  An entry message status that indicates the operation cancels processing as soon as possible.
- [static let ok: ArchiveHeader.EntryMessageStatus](./entrymessagestatus/ok.md)
  An entry message status that indicates the operation keeps the entry.
- [static let skip: ArchiveHeader.EntryMessageStatus](./entrymessagestatus/skip.md)
  An entry message status that indicates the operation skips the entry.
### Instance Properties
- [var description: String](./entrymessagestatus/description.md)
  A textual representation of this instance.
### Raw Values
- [var rawValue: Int32](./entrymessagestatus/rawvalue.md)
- [init(rawValue: Int32)](./entrymessagestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Manipulating Entries
- [ArchiveHeader.EntryAttributes](./entryattributes.md)
  An object that describes archive entry attributes.
- [ArchiveHeader.EntryXATBlob](./entryxatblob.md)
  An object that describes the extended attributes of an archive entry.
- [var entryType: ArchiveHeader.EntryType?](./entrytype-swift.property.md)
  The entry type from `TYP` field, or `nil` if missing or invalid.
- [ArchiveHeader.EntryType](./entrytype-swift.struct.md)
  Constants that specify the filesystem entry types.
- [ArchiveHeader.EntryFilter](./entryfilter.md)
  A type alias for the parameters passed to an archive stream operation’s entry selection and status closure.
- [ArchiveHeader.EntryMessage](./entrymessage.md)
  Constants that represent message values for the entry message filters.
- [ArchiveHeader.EntryFilterData](./entryfilterdata.md)
  Enumerations that represent entry filter data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entrymessagestatus)*