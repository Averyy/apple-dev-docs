# recordWithIDWasDeletedBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The block to execute when a record no longer exists.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) void (^recordWithIDWasDeletedBlock)(CKRecordID *recordID, CKRecordType recordType);
```

#### Discussion

The block returns no value and takes the following parameters:

- **`recordID`**: The deleted record’s ID.
- **`recordType`**: The deleted record’s type.

The operation executes this block once for each record the server deletes after the previous change token. Each time the block executes, it executes serially with respect to the other blocks of the operation. If there aren’t any record deletions, this block doesn’t execute.

Set this property before you execute the operation or submit it to a queue.

## See Also

### Processing the Zone Change Operation Results
- [var recordChangedBlock: ((CKRecord) -> Void)?](./recordchangedblock.md)
  The closure to execute with the contents of a changed record.
- [var recordZoneChangeTokensUpdatedBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?) -> Void)?](./recordzonechangetokensupdatedblock.md)
  The closure to execute when the change token updates.
- [var recordZoneFetchCompletionBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?, Bool, (any Error)?) -> Void)?](./recordzonefetchcompletionblock.md)
  The closure to execute when a record zone’s fetch finishes.
- [var fetchRecordZoneChangesCompletionBlock: (((any Error)?) -> Void)?](./fetchrecordzonechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordwithidwasdeletedblock-912xy)*