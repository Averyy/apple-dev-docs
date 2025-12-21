# CKRecordZone.EncryptionScope

**Framework**: CloudKit  
**Kind**: enum

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum EncryptionScope
```

## Topics

### Enumeration Cases
- [CKRecordZone.EncryptionScope.perRecord](ckrecordzone/encryptionscope-swift.enum/perrecord.md)
  Zone uses per-record encryption keys for any encrypted values on a record or share.
- [CKRecordZone.EncryptionScope.perZone](ckrecordzone/encryptionscope-swift.enum/perzone.md)
  Zone uses per-zone encryption keys for encrypted values across all records and the zone-wide share, if present.
### Initializers
- [init?(rawValue: Int)](ckrecordzone/encryptionscope-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/encryptionscope-swift.enum)*