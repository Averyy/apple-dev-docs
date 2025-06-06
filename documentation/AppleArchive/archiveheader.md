# ArchiveHeader

**Framework**: Apple Archive  
**Kind**: class

An AppleArchive entry header.

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
class ArchiveHeader
```

## Topics

### Creating an Archive Header
- [init()](archiveheader/init.md)
  Creates a new empty archive header.
- [init?(keySet: ArchiveHeader.FieldKeySet, directory: FilePath, path: FilePath, flags: ArchiveFlags)](archiveheader/init(keyset:directory:path:flags:).md)
  Creates a new archive header with fields derived from the filesystem object, at the specified directory and path.
- [init?(withAAEncodedData: UnsafeBufferPointer<UInt8>)](archiveheader/init(withaaencodeddata:).md)
  Creates a new archive header from encoded data.
- [init(copying: ArchiveHeader)](archiveheader/init(copying:).md)
  Creates a copy of an archive header.
### Manipulating Fields
- [func field(forKey: ArchiveHeader.FieldKey) -> ArchiveHeader.Field?](archiveheader/field(forkey:).md)
  Returns the field for a specified key.
- [ArchiveHeader.FieldKey](archiveheader/fieldkey-swift.struct.md)
  A type that’s an alias for the field key structure.
- [ArchiveHeader.Field](archiveheader/field.md)
  An enumeration that describes the type, key, and value of a header field.
- [var fieldType: ArchiveHeader._FieldTypes](archiveheader/fieldtype-swift.property.md)
  The field types of the archive header.
- [ArchiveHeader.FieldType](archiveheader/fieldtype-swift.struct.md)
  Constants that specify the field type of an archive header.
- [var fieldKey: ArchiveHeader._FieldKeys](archiveheader/fieldkey-swift.property.md)
  The field keys of the archive header.
- [ArchiveHeader.FieldKeySet](archiveheader/fieldkeyset.md)
  An object that represents a field key set.
### Manipulating Entries
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
- [ArchiveHeader.EntryMessageStatus](archiveheader/entrymessagestatus.md)
  Statuses that you return from an archive stream operation’s entry selection and status closure.
### Accessing File Paths
- [var entryPath: FilePath?](archiveheader/entrypath.md)
  The entry from the path field, or nil if missing or invalid.
### Accessing AppleArchive Encoded Data
- [func withAAEncodedData<R>((UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R](archiveheader/withaaencodeddata(_:).md)
  Executes a closure with encoded data.
### Collection Requirements
- [func append(ArchiveHeader.Field)](archiveheader/append(_:).md)
- [func remove(at: Int) -> ArchiveHeader.Field](archiveheader/remove(at:).md)
- [func removeAll()](archiveheader/removeall.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader)*