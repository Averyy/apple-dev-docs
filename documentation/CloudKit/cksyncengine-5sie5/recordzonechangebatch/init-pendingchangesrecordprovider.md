# init(pendingChanges:recordProvider:)

**Framework**: CloudKit  
**Kind**: init

Creates a batch of records to modify using the provided record zone changes.

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
init?(pendingChanges: [CKSyncEngine.PendingRecordZoneChange], recordProvider: (CKRecord.ID) async -> CKRecord?) async
```

#### Return Value

The batch of records to modify, or `nil` if there are no pending changes.

#### Discussion

This method iterates over `pendingChanges` and adds the necessary information to the new batch, until there are no more changes or the size of the batch reaches the maximum limit. If the type of change is a record save, the method asks the specified `recordProvider` closure for that record. If the closure returns `nil`, the method skips that change.

## Parameters

- `pendingChanges`: The record zone changes to process.
- `recordProvider`: A closure that returns the record for the specified record identifier.

## See Also

- [CKSyncEngine.PendingRecordZoneChange](cksyncengine-5sie5/pendingrecordzonechange.md)
  Describes an unsent record modification.
- [init(recordsToSave: [CKRecord], recordIDsToDelete: [CKRecord.ID], atomicByZone: Bool)](cksyncengine-5sie5/recordzonechangebatch/init(recordstosave:recordidstodelete:atomicbyzone:).md)
  Creates a batch of records to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/recordzonechangebatch/init(pendingchanges:recordprovider:))*