# CKSyncEngineSentRecordZoneChangesEvent

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

The sync engine finished sending a batch of record zone changes to the server.

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
@interface CKSyncEngineSentRecordZoneChangesEvent : CKSyncEngineEvent
```

## Overview

If a record save succeeded, you should encode the system fields of this record to use the next time you save. See [`encodeSystemFields(with:)`](./ckrecord/encodesystemfields%28with%29.md).

If a record deletion succeeded, you should remove any local system fields for that record.

If the record change failed, try to resolve the issue causing the error and save the record again if necessary.

## Topics

### Accessing successful changes
- [deletedRecordIDs](./cksyncenginesentrecordzonechangesevent/deletedrecordids.md)
  The unique identifiers of the deleted records.
- [savedRecords](./cksyncenginesentrecordzonechangesevent/savedrecords.md)
  The modified records.
### Accessing failed changes
- [failedRecordDeletes](./cksyncenginesentrecordzonechangesevent/failedrecorddeletes.md)
  The unique identifiers of the records CloudKit is unable to delete, and the reasons why.
- [failedRecordSaves](./cksyncenginesentrecordzonechangesevent/failedrecordsaves.md)
  The records that CloudKit is unable to modify.
- [CKSyncEngineFailedRecordSave](./cksyncenginefailedrecordsave.md)
  A type that describes an unsuccessful attempt to modify an individual record.

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
- [CKSyncEngineSentDatabaseChangesEvent](./cksyncenginesentdatabasechangesevent.md)
  An object that provides information about a sent batch of database changes.
- [sentRecordZoneChangesEvent](./cksyncengineevent/sentrecordzonechangesevent.md)
  The event downcast to the subclass that represents a sent batch of record zone changes.
- [didSendChangesEvent](./cksyncengineevent/didsendchangesevent.md)
  The event downcast to the subclass that represents a completed send operation.
- [CKSyncEngineDidSendChangesEvent](./cksyncenginedidsendchangesevent.md)
  An object that provides information about a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesentrecordzonechangesevent)*