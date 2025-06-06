# ArchiveHeader.FieldKeySet

**Framework**: Apple Archive  
**Kind**: class

An object that represents a field key set.

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
final class FieldKeySet
```

## Topics

### Creating a Field Key Set
- [init()](archiveheader/fieldkeyset/init.md)
  Creates a new empty field key set.
- [init?(String)](archiveheader/fieldkeyset/init(_:).md)
  Creates a new field key set from the specified comma-separated string of three-letter keys.
- [init(copying: ArchiveHeader.FieldKeySet)](archiveheader/fieldkeyset/init(copying:).md)
  Creates a copy of the specified field key set.
### Specifying Default Field Key Sets
- [static var defaultForArchive: ArchiveHeader.FieldKeySet](archiveheader/fieldkeyset/defaultforarchive.md)
  A constant that contains the default key set for an archive.
- [static var defaultForManifest: ArchiveHeader.FieldKeySet](archiveheader/fieldkeyset/defaultformanifest.md)
  A constant that contains the default key set for a manifest.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/fieldkeyset)*