# ArchiveHeader.EntryAttributes

**Framework**: Apple Archive  
**Kind**: class

An object that describes archive entry attributes.

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
class EntryAttributes
```

## Topics

### Instance Properties
- [var btm: timespec?](archiveheader/entryattributes/btm.md)
  A time specification value that represents the backup time of the entry.
- [var ctm: timespec?](archiveheader/entryattributes/ctm.md)
  A time specification value that represents the creation time of the entry.
- [var flg: UInt32?](archiveheader/entryattributes/flg.md)
  An unsigned integer that represents the BSD flags of the entry.
- [var gid: UInt32?](archiveheader/entryattributes/gid.md)
  An unsigned integer that represents the group ID of the entry.
- [var mod: UInt32?](archiveheader/entryattributes/mod.md)
  An unsigned integer that represents the file modes of the entry.
- [var mtm: timespec?](archiveheader/entryattributes/mtm.md)
  A time specification value that represents the modification time of the entry.
- [var uid: UInt32?](archiveheader/entryattributes/uid.md)
  An unsigned integer that represents the user ID of the entry.

## See Also

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
- [ArchiveHeader.EntryMessageStatus](archiveheader/entrymessagestatus.md)
  Statuses that you return from an archive stream operation’s entry selection and status closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryattributes)*