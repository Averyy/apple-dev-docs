# perRecordProgressBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute with progress information for individual records.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var perRecordProgressBlock: ((CKRecord.ID, Double) -> Void)? { get set }
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- The ID of the record to retrieve.
- The amount of data, as a percentage, that CloudKit downloads for the record. The range is `0.0` to `1.0`, where `0.0` indicates that CloudKit hasn’t downloaded anything, and `1.0` means the download is complete.

The fetch operation executes this closure one or more times for each record ID in the [`recordIDs`](ckfetchrecordsoperation/recordids.md) property. Each time the closure executes, it executes serially with respect to the other progress closures of the operation. You can use this closure to track the ongoing progress of the download operation.

If you intend to use this closure to process results, set it before you execute the operation or add the operation to a queue.

## See Also

- [var perRecordCompletionBlock: ((CKRecord?, CKRecord.ID?, (any Error)?) -> Void)?](ckfetchrecordsoperation/perrecordcompletionblock.md)
  The closure to execute when a record becomes available.
- [var fetchRecordsCompletionBlock: (([CKRecord.ID : CKRecord]?, (any Error)?) -> Void)?](ckfetchrecordsoperation/fetchrecordscompletionblock.md)
  The closure to execute after CloudKit retrieves all of the records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/perrecordprogressblock)*