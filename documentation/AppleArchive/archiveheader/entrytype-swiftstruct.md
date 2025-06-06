# ArchiveHeader.EntryType

**Framework**: Apple Archive  
**Kind**: struct

Constants that specify the filesystem entry types.

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
struct EntryType
```

## Topics

### Entry Types
- [static let blockSpecial: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/blockspecial.md)
  A constant that indicates the entry is a block device.
- [static let characterSpecial: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/characterspecial.md)
  A constant that indicates the entry is a character device.
- [static let directory: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/directory.md)
  A constant that indicates the entry is a directory.
- [static let door: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/door.md)
  A constant that indicates the entry is a door.
- [static let fifo: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/fifo.md)
  A constant that indicates the entry is a FIFO special file.
- [static let link: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/link.md)
  A constant that indicates the entry is a symbolic link.
- [static let metadata: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/metadata.md)
  A constant that indicates the entry is metadata.
- [static let port: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/port.md)
  A constant that indicates the entry is a port.
- [static let regularFile: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/regularfile.md)
  A constant that indicates the entry is a regular file.
- [static let socket: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/socket.md)
  A constant that indicates the entry is a socket.
- [static let whiteout: ArchiveHeader.EntryType](archiveheader/entrytype-swift.struct/whiteout.md)
  A constant that indicates the entry is a whiteout.
### Instance Properties
- [var description: String](archiveheader/entrytype-swift.struct/description.md)
  A textual representation of this instance.
### Raw Values
- [init(rawValue: UInt32)](archiveheader/entrytype-swift.struct/init(rawvalue:).md)
- [var rawValue: UInt32](archiveheader/entrytype-swift.struct/rawvalue.md)

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
- [ArchiveHeader.EntryFilter](archiveheader/entryfilter.md)
  A type alias for the parameters passed to an archive stream operation’s entry selection and status closure.
- [ArchiveHeader.EntryMessage](archiveheader/entrymessage.md)
  Constants that represent message values for the entry message filters.
- [ArchiveHeader.EntryFilterData](archiveheader/entryfilterdata.md)
  Enumerations that represent entry filter data.
- [ArchiveHeader.EntryMessageStatus](archiveheader/entrymessagestatus.md)
  Statuses that you return from an archive stream operation’s entry selection and status closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entrytype-swift.struct)*