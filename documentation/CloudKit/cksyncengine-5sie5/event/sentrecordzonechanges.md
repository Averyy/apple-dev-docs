# CKSyncEngine.Event.SentRecordZoneChanges

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about a sent batch of record zone changes.

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
- [CKSyncEngine.Event.SentDatabaseChanges](cksyncengine-5sie5/event/sentdatabasechanges.md)
  A type that provides information about a sent batch of database changes.
- [case sentRecordZoneChanges(CKSyncEngine.Event.SentRecordZoneChanges)](cksyncengine-5sie5/event/sentrecordzonechanges(_:).md)
  An event indicating a sent batch of record zone changes.
- [case didSendChanges(CKSyncEngine.Event.DidSendChanges)](cksyncengine-5sie5/event/didsendchanges(_:).md)
  An event that indicates a finished send operation.
- [CKSyncEngine.Event.DidSendChanges](cksyncengine-5sie5/event/didsendchanges.md)
  A type that provides information about a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentrecordzonechanges)*