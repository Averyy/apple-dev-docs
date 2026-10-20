# fetchRecordZoneChangesCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when the operation finishes.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.12+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use fetchRecordZoneChangesResultBlock instead

## Declaration

```swift
var fetchRecordZoneChangesCompletionBlock: (((any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^fetchRecordZoneChangesCompletionBlock)(NSError *operationError);
```

#### Discussion

The closure has no return value and takes the following parameter:

- An error object that contains information about a problem, or `nil` if CloudKit successfully retrieves the record zone changes.

This closure executes only once, and represents your final opportunity to process the results. The closure executes serially with respect to the other closures of the operation.

Set this property before you execute the operation or submit it to a queue.

## See Also

### Processing the Zone Change Operation Results
- [var recordChangedBlock: ((CKRecord) -> Void)?](./recordchangedblock.md)
  The closure to execute with the contents of a changed record.
- [var recordWithIDWasDeletedBlock: ((CKRecord.ID, CKRecord.RecordType) -> Void)?](./recordwithidwasdeletedblock-3z14c.md)
  The closure to execute when a record no longer exists.
- [var recordZoneChangeTokensUpdatedBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?) -> Void)?](./recordzonechangetokensupdatedblock.md)
  The closure to execute when the change token updates.
- [var recordZoneFetchCompletionBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?, Bool, (any Error)?) -> Void)?](./recordzonefetchcompletionblock.md)
  The closure to execute when a record zone’s fetch finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/fetchrecordzonechangescompletionblock)*