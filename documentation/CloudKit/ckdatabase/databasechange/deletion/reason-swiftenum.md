# CKDatabase.DatabaseChange.Deletion.Reason

**Framework**: CloudKit  
**Kind**: enum

Constants that represent why a record zone was deleted.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
enum Reason
```

## Topics

### Enumeration Cases
- [CKDatabase.DatabaseChange.Deletion.Reason.deleted](ckdatabase/databasechange/deletion/reason-swift.enum/deleted.md)
  Your app deleted the record zone.
- [CKDatabase.DatabaseChange.Deletion.Reason.encryptedDataReset](ckdatabase/databasechange/deletion/reason-swift.enum/encrypteddatareset.md)
  The user chose to reset all encrypted data for their account.
- [CKDatabase.DatabaseChange.Deletion.Reason.purged](ckdatabase/databasechange/deletion/reason-swift.enum/purged.md)
  A deletion from the user via the iCloud storage UI.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/databasechange/deletion/reason-swift.enum)*