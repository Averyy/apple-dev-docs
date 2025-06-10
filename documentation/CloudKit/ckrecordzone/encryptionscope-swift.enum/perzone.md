# CKRecordZone.EncryptionScope.perZone

**Framework**: CloudKit  
**Kind**: case

Zone uses per-zone encryption keys for encrypted values across all records and the zone-wide share, if present.

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
case perZone
```

#### Discussion

This is an optional optimization that can reduce the overall storage used by encryption keys in a zone. Note that:

- Record zones using per-zone encryption only support zone-wide sharing.
- Encryption scope can only be assigned at zone creation and cannot be changed for the lifetime of the zone.
- The server will not return zones using per-zone encryption to device OS versions older than the corresponding API availability version.
- An older OS trying to overwrite an existing zone using per-zone encryption due to a naming collision will result in a `.serverRejectedRequest` error.
- On device OS upgrade, your application is responsible for fetching database changes via `CKFetchDatabaseChangesOperation` with a nil sync token to ensure it has received all the zones available to it from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/encryptionscope-swift.enum/perzone)*