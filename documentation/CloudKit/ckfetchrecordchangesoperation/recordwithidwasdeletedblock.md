# recordWithIDWasDeletedBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The block to execute with the ID of a deleted record.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- iPadOS 8.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CKFetchRecordZoneChangesOperation)
- macOS 10.10+ - Deprecated in 10.12 (renamed: CKFetchRecordZoneChangesOperation)
- tvOS 9.0+ - Deprecated in 10.0 (renamed: CKFetchRecordZoneChangesOperation)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CKFetchRecordZoneChangesOperation)
- watchOS 3.0+ - Deprecated in 3.0 (renamed: CKFetchRecordZoneChangesOperation)

## Declaration

```swift
var recordWithIDWasDeletedBlock: ((CKRecord.ID) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^recordWithIDWasDeletedBlock)(CKRecordID *recordID);
```

## Discussion

The block returns no value and takes the following parameters:

- **`recordID`**: The ID of the deleted record.

The operation object executes this block once for each record the server deletes in the record zone after the previous fetch request. Each time the block executes, it executes serially with respect to the other progress blocks of the operation. If there aren’t any deleted records, this block doesn’t execute.

If you intend to use this block to process results, set it before executing the operation or submitting it to a queue.

## See Also

### Processing the Fetch Record Changes Results
- [var recordChangedBlock: ((CKRecord) -> Void)?](./recordchangedblock.md)
  The block to execute with the contents of a changed record.
- [var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, Data?, (any Error)?) -> Void)?](./fetchrecordchangescompletionblock.md)
  The block to execute when the system finishes processing all changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/recordwithidwasdeletedblock)*