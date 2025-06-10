# init(recordsToSave:recordIDsToDelete:atomicByZone:)

**Framework**: CloudKit  
**Kind**: init

Creates a batch of records to modify.

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
init(recordsToSave: [CKRecord] = [], recordIDsToDelete: [CKRecord.ID] = [], atomicByZone: Bool = false)
```

#### Discussion

> ❗ **Important**:  When using this initializer to create batches, consider the number of records you specify and their combined size. If you specify too many records, or their combined size is too large, the send operation may fail with an error of type [`CKError.Code.limitExceeded`](ckerror/code/limitexceeded.md).

## Parameters

- `recordsToSave`: The records to save.
- `recordIDsToDelete`: The identifiers of the records to delete.
- `atomicByZone`: A Boolean value that determines whether CloudKit modifies the specified records atomically by record zone.

## See Also

- [init?(pendingChanges: [CKSyncEngine.PendingRecordZoneChange], recordProvider: (CKRecord.ID) async -> CKRecord?) async](cksyncengine-5sie5/recordzonechangebatch/init(pendingchanges:recordprovider:).md)
  Creates a batch of records to modify using the provided record zone changes.
- [CKSyncEngine.PendingRecordZoneChange](cksyncengine-5sie5/pendingrecordzonechange.md)
  Describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/recordzonechangebatch/init(recordstosave:recordidstodelete:atomicbyzone:))*