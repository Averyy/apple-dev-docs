# CKSyncEngine.Event.SentRecordZoneChanges

**Framework**: CloudKit  
**Kind**: struct

The sync engine finished sending a batch of record zone changes to the server.

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
struct SentRecordZoneChanges
```

#### Overview

If a record save succeeded, you should encode the system fields of this record to use the next time you save. See [`encodeSystemFields(with:)`](ckrecord/encodesystemfields(with:).md).

If a record deletion succeeded, you should remove any local system fields for that record.

If the record change failed, try to resolve the issue causing the error and save the record again if necessary.

## Topics

### Accessing successful changes
- [let deletedRecordIDs: [CKRecord.ID]](cksyncengine-5sie5/event/sentrecordzonechanges/deletedrecordids.md)
  The unique identifiers of the deleted records.
- [let savedRecords: [CKRecord]](cksyncengine-5sie5/event/sentrecordzonechanges/savedrecords.md)
  The modified records.
### Accessing failed changes
- [let failedRecordDeletes: [CKRecord.ID : CKError]](cksyncengine-5sie5/event/sentrecordzonechanges/failedrecorddeletes.md)
  The unique identifiers of the records CloudKit is unable to delete, and the reasons why.
- [let failedRecordSaves: [CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave]](cksyncengine-5sie5/event/sentrecordzonechanges/failedrecordsaves.md)
  The records that CloudKit is unable to modify.
- [CKSyncEngine.Event.SentRecordZoneChanges.FailedRecordSave](cksyncengine-5sie5/event/sentrecordzonechanges/failedrecordsave.md)
  A type that describes an unsuccessful attempt to modify a single record.
### Debugging the event
- [var description: String](cksyncengine-5sie5/event/sentrecordzonechanges/description.md)
  A textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/event/sentrecordzonechanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case willSendChanges(CKSyncEngine.Event.WillSendChanges)](cksyncengine-5sie5/event/willsendchanges(_:).md)
  The sync engine is about to send changes to the server.
- [CKSyncEngine.Event.WillSendChanges](cksyncengine-5sie5/event/willsendchanges.md)
  A type that provides information about an imminent send of local changes.
- [case sentDatabaseChanges(CKSyncEngine.Event.SentDatabaseChanges)](cksyncengine-5sie5/event/sentdatabasechanges(_:).md)
  The sync engine sent a batch of database changes to the server.
- [CKSyncEngine.Event.SentDatabaseChanges](cksyncengine-5sie5/event/sentdatabasechanges.md)
  A type that provides information about a sent batch of database changes.
- [case sentRecordZoneChanges(CKSyncEngine.Event.SentRecordZoneChanges)](cksyncengine-5sie5/event/sentrecordzonechanges(_:).md)
  The sync engine sent a batch of record zone changes to the server.
- [case didSendChanges(CKSyncEngine.Event.DidSendChanges)](cksyncengine-5sie5/event/didsendchanges(_:).md)
  The sync engine finished sending changes to the server.
- [CKSyncEngine.Event.DidSendChanges](cksyncengine-5sie5/event/didsendchanges.md)
  A type that provides information about a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentrecordzonechanges)*