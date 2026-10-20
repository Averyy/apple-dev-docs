# ArchiveHeader.EntryMessage

**Framework**: Apple Archive  
**Kind**: struct  
**Role**: Structure

Constants that represent message values for the entry message filters.

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
struct EntryMessage
```

## Topics

### Entry Messages
- [static let convertExclude: ArchiveHeader.EntryMessage](./entrymessage/convertexclude.md)
  An entry message indicating the conversion operation has skipped the entry as the path data is an archive header instance.
- [static let decodeReading: ArchiveHeader.EntryMessage](./entrymessage/decodereading.md)
  An entry message indicating the decoder operation is reading the entry at path.
- [static let encodeScanning: ArchiveHeader.EntryMessage](./entrymessage/encodescanning.md)
  An entry message indicating the encoder operation is scanning the entry at path.
- [static let encodeWriting: ArchiveHeader.EntryMessage](./entrymessage/encodewriting.md)
  An entry message indicating the encoder operation is writing the entry at path.
- [static let extractACL: ArchiveHeader.EntryMessage](./entrymessage/extractacl.md)
  An entry message indicating the extraction operation has modified entry access control lists.
- [static let extractAttributes: ArchiveHeader.EntryMessage](./entrymessage/extractattributes.md)
  An entry message indicating the extraction operation has modified entry attributes, and that the data is an entry attributes instance.
- [static let extractBegin: ArchiveHeader.EntryMessage](./entrymessage/extractbegin.md)
  An entry message indicating the extraction operation has began, this is the first message for this entry.
- [static let extractEnd: ArchiveHeader.EntryMessage](./entrymessage/extractend.md)
  An entry message indicating the extraction operation has ended, this is the last message for this entry.
- [static let extractFail: ArchiveHeader.EntryMessage](./entrymessage/extractfail.md)
  An entry message indicating the extraction operation has failed, this is the last message for this entry.
- [static let extractXAT: ArchiveHeader.EntryMessage](./entrymessage/extractxat.md)
  An entry message indicating the extraction operation has modified entry extended attributes, and that the data is an entry extended attributes blob.
- [static let processExclude: ArchiveHeader.EntryMessage](./entrymessage/processexclude.md)
  An entry message indicating the process operation has skipped this entry and that the data is an archive header instance.
- [static let searchExclude: ArchiveHeader.EntryMessage](./entrymessage/searchexclude.md)
  An entry message indicating the operation has excluded the entry, specified by path, in search.
- [static let searchFail: ArchiveHeader.EntryMessage](./entrymessage/searchfail.md)
  An entry message indicating the operation has reported an error in search.
- [static let searchPruneDirectory: ArchiveHeader.EntryMessage](./entrymessage/searchprunedirectory.md)
  An entry message indicating the operation has skipped the directory, specified by path, in search.
### Instance Properties
- [var description: String](./entrymessage/description.md)
  A textual representation of this instance.
### Raw Values
- [var rawValue: UInt32](./entrymessage/rawvalue.md)
- [init(rawValue: UInt32)](./entrymessage/init%28rawvalue%29.md)

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
- [ArchiveHeader.EntryFilterData](./entryfilterdata.md)
  Enumerations that represent entry filter data.
- [ArchiveHeader.EntryMessageStatus](./entrymessagestatus.md)
  Statuses that you return from an archive stream operation’s entry selection and status closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entrymessage)*