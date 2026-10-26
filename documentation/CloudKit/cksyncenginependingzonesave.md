# CKSyncEnginePendingZoneSave

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that describes an unsent record zone modification.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface CKSyncEnginePendingZoneSave : CKSyncEnginePendingDatabaseChange
```

## Topics

### Creating a pending zone save
- [- initWithZone:](./cksyncenginependingzonesave/initwithzone_.md)
  Creates a pending zone save for the specified record zone.
### Identifying the record zone
- [zone](./cksyncenginependingzonesave/zone.md)
  The record zone to save.

## Relationships

### Inherits From
- [CKSyncEnginePendingDatabaseChange](./cksyncenginependingdatabasechange.md)

## See Also

### Modifying pending changes
- [- addPendingDatabaseChanges:](./cksyncenginestate/addpendingdatabasechanges_.md)
  Adds the specified database changes to the state.
- [- removePendingDatabaseChanges:](./cksyncenginestate/removependingdatabasechanges_.md)
  Removes the specified database changes from the state.
- [CKSyncEnginePendingZoneDelete](./cksyncenginependingzonedelete.md)
  An object that describes an unsent record zone deletion.
- [CKSyncEnginePendingDatabaseChange](./cksyncenginependingdatabasechange.md)
  An object that describes an unsent database modification.
- [- addPendingRecordZoneChanges:](./cksyncenginestate/addpendingrecordzonechanges_.md)
  Adds the specified record zone changes to the state.
- [- removePendingRecordZoneChanges:](./cksyncenginestate/removependingrecordzonechanges_.md)
  Removes the specified record zone changes from the state.
- [CKSyncEnginePendingRecordZoneChange](./cksyncenginependingrecordzonechange.md)
  An object that describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginependingzonesave)*