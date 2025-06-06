# ArchiveHeader.FieldKey

**Framework**: Apple Archive  
**Kind**: struct

A type that’s an alias for the field key structure.

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
struct FieldKey
```

#### Overview

Apple Archive supports the following predefined keys:

## Topics

### Field Key Creation
- [init(String)](archiveheader/fieldkey-swift.struct/init(_:).md)
  Creates a new field key from the key you specify.
### Instance Properties
- [var description: String](archiveheader/fieldkey-swift.struct/description.md)
  A textual representation of this instance.
### Equatable Requirements
- [static func == (ArchiveHeader.FieldKey, ArchiveHeader.FieldKey) -> Bool](archiveheader/fieldkey-swift.struct/==(_:_:).md)
  Equatable protocol
### Hash Values
- [func hash(into: inout Hasher)](archiveheader/fieldkey-swift.struct/hash(into:).md)
  Hashable protocol

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [func field(forKey: ArchiveHeader.FieldKey) -> ArchiveHeader.Field?](archiveheader/field(forkey:).md)
  Returns the field for a specified key.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/fieldkey-swift.struct)*