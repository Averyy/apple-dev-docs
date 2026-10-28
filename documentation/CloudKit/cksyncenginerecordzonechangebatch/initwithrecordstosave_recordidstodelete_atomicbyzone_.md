# initWithRecordsToSave:recordIDsToDelete:atomicByZone:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a batch of records to modify.

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
- (instancetype) initWithRecordsToSave:(NSArray<CKRecord *> *) recordsToSave recordIDsToDelete:(NSArray<CKRecordID *> *) recordIDsToDelete atomicByZone:(BOOL) atomicByZone;
```

## Return Value

An initialized change batch.

## Discussion

> ❗ **Important**: When using this initializer to create batches, consider the number of records you specify and their combined size. If you specify too many records, or their combined size is too large, the send operation may fail with an error of type [`CKError.Code.limitExceeded`](../ckerror/code/limitexceeded.md).

## Parameters

- `recordsToSave`: The records to save.
- `recordIDsToDelete`: The identifiers of the records to delete.
- `atomicByZone`: A Boolean value that determines whether CloudKit modifies the specified records atomically by record zone.

## See Also

### Creating a batch
- [- initWithPendingChanges:recordProvider:](./initwithpendingchanges_recordprovider_.md)
  Creates a batch of records to modify using the provided record zone changes.
- [CKSyncEnginePendingRecordZoneChange](../cksyncenginependingrecordzonechange.md)
  An object that describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginerecordzonechangebatch/initwithrecordstosave:recordidstodelete:atomicbyzone:)*