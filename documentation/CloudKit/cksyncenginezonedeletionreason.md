# CKSyncEngineZoneDeletionReason

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CKSyncEngineZoneDeletionReason : NSInteger;
```

## Topics

### Deletion reasons
- [CKSyncEngineZoneDeletionReason.deleted](./cksyncenginezonedeletionreason/deleted.md)
  Your app deleted the record zone.
- [CKSyncEngineZoneDeletionReason.encryptedDataReset](./cksyncenginezonedeletionreason/encrypteddatareset.md)
  The owner of the iCloud account reset their encrypted data.
- [CKSyncEngineZoneDeletionReason.purged](./cksyncenginezonedeletionreason/purged.md)
  The owner of the iCloud account purged your app’s data using the Settings app.
### Initializers
- [init?(rawValue: Int)](./cksyncenginezonedeletionreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing changes
- [let deletions: [CKDatabase.DatabaseChange.Deletion]](./cksyncengine-5sie5/event/fetcheddatabasechanges/deletions.md)
  The fetched record zone deletions.
- [let modifications: [CKDatabase.DatabaseChange.Modification]](./cksyncengine-5sie5/event/fetcheddatabasechanges/modifications.md)
  The fetched record zone modifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginezonedeletionreason)*