# CKSyncEngineZoneDeletionReason

**Framework**: CloudKit  
**Kind**: enum

Describes the reason for a record zone deletion.

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
enum CKSyncEngineZoneDeletionReason
```

## Topics

### Deletion reasons
- [CKSyncEngineZoneDeletionReason.deleted](cksyncenginezonedeletionreason/deleted.md)
  Your app deleted the record zone.
- [CKSyncEngineZoneDeletionReason.encryptedDataReset](cksyncenginezonedeletionreason/encrypteddatareset.md)
  The owner of the iCloud account reset their encrypted data.
- [CKSyncEngineZoneDeletionReason.purged](cksyncenginezonedeletionreason/purged.md)
  The owner of the iCloud account purged your app’s data using the Settings app.
### Initializers
- [init?(rawValue: Int)](cksyncenginezonedeletionreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let deletions: [CKDatabase.DatabaseChange.Deletion]](cksyncengine-5sie5/event/fetcheddatabasechanges/deletions.md)
  The fetched record deletions.
- [let modifications: [CKDatabase.DatabaseChange.Modification]](cksyncengine-5sie5/event/fetcheddatabasechanges/modifications.md)
  The fetched record modifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginezonedeletionreason)*