# ArchiveHeader.Field.flag(key:)

**Framework**: Apple Archive  
**Kind**: case

An enumeration that indicates the field is a flag.

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
case flag(key: ArchiveHeader.FieldKey)
```

## See Also

- [case blob(key: ArchiveHeader.FieldKey, size: UInt64, offset: UInt64)](archiveheader/field/blob(key:size:offset:).md)
  An enumeration that indicates the field is a data blob.
- [case hash(key: ArchiveHeader.FieldKey, hashFunction: ArchiveHash, value: ContiguousArray<UInt8>)](archiveheader/field/hash(key:hashfunction:value:).md)
  An enumeration that indicates the field is a hash.
- [case string(key: ArchiveHeader.FieldKey, value: String)](archiveheader/field/string(key:value:).md)
  An enumeration that indicates the field is a string.
- [case timespec(key: ArchiveHeader.FieldKey, value: timespec)](archiveheader/field/timespec(key:value:).md)
  An enumeration that indicates the field is a time value.
- [case uint(key: ArchiveHeader.FieldKey, value: UInt64)](archiveheader/field/uint(key:value:).md)
  An enumeration that indicates the field is an unsigned integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/field/flag(key:))*