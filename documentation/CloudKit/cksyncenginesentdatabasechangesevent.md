# CKSyncEngineSentDatabaseChangesEvent

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that provides information about a sent batch of database changes.

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
@interface CKSyncEngineSentDatabaseChangesEvent : CKSyncEngineEvent
```

## Topics

### Accessing successful changes
- [deletedZoneIDs](./cksyncenginesentdatabasechangesevent/deletedzoneids.md)
  The unique identifiers of the deleted record zones.
- [savedZones](./cksyncenginesentdatabasechangesevent/savedzones.md)
  The modified record zones.
### Accessing failed changes
- [failedZoneDeletes](./cksyncenginesentdatabasechangesevent/failedzonedeletes.md)
  The unique identifiers of the record zones CloudKit is unable to delete, and the reasons why.
- [failedZoneSaves](./cksyncenginesentdatabasechangesevent/failedzonesaves.md)
  The record zones that CloudKit is unable to modify.
- [CKSyncEngineFailedZoneSave](./cksyncenginefailedzonesave.md)
  An object that describes an unsuccessful attempt to modify a single record zone.

## Relationships

### Inherits From
- [CKSyncEngineEvent](./cksyncengineevent.md)

## See Also

### Accessing send events
- [willSendChangesEvent](./cksyncengineevent/willsendchangesevent.md)
  The event downcast to the subclass that represents an imminent send operation.
- [CKSyncEngineWillSendChangesEvent](./cksyncenginewillsendchangesevent.md)
  An object that provides information about an imminent send of local changes.
- [sentDatabaseChangesEvent](./cksyncengineevent/sentdatabasechangesevent.md)
  The event downcast to the subclass that represents a sent batch of database changes.
- [sentRecordZoneChangesEvent](./cksyncengineevent/sentrecordzonechangesevent.md)
  The event downcast to the subclass that represents a sent batch of record zone changes.
- [CKSyncEngineSentRecordZoneChangesEvent](./cksyncenginesentrecordzonechangesevent.md)
  The sync engine finished sending a batch of record zone changes to the server.
- [didSendChangesEvent](./cksyncengineevent/didsendchangesevent.md)
  The event downcast to the subclass that represents a completed send operation.
- [CKSyncEngineDidSendChangesEvent](./cksyncenginedidsendchangesevent.md)
  An object that provides information about a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesentdatabasechangesevent)*