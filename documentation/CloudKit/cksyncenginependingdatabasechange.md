# CKSyncEnginePendingDatabaseChange

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that describes an unsent database modification.

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
@interface CKSyncEnginePendingDatabaseChange : NSObject
```

## Topics

### Understanding the change
- [type](./cksyncenginependingdatabasechange/type.md)
  The type of database change.
- [enum CKSyncEnginePendingDatabaseChangeType](./cksyncenginependingdatabasechangetype.md)
  Describes the type of a pending database change.
- [zoneID](./cksyncenginependingdatabasechange/zoneid.md)
  The identifier of the record zone to change.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CKSyncEnginePendingZoneDelete](./cksyncenginependingzonedelete.md)
- [CKSyncEnginePendingZoneSave](./cksyncenginependingzonesave.md)

## See Also

### Modifying pending changes
- [- addPendingDatabaseChanges:](./cksyncenginestate/addpendingdatabasechanges_.md)
  Adds the specified database changes to the state.
- [- removePendingDatabaseChanges:](./cksyncenginestate/removependingdatabasechanges_.md)
  Removes the specified database changes from the state.
- [CKSyncEnginePendingZoneDelete](./cksyncenginependingzonedelete.md)
  An object that describes an unsent record zone deletion.
- [CKSyncEnginePendingZoneSave](./cksyncenginependingzonesave.md)
  An object that describes an unsent record zone modification.
- [- addPendingRecordZoneChanges:](./cksyncenginestate/addpendingrecordzonechanges_.md)
  Adds the specified record zone changes to the state.
- [- removePendingRecordZoneChanges:](./cksyncenginestate/removependingrecordzonechanges_.md)
  Removes the specified record zone changes from the state.
- [CKSyncEnginePendingRecordZoneChange](./cksyncenginependingrecordzonechange.md)
  An object that describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginependingdatabasechange)*