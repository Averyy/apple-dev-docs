# ArchiveHeader.EntryType

**Framework**: Apple Archive  
**Kind**: struct  
**Role**: Structure

Constants that specify the filesystem entry types.

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
struct EntryType
```

## Topics

### Entry Types
- [static let blockSpecial: ArchiveHeader.EntryType](./entrytype-swift.struct/blockspecial.md)
  A constant that indicates the entry is a block device.
- [static let characterSpecial: ArchiveHeader.EntryType](./entrytype-swift.struct/characterspecial.md)
  A constant that indicates the entry is a character device.
- [static let directory: ArchiveHeader.EntryType](./entrytype-swift.struct/directory.md)
  A constant that indicates the entry is a directory.
- [static let door: ArchiveHeader.EntryType](./entrytype-swift.struct/door.md)
  A constant that indicates the entry is a door.
- [static let fifo: ArchiveHeader.EntryType](./entrytype-swift.struct/fifo.md)
  A constant that indicates the entry is a FIFO special file.
- [static let link: ArchiveHeader.EntryType](./entrytype-swift.struct/link.md)
  A constant that indicates the entry is a symbolic link.
- [static let metadata: ArchiveHeader.EntryType](./entrytype-swift.struct/metadata.md)
  A constant that indicates the entry is metadata.
- [static let port: ArchiveHeader.EntryType](./entrytype-swift.struct/port.md)
  A constant that indicates the entry is a port.
- [static let regularFile: ArchiveHeader.EntryType](./entrytype-swift.struct/regularfile.md)
  A constant that indicates the entry is a regular file.
- [static let socket: ArchiveHeader.EntryType](./entrytype-swift.struct/socket.md)
  A constant that indicates the entry is a socket.
- [static let whiteout: ArchiveHeader.EntryType](./entrytype-swift.struct/whiteout.md)
  A constant that indicates the entry is a whiteout.
### Instance Properties
- [var description: String](./entrytype-swift.struct/description.md)
  A textual representation of this instance.
### Raw Values
- [init(rawValue: UInt32)](./entrytype-swift.struct/init%28rawvalue%29.md)
- [var rawValue: UInt32](./entrytype-swift.struct/rawvalue.md)

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
- [ArchiveHeader.EntryFilter](./entryfilter.md)
  A type alias for the parameters passed to an archive stream operation’s entry selection and status closure.
- [ArchiveHeader.EntryMessage](./entrymessage.md)
  Constants that represent message values for the entry message filters.
- [ArchiveHeader.EntryFilterData](./entryfilterdata.md)
  Enumerations that represent entry filter data.
- [ArchiveHeader.EntryMessageStatus](./entrymessagestatus.md)
  Statuses that you return from an archive stream operation’s entry selection and status closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entrytype-swift.struct)*