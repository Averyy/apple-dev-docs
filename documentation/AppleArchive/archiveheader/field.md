# ArchiveHeader.Field

**Framework**: Apple Archive  
**Kind**: enum  
**Role**: Enumeration

An enumeration that describes the type, key, and value of a header field.

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
enum Field
```

## Topics

### Field Constants
- [case blob(key: ArchiveHeader.FieldKey, size: UInt64, offset: UInt64)](./field/blob%28key,size,offset%29.md)
  An enumeration that indicates the field is a data blob.
- [case flag(key: ArchiveHeader.FieldKey)](./field/flag%28key%29.md)
  An enumeration that indicates the field is a flag.
- [case hash(key: ArchiveHeader.FieldKey, hashFunction: ArchiveHash, value: ContiguousArray<UInt8>)](./field/hash%28key,hashfunction,value%29.md)
  An enumeration that indicates the field is a hash.
- [case string(key: ArchiveHeader.FieldKey, value: String)](./field/string%28key,value%29.md)
  An enumeration that indicates the field is a string.
- [case timespec(key: ArchiveHeader.FieldKey, value: timespec)](./field/timespec%28key,value%29.md)
  An enumeration that indicates the field is a time value.
- [case uint(key: ArchiveHeader.FieldKey, value: UInt64)](./field/uint%28key,value%29.md)
  An enumeration that indicates the field is an unsigned integer.
### Instance Properties
- [var key: ArchiveHeader.FieldKey](./field/key.md)
  The field key of this field.
- [var type: ArchiveHeader.FieldType](./field/type.md)
  The field type of this field.

## See Also

### Manipulating Fields
- [func field(forKey: ArchiveHeader.FieldKey) -> ArchiveHeader.Field?](./field%28forkey%29.md)
  Returns the field for a specified key.
- [ArchiveHeader.FieldKey](./fieldkey-swift.struct.md)
  A type that’s an alias for the field key structure.
- [var fieldType: ArchiveHeader._FieldTypes](./fieldtype-swift.property.md)
  The field types of the archive header.
- [ArchiveHeader.FieldType](./fieldtype-swift.struct.md)
  Constants that specify the field type of an archive header.
- [var fieldKey: ArchiveHeader._FieldKeys](./fieldkey-swift.property.md)
  The field keys of the archive header.
- [ArchiveHeader.FieldKeySet](./fieldkeyset.md)
  An object that represents a field key set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/field)*