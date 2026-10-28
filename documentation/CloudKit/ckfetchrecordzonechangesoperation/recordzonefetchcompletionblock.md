# recordZoneFetchCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when a record zone’s fetch finishes.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.12+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use recordZoneFetchResultBlock instead

## Declaration

```swift
var recordZoneFetchCompletionBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?, Bool, (any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^recordZoneFetchCompletionBlock)(CKRecordZoneID *recordZoneID, CKServerChangeToken *serverChangeToken, NSData *clientChangeTokenData, BOOL moreComing, NSError *recordZoneError);
```

## Discussion

The closure returns no value and takes the following parameters:

- The record zone’s ID.
- The change token to store and use in subsequent instances of [`CKFetchRecordZoneChangesOperation`](../ckfetchrecordzonechangesoperation.md).
- The more recent client change token from the device. If the change token isn’t the more recent change token you provided, the server might not have received the associated changes.
- A Boolean that indicates whether this is the final record zone change. If [`fetchAllChanges`](./fetchallchanges.md) is [`false`](../../Swift/false.md), it’s the app’s responsibility to create additional instances of [`CKFetchRecordZoneChangesOperation`](../ckfetchrecordzonechangesoperation.md) to fetch further changes.
- An error object that contains information about a problem, or `nil` if the operation successfully retrieves the results.

The app is responsible for saving the change token at the end of the operation and providing it to future uses of [`CKFetchRecordZoneChangesOperation`](../ckfetchrecordzonechangesoperation.md). Each time the closure executes, it executes serially with respect to the other closures of the operation.

Set this property before you execute the operation or submit it to a queue.

## See Also

### Processing the Zone Change Operation Results
- [var recordChangedBlock: ((CKRecord) -> Void)?](./recordchangedblock.md)
  The closure to execute with the contents of a changed record.
- [var recordWithIDWasDeletedBlock: ((CKRecord.ID, CKRecord.RecordType) -> Void)?](./recordwithidwasdeletedblock-3z14c.md)
  The closure to execute when a record no longer exists.
- [var recordZoneChangeTokensUpdatedBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?) -> Void)?](./recordzonechangetokensupdatedblock.md)
  The closure to execute when the change token updates.
- [var fetchRecordZoneChangesCompletionBlock: (((any Error)?) -> Void)?](./fetchrecordzonechangescompletionblock.md)
  The closure to execute when the operation finishes.
- [recordWithIDWasDeletedBlock](./recordwithidwasdeletedblock-912xy.md)
  The block to execute when a record no longer exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordzonefetchcompletionblock)*