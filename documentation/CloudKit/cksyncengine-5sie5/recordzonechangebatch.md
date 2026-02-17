# CKSyncEngine.RecordZoneChangeBatch

**Framework**: CloudKit  
**Kind**: struct

A type that contains the record changes for a single send operation.

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
struct RecordZoneChangeBatch
```

## Topics

### Creating a batch
- [init?(pendingChanges: [CKSyncEngine.PendingRecordZoneChange], recordProvider: (CKRecord.ID) async -> CKRecord?) async](cksyncengine-5sie5/recordzonechangebatch/init(pendingchanges:recordprovider:).md)
  Creates a batch of records to modify using the provided record zone changes.
- [CKSyncEngine.PendingRecordZoneChange](cksyncengine-5sie5/pendingrecordzonechange.md)
  Describes an unsent record modification.
- [init(recordsToSave: [CKRecord], recordIDsToDelete: [CKRecord.ID], atomicByZone: Bool)](cksyncengine-5sie5/recordzonechangebatch/init(recordstosave:recordidstodelete:atomicbyzone:).md)
  Creates a batch of records to modify.
### Managing atomicity
- [var atomicByZone: Bool](cksyncengine-5sie5/recordzonechangebatch/atomicbyzone.md)
  A Boolean value that determines whether CloudKit modifies records atomically by record zone.
### Managing the records
- [var recordIDsToDelete: [CKRecord.ID]](cksyncengine-5sie5/recordzonechangebatch/recordidstodelete.md)
  The record identifiers of the records to delete.
- [var recordsToSave: [CKRecord]](cksyncengine-5sie5/recordzonechangebatch/recordstosave.md)
  The records to save.
### Debugging the batch
- [var description: String](cksyncengine-5sie5/recordzonechangebatch/description.md)
  The textual description of the batch that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/recordzonechangebatch/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func nextRecordZoneChangeBatch(CKSyncEngine.SendChangesContext, syncEngine: CKSyncEngine) async -> CKSyncEngine.RecordZoneChangeBatch?](cksyncenginedelegate-1q7g8/nextrecordzonechangebatch(_:syncengine:).md)
  Asks the delegate to provide the next set of record changes to send to the server.
- [CKSyncEngine.SendChangesContext](cksyncengine-5sie5/sendchangescontext.md)
  The context of an attempt to send changes to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/recordzonechangebatch)*