# ArchiveHeader.FieldType

**Framework**: Apple Archive  
**Kind**: struct  
**Role**: Structure

Constants that specify the field type of an archive header.

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
struct FieldType
```

## Topics

### Field Types
- [static let blob: ArchiveHeader.FieldType](./fieldtype-swift.struct/blob.md)
  A constant that indicates the field is a data blob.
- [static let flag: ArchiveHeader.FieldType](./fieldtype-swift.struct/flag.md)
  A constant that indicates the field is a flag.
- [static let hash: ArchiveHeader.FieldType](./fieldtype-swift.struct/hash.md)
  A constant that indicates the field is a hash.
- [static let string: ArchiveHeader.FieldType](./fieldtype-swift.struct/string.md)
  A constant that indicates the field is a string.
- [static let timespec: ArchiveHeader.FieldType](./fieldtype-swift.struct/timespec.md)
  A constant that indicates the field is a time value.
- [static let uint: ArchiveHeader.FieldType](./fieldtype-swift.struct/uint.md)
  A constant that indicates the field is an unsigned integer.
### Raw Values
- [init(rawValue: UInt32)](./fieldtype-swift.struct/init%28rawvalue%29.md)
- [var rawValue: UInt32](./fieldtype-swift.struct/rawvalue.md)
### Instance Properties
- [var description: String](./fieldtype-swift.struct/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

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
- [var fieldKey: ArchiveHeader._FieldKeys](./fieldkey-swift.property.md)
  The field keys of the archive header.
- [ArchiveHeader.FieldKeySet](./fieldkeyset.md)
  An object that represents a field key set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/fieldtype-swift.struct)*