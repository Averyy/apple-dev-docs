# ArchiveHeader.FieldType

**Framework**: Apple Archive  
**Kind**: struct

Constants that specify the field type of an archive header.

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
struct FieldType
```

## Topics

### Field Types
- [static let blob: ArchiveHeader.FieldType](archiveheader/fieldtype-swift.struct/blob.md)
  A constant that indicates the field is a data blob.
- [static let flag: ArchiveHeader.FieldType](archiveheader/fieldtype-swift.struct/flag.md)
  A constant that indicates the field is a flag.
- [static let hash: ArchiveHeader.FieldType](archiveheader/fieldtype-swift.struct/hash.md)
  A constant that indicates the field is a hash.
- [static let string: ArchiveHeader.FieldType](archiveheader/fieldtype-swift.struct/string.md)
  A constant that indicates the field is a string.
- [static let timespec: ArchiveHeader.FieldType](archiveheader/fieldtype-swift.struct/timespec.md)
  A constant that indicates the field is a time value.
- [static let uint: ArchiveHeader.FieldType](archiveheader/fieldtype-swift.struct/uint.md)
  A constant that indicates the field is an unsigned integer.
### Raw Values
- [init(rawValue: UInt32)](archiveheader/fieldtype-swift.struct/init(rawvalue:).md)
- [var rawValue: UInt32](archiveheader/fieldtype-swift.struct/rawvalue.md)
### Instance Properties
- [var description: String](archiveheader/fieldtype-swift.struct/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [func field(forKey: ArchiveHeader.FieldKey) -> ArchiveHeader.Field?](archiveheader/field(forkey:).md)
  Returns the field for a specified key.
- [ArchiveHeader.FieldKey](archiveheader/fieldkey-swift.struct.md)
  A type that’s an alias for the field key structure.
- [ArchiveHeader.Field](archiveheader/field.md)
  An enumeration that describes the type, key, and value of a header field.
- [var fieldType: ArchiveHeader._FieldTypes](archiveheader/fieldtype-swift.property.md)
  The field types of the archive header.
- [var fieldKey: ArchiveHeader._FieldKeys](archiveheader/fieldkey-swift.property.md)
  The field keys of the archive header.
- [ArchiveHeader.FieldKeySet](archiveheader/fieldkeyset.md)
  An object that represents a field key set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/fieldtype-swift.struct)*