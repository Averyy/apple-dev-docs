# CKDatabase.DatabaseChange.Deletion

**Framework**: CloudKit  
**Kind**: struct

A database change that represents the deletion of a record zone.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
struct Deletion
```

## Topics

### Identifying the Deleted Record Zone
- [var zoneID: CKRecordZone.ID](ckdatabase/databasechange/deletion/zoneid.md)
  The identifier of the deleted record zone.
- [var purged: Bool](ckdatabase/databasechange/deletion/purged.md)
  A Boolean value that indicates whether the user deleted the record zone when managing their iCloud storage.
### Instance Properties
- [var reason: CKDatabase.DatabaseChange.Deletion.Reason](ckdatabase/databasechange/deletion/reason-swift.property.md)
### Enumerations
- [CKDatabase.DatabaseChange.Deletion.Reason](ckdatabase/databasechange/deletion/reason-swift.enum.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/databasechange/deletion)*