# recordChangedBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute with the contents of a changed record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var recordChangedBlock: ((CKRecord) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- The changed record. If you specify a value for the [`desiredKeys`](ckfetchrecordzonechangesoperation/zoneoptions/desiredkeys.md) property, the record contains only the corresponding fields.

The operation executes this closure once for each record in the record zone with changes since the previous fetch request. Each time the closure executes, it executes serially with respect to the other closures of the operation. If there aren’t any record changes, this closure doesn’t execute.

Set this property before you execute the operation or submit it to a queue.

## See Also

- [var recordWithIDWasDeletedBlock: ((CKRecord.ID, CKRecord.RecordType) -> Void)?](ckfetchrecordzonechangesoperation/recordwithidwasdeletedblock-3z14c.md)
  The closure to execute when a record no longer exists.
- [var recordZoneChangeTokensUpdatedBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonechangetokensupdatedblock.md)
  The closure to execute when the change token updates.
- [var recordZoneFetchCompletionBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?, Bool, (any Error)?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonefetchcompletionblock.md)
  The closure to execute when a record zone’s fetch finishes.
- [var fetchRecordZoneChangesCompletionBlock: (((any Error)?) -> Void)?](ckfetchrecordzonechangesoperation/fetchrecordzonechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordchangedblock)*