# CKSyncEngine.Event.SentDatabaseChanges

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that provides information about a sent batch of database changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
struct SentDatabaseChanges
```

## Topics

### Accessing successful changes
- [let deletedZoneIDs: [CKRecordZone.ID]](./sentdatabasechanges/deletedzoneids.md)
  The unique identifiers of the deleted record zones.
- [let savedZones: [CKRecordZone]](./sentdatabasechanges/savedzones.md)
  The modified record zones.
### Accessing failed changes
- [let failedZoneDeletes: [CKRecordZone.ID : CKError]](./sentdatabasechanges/failedzonedeletes.md)
  The unique identifiers of the record zones CloudKit is unable to delete, and the reasons why.
- [let failedZoneSaves: [CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave]](./sentdatabasechanges/failedzonesaves.md)
  The record zones that CloudKit is unable to modify.
- [CKSyncEngine.Event.SentDatabaseChanges.FailedZoneSave](./sentdatabasechanges/failedzonesave.md)
  A type that describes an unsuccessful attempt to modify a single record zone.
### Debugging the event
- [var description: String](./sentdatabasechanges/description.md)
  A textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./sentdatabasechanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Pending local changes
- [case willSendChanges(CKSyncEngine.Event.WillSendChanges)](./willsendchanges%28_%29.md)
  The sync engine is about to send changes to the server.
- [CKSyncEngine.Event.WillSendChanges](./willsendchanges.md)
  A type that provides information about an imminent send of local changes.
- [case sentDatabaseChanges(CKSyncEngine.Event.SentDatabaseChanges)](./sentdatabasechanges%28_%29.md)
  The sync engine sent a batch of database changes to the server.
- [case sentRecordZoneChanges(CKSyncEngine.Event.SentRecordZoneChanges)](./sentrecordzonechanges%28_%29.md)
  The sync engine sent a batch of record zone changes to the server.
- [CKSyncEngine.Event.SentRecordZoneChanges](./sentrecordzonechanges.md)
  The sync engine finished sending a batch of record zone changes to the server.
- [case didSendChanges(CKSyncEngine.Event.DidSendChanges)](./didsendchanges%28_%29.md)
  The sync engine finished sending changes to the server.
- [CKSyncEngine.Event.DidSendChanges](./didsendchanges.md)
  A type that provides information about a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentdatabasechanges)*