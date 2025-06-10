# CKSyncEngineZoneDeletionReason.purged

**Framework**: CloudKit  
**Kind**: case

The owner of the iCloud account purged your app’s data using the Settings app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case purged
```

#### Discussion

> ❗ **Important**:  Upon receipt of deletions with this reason, you must delete any locally cached data and not resend it to iCloud.

## See Also

- [CKSyncEngineZoneDeletionReason.deleted](cksyncenginezonedeletionreason/deleted.md)
  Your app deleted the record zone.
- [CKSyncEngineZoneDeletionReason.encryptedDataReset](cksyncenginezonedeletionreason/encrypteddatareset.md)
  The owner of the iCloud account reset their encrypted data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginezonedeletionreason/purged)*