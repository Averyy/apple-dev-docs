# ArchiveHeader.Field

**Framework**: Apple Archive  
**Kind**: enum

An enumeration that describes the type, key, and value of a header field.

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
enum Field
```

## Topics

### Field Constants
- [case blob(key: ArchiveHeader.FieldKey, size: UInt64, offset: UInt64)](archiveheader/field/blob(key:size:offset:).md)
  An enumeration that indicates the field is a data blob.
- [case flag(key: ArchiveHeader.FieldKey)](archiveheader/field/flag(key:).md)
  An enumeration that indicates the field is a flag.
- [case hash(key: ArchiveHeader.FieldKey, hashFunction: ArchiveHash, value: ContiguousArray<UInt8>)](archiveheader/field/hash(key:hashfunction:value:).md)
  An enumeration that indicates the field is a hash.
- [case string(key: ArchiveHeader.FieldKey, value: String)](archiveheader/field/string(key:value:).md)
  An enumeration that indicates the field is a string.
- [case timespec(key: ArchiveHeader.FieldKey, value: timespec)](archiveheader/field/timespec(key:value:).md)
  An enumeration that indicates the field is a time value.
- [case uint(key: ArchiveHeader.FieldKey, value: UInt64)](archiveheader/field/uint(key:value:).md)
  An enumeration that indicates the field is an unsigned integer.
### Instance Properties
- [var key: ArchiveHeader.FieldKey](archiveheader/field/key.md)
  The field key of this field.
- [var type: ArchiveHeader.FieldType](archiveheader/field/type.md)
  The field type of this field.

## See Also

- [func field(forKey: ArchiveHeader.FieldKey) -> ArchiveHeader.Field?](archiveheader/field(forkey:).md)
  Returns the field for a specified key.
- [ArchiveHeader.FieldKey](archiveheader/fieldkey-swift.struct.md)
  A type that’s an alias for the field key structure.
- [var fieldType: ArchiveHeader._FieldTypes](archiveheader/fieldtype-swift.property.md)
  The field types of the archive header.
- [ArchiveHeader.FieldType](archiveheader/fieldtype-swift.struct.md)
  Constants that specify the field type of an archive header.
- [var fieldKey: ArchiveHeader._FieldKeys](archiveheader/fieldkey-swift.property.md)
  The field keys of the archive header.
- [ArchiveHeader.FieldKeySet](archiveheader/fieldkeyset.md)
  An object that represents a field key set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/field)*