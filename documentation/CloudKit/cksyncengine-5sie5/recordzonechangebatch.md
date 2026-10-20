# CKSyncEngine.RecordZoneChangeBatch

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that contains the record changes for a single send operation.

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
struct RecordZoneChangeBatch
```

## Topics

### Creating a batch
- [init?(pendingChanges: [CKSyncEngine.PendingRecordZoneChange], recordProvider: (CKRecord.ID) async -> CKRecord?) async](./recordzonechangebatch/init%28pendingchanges,recordprovider%29.md)
  Creates a batch of records to modify using the provided record zone changes.
- [CKSyncEngine.PendingRecordZoneChange](./pendingrecordzonechange.md)
  Describes an unsent record modification.
- [init(recordsToSave: [CKRecord], recordIDsToDelete: [CKRecord.ID], atomicByZone: Bool)](./recordzonechangebatch/init%28recordstosave,recordidstodelete,atomicbyzone%29.md)
  Creates a batch of records to modify.
### Managing atomicity
- [var atomicByZone: Bool](./recordzonechangebatch/atomicbyzone.md)
  A Boolean value that determines whether CloudKit modifies records atomically by record zone.
### Managing the records
- [var recordIDsToDelete: [CKRecord.ID]](./recordzonechangebatch/recordidstodelete.md)
  The record identifiers of the records to delete.
- [var recordsToSave: [CKRecord]](./recordzonechangebatch/recordstosave.md)
  The records to save.
### Debugging the batch
- [var description: String](./recordzonechangebatch/description.md)
  The textual description of the batch that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./recordzonechangebatch/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending changes
- [func nextRecordZoneChangeBatch(CKSyncEngine.SendChangesContext, syncEngine: CKSyncEngine) async -> CKSyncEngine.RecordZoneChangeBatch?](../cksyncenginedelegate-1q7g8/nextrecordzonechangebatch%28_,syncengine%29.md)
  Asks the delegate to provide the next set of record changes to send to the server.
- [CKSyncEngine.SendChangesContext](./sendchangescontext.md)
  The context of an attempt to send changes to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/recordzonechangebatch)*