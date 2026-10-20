# ArchiveHeader.FieldKeySet

**Framework**: Apple Archive  
**Kind**: class  
**Role**: Class

An object that represents a field key set.

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
final class FieldKeySet
```

## Topics

### Creating a Field Key Set
- [init()](./fieldkeyset/init%28%29.md)
  Creates a new empty field key set.
- [init?(String)](./fieldkeyset/init%28_%29.md)
  Creates a new field key set from the specified comma-separated string of three-letter keys.
- [init(copying: ArchiveHeader.FieldKeySet)](./fieldkeyset/init%28copying%29.md)
  Creates a copy of the specified field key set.
### Specifying Default Field Key Sets
- [static var defaultForArchive: ArchiveHeader.FieldKeySet](./fieldkeyset/defaultforarchive.md)
  A constant that contains the default key set for an archive.
- [static var defaultForManifest: ArchiveHeader.FieldKeySet](./fieldkeyset/defaultformanifest.md)
  A constant that contains the default key set for a manifest.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sequence](../../Swift/sequence.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Manipulating Fields
- [func field(forKey: ArchiveHeader.FieldKey) -> ArchiveHeader.Field?](./field%28forkey%29.md)
  Returns the field for a specified key.
- [ArchiveHeader.FieldKey](./fieldkey-swift.struct.md)
  A type that’s an alias for the field key structure.
- [ArchiveHeader.Field](./field.md)
  An enumeration that describes the type, key, and value of a header field.
- [var fieldType: ArchiveHeader._FieldTypes](./fieldtype-swift.property.md)
  The field types of the archive header.
- [ArchiveHeader.FieldType](./fieldtype-swift.struct.md)
  Constants that specify the field type of an archive header.
- [var fieldKey: ArchiveHeader._FieldKeys](./fieldkey-swift.property.md)
  The field keys of the archive header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/fieldkeyset)*