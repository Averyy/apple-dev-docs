# ArchiveHeader.Field.hash(key:hashFunction:value:)

**Framework**: Apple Archive  
**Kind**: case  
**Role**: Case

An enumeration that indicates the field is a hash.

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
case hash(key: ArchiveHeader.FieldKey, hashFunction: ArchiveHash, value: ContiguousArray<UInt8>)
```

## See Also

### Field Constants
- [case blob(key: ArchiveHeader.FieldKey, size: UInt64, offset: UInt64)](./blob%28key,size,offset%29.md)
  An enumeration that indicates the field is a data blob.
- [case flag(key: ArchiveHeader.FieldKey)](./flag%28key%29.md)
  An enumeration that indicates the field is a flag.
- [case string(key: ArchiveHeader.FieldKey, value: String)](./string%28key,value%29.md)
  An enumeration that indicates the field is a string.
- [case timespec(key: ArchiveHeader.FieldKey, value: timespec)](./timespec%28key,value%29.md)
  An enumeration that indicates the field is a time value.
- [case uint(key: ArchiveHeader.FieldKey, value: UInt64)](./uint%28key,value%29.md)
  An enumeration that indicates the field is an unsigned integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveheader/field/hash(key:hashfunction:value:))*