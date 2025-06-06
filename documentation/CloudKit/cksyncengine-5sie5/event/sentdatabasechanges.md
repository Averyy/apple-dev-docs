# CKSyncEngine.Event.SentDatabaseChanges

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about a sent batch of database changes.

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
struct SentDatabaseChanges
```

## Topics

### Accessing successful changes
- [let deletedZoneIDs: [CKRecordZone.ID]](cksyncengine-5sie5/event/sentdatabasechanges/deletedzoneids.md)
  The unique identifiers of the deleted record zones.
- [let savedZones: [CKRecordZone]](cksyncengine-5sie5/event/sentdatabasechanges/savedzones.md)
  The modified record zones.
### Accessing failed changes
- [let failedZoneDeletes: [CKRecordZone.ID : CKError]](cksyncengine-5sie5/event/sentdatabasechanges/failedzonedeletes.md)
  The unique identifiers of the record zones CloudKit is unable to delete, and the reasons why.
- [let failedZoneSaves: [CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave]](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesaves.md)
  The record zones that CloudKit is unable to modify.
- [CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave](cksyncengine-5sie5/event/sentdatabasechanges/failedzonesave.md)
  A type that describes an unsuccessful attempt to modify a single record zone.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [case willSendChanges(CKSyncEngine.Event.WillSendChanges)](cksyncengine-5sie5/event/willsendchanges(_:).md)
  An event indicating an imminent send of local changes.
- [CKSyncEngine.Event.WillSendChanges](cksyncengine-5sie5/event/willsendchanges.md)
  A type that provides information about an imminent send of local changes.
- [case sentDatabaseChanges(CKSyncEngine.Event.SentDatabaseChanges)](cksyncengine-5sie5/event/sentdatabasechanges(_:).md)
  An event indicating a sent batch of database changes.
- [case sentRecordZoneChanges(CKSyncEngine.Event.SentRecordZoneChanges)](cksyncengine-5sie5/event/sentrecordzonechanges(_:).md)
  An event indicating a sent batch of record zone changes.
- [CKSyncEngine.Event.SentRecordZoneChanges](cksyncengine-5sie5/event/sentrecordzonechanges.md)
  A type that provides information about a sent batch of record zone changes.
- [case didSendChanges(CKSyncEngine.Event.DidSendChanges)](cksyncengine-5sie5/event/didsendchanges(_:).md)
  An event that indicates a finished send operation.
- [CKSyncEngine.Event.DidSendChanges](cksyncengine-5sie5/event/didsendchanges.md)
  A type that provides information about a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentdatabasechanges)*