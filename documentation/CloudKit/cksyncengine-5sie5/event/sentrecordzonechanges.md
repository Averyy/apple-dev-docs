# CKSyncEngine.Event.SentRecordZoneChanges

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

The sync engine finished sending a batch of record zone changes to the server.

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
struct SentRecordZoneChanges
```

#### Overview

If a record save succeeded, you should encode the system fields of this record to use the next time you save. See [`encodeSystemFields(with:)`](../../ckrecord/encodesystemfields%28with%29.md).

If a record deletion succeeded, you should remove any local system fields for that record.

If the record change failed, try to resolve the issue causing the error and save the record again if necessary.

## Topics

### Accessing successful changes
- [let deletedRecordIDs: [CKRecord.ID]](./sentrecordzonechanges/deletedrecordids.md)
  The unique identifiers of the deleted records.
- [let savedRecords: [CKRecord]](./sentrecordzonechanges/savedrecords.md)
  The modified records.
### Accessing failed changes
- [let failedRecordDeletes: [CKRecord.ID : CKError]](./sentrecordzonechanges/failedrecorddeletes.md)
  The unique identifiers of the records CloudKit is unable to delete, and the reasons why.
- [let failedRecordSaves: [CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave]](./sentrecordzonechanges/failedrecordsaves.md)
  The records that CloudKit is unable to modify.
- [CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave](./sentrecordzonechanges/failedrecordsave.md)
  A type that describes an unsuccessful attempt to modify a single record.
### Debugging the event
- [var description: String](./sentrecordzonechanges/description.md)
  A textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./sentrecordzonechanges/customstringconvertible-implementations.md)

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
- [CKSyncEngine.Event.SentDatabaseChanges](./sentdatabasechanges.md)
  A type that provides information about a sent batch of database changes.
- [case sentRecordZoneChanges(CKSyncEngine.Event.SentRecordZoneChanges)](./sentrecordzonechanges%28_%29.md)
  The sync engine sent a batch of record zone changes to the server.
- [case didSendChanges(CKSyncEngine.Event.DidSendChanges)](./didsendchanges%28_%29.md)
  The sync engine finished sending changes to the server.
- [CKSyncEngine.Event.DidSendChanges](./didsendchanges.md)
  A type that provides information about a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentrecordzonechanges)*