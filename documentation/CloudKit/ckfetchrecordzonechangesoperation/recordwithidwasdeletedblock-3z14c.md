# recordWithIDWasDeletedBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when a record no longer exists.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
var recordWithIDWasDeletedBlock: ((CKRecord.ID, CKRecord.RecordType) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- The deleted record’s ID.
- The deleted record’s type.

The operation executes this closure once for each record the server deletes after the previous change token. Each time the closure executes, it executes serially with respect to the other closures of the operation. If there aren’t any record deletions, this closure doesn’t execute.

Set this property before you execute the operation or submit it to a queue.

## See Also

- [var recordChangedBlock: ((CKRecord) -> Void)?](ckfetchrecordzonechangesoperation/recordchangedblock.md)
  The closure to execute with the contents of a changed record.
- [var recordZoneChangeTokensUpdatedBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonechangetokensupdatedblock.md)
  The closure to execute when the change token updates.
- [var recordZoneFetchCompletionBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?, Bool, (any Error)?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonefetchcompletionblock.md)
  The closure to execute when a record zone’s fetch finishes.
- [var fetchRecordZoneChangesCompletionBlock: (((any Error)?) -> Void)?](ckfetchrecordzonechangesoperation/fetchrecordzonechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordwithidwasdeletedblock-3z14c)*