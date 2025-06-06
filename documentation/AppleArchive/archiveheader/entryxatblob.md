# ArchiveHeader.EntryXATBlob

**Framework**: Apple Archive  
**Kind**: class

An object that describes the extended attributes of an archive entry.

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
class EntryXATBlob
```

## Topics

### Creating an Extended Attributes Blob
- [init()](archiveheader/entryxatblob/init.md)
  Creates a new empty extended attribute blob.
- [init?(directory: FilePath, path: FilePath, flags: ArchiveFlags)](archiveheader/entryxatblob/init(directory:path:flags:).md)
  Creates a new extended attribute blob from the specified directory and path.
- [init?(withAAEncodedData: UnsafeBufferPointer<UInt8>)](archiveheader/entryxatblob/init(withaaencodeddata:).md)
  Creates a new archive header from encoded data.
### Applying an Extended Attributes Blob
- [func apply(directory: FilePath, path: FilePath, flags: ArchiveFlags) throws](archiveheader/entryxatblob/apply(directory:path:flags:).md)
  Applies extended attributes to a filesystem object.
### Describing Extended Attributes
- [ArchiveHeader.EntryXATBlob.ExtendedAttribute](archiveheader/entryxatblob/extendedattribute.md)
  A structure that describes the extended attributes of a filesystem.
### Collection Requirements
- [func append(ArchiveHeader.EntryXATBlob.ExtendedAttribute)](archiveheader/entryxatblob/append(_:).md)
- [func remove(at: Int) -> ArchiveHeader.EntryXATBlob.ExtendedAttribute](archiveheader/entryxatblob/remove(at:).md)
- [func removeAll()](archiveheader/entryxatblob/removeall.md)
- [func withAAEncodedData<R>((UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R](archiveheader/entryxatblob/withaaencodeddata(_:).md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [ArchiveHeader.EntryAttributes](archiveheader/entryattributes.md)
  An object that describes archive entry attributes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryxatblob)*