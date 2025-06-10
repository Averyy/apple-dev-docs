# encryptionScope

**Framework**: CloudKit  
**Kind**: property

The encryption scope determines the granularity at which encryption keys are stored within the zone.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var encryptionScope: CKRecordZone.EncryptionScope { get set }
```

#### Discussion

Zone encryption scope defaults to `CKRecordZoneEncryptionScopePerRecord` and can only be modified before zone creation. Attempting to change the encryption scope of an existing zone is invalid and will result in an error.

Zones using `CKRecordZoneEncryptionScopePerZone` can only use zone-wide sharing and are not compatible with older device OS versions. Refer to `CKRecordZoneEncryptionScope` for more info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/encryptionscope-swift.property)*