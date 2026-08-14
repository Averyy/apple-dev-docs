# recordZoneFetchCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when a record zone’s fetch finishes.

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
var recordZoneFetchCompletionBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?, Bool, (any Error)?) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- The record zone’s ID.
- The change token to store and use in subsequent instances of [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md).
- The more recent client change token from the device. If the change token isn’t the more recent change token you provided, the server might not have received the associated changes.
- A Boolean that indicates whether this is the final record zone change. If [`fetchAllChanges`](ckfetchrecordzonechangesoperation/fetchallchanges.md) is [`false`](https://developer.apple.com/documentation/swift/false), it’s the app’s responsibility to create additional instances of [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md) to fetch further changes.
- An error object that contains information about a problem, or `nil` if the operation successfully retrieves the results.

The app is responsible for saving the change token at the end of the operation and providing it to future uses of [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md). Each time the closure executes, it executes serially with respect to the other closures of the operation.

Set this property before you execute the operation or submit it to a queue.

## See Also

- [var recordChangedBlock: ((CKRecord) -> Void)?](ckfetchrecordzonechangesoperation/recordchangedblock.md)
  The closure to execute with the contents of a changed record.
- [var recordWithIDWasDeletedBlock: ((CKRecord.ID, CKRecord.RecordType) -> Void)?](ckfetchrecordzonechangesoperation/recordwithidwasdeletedblock-3z14c.md)
  The closure to execute when a record no longer exists.
- [var recordZoneChangeTokensUpdatedBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonechangetokensupdatedblock.md)
  The closure to execute when the change token updates.
- [var fetchRecordZoneChangesCompletionBlock: (((any Error)?) -> Void)?](ckfetchrecordzonechangesoperation/fetchrecordzonechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordzonefetchcompletionblock)*