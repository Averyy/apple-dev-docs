# perRecordCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when a record becomes available.

**Availability**:
- iOS 8.0+ - Deprecated in 15.0
- iPadOS 8.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.10+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use perRecordResultBlock instead

## Declaration

```swift
var perRecordCompletionBlock: ((CKRecord?, CKRecord.ID?, (any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^perRecordCompletionBlock)(CKRecord *record, CKRecordID *recordID, NSError *error);
```

## Discussion

This property is a closure that returns no value and has the following parameters:

- The record, or `nil` if CloudKit can’t retrieve the record.
- The ID of the record.
- If CloudKit can’t retrieve the record, an error that provides information about the failure; otherwise, `nil`.

The fetch operation executes this closure once for each record ID in the [`recordIDs`](./recordids.md) property. Each time the closure executes, it executes serially with respect to the other progress closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.

## See Also

### Processing Record Fetch Results
- [var perRecordProgressBlock: ((CKRecord.ID, Double) -> Void)?](./perrecordprogressblock.md)
  The closure to execute with progress information for individual records.
- [var fetchRecordsCompletionBlock: (([CKRecord.ID : CKRecord]?, (any Error)?) -> Void)?](./fetchrecordscompletionblock.md)
  The closure to execute after CloudKit retrieves all of the records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/perrecordcompletionblock)*