# CKRecordZone.EncryptionScope

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CKRecordZoneEncryptionScope : NSInteger;
```

## Topics

### Enumeration Cases
- [CKRecordZone.EncryptionScope.perRecord](./encryptionscope-swift.enum/perrecord.md)
  Zone uses per-record encryption keys for any encrypted values on a record or share.
- [CKRecordZone.EncryptionScope.perZone](./encryptionscope-swift.enum/perzone.md)
  Zone uses per-zone encryption keys for encrypted values across all records and the zone-wide share, if present.
### Initializers
- [init?(rawValue: Int)](./encryptionscope-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/encryptionscope-swift.enum)*