# ArchiveHeader.EntryXATBlob

**Framework**: Apple Archive  
**Kind**: class  
**Role**: Class

An object that describes the extended attributes of an archive entry.

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
class EntryXATBlob
```

## Topics

### Creating an Extended Attributes Blob
- [init()](./entryxatblob/init%28%29.md)
  Creates a new empty extended attribute blob.
- [init?(directory: FilePath, path: FilePath, flags: ArchiveFlags)](./entryxatblob/init%28directory,path,flags%29.md)
  Creates a new extended attribute blob from the specified directory and path.
- [init?(withAAEncodedData: UnsafeBufferPointer<UInt8>)](./entryxatblob/init%28withaaencodeddata%29.md)
  Creates a new archive header from encoded data.
### Applying an Extended Attributes Blob
- [func apply(directory: FilePath, path: FilePath, flags: ArchiveFlags) throws](./entryxatblob/apply%28directory,path,flags%29.md)
  Applies extended attributes to a filesystem object.
### Describing Extended Attributes
- [ArchiveHeader.EntryXATBlob.ExtendedAttribute](./entryxatblob/extendedattribute.md)
  A structure that describes the extended attributes of a filesystem.
### Collection Requirements
- [func append(ArchiveHeader.EntryXATBlob.ExtendedAttribute)](./entryxatblob/append%28_%29.md)
- [func remove(at: Int) -> ArchiveHeader.EntryXATBlob.ExtendedAttribute](./entryxatblob/remove%28at%29.md)
- [func removeAll()](./entryxatblob/removeall%28%29.md)
- [func withAAEncodedData<R>((UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R](./entryxatblob/withaaencodeddata%28_%29.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [MutableCollection](../../Swift/mutablecollection.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Manipulating Entries
- [ArchiveHeader.EntryAttributes](./entryattributes.md)
  An object that describes archive entry attributes.
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
- [ArchiveHeader.EntryMessageStatus](./entrymessagestatus.md)
  Statuses that you return from an archive stream operation’s entry selection and status closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/entryxatblob)*