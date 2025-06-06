# perRecordCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when CloudKit saves a record.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var perRecordCompletionBlock: ((CKRecord, (any Error)?) -> Void)? { get set }
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- The record that CloudKit saves.
- If CloudKit can’t save the record, an error that provides information about the failure; otherwise, `nil`.

The closure executes once for each record in the [`recordsToSave`](ckmodifyrecordsoperation/recordstosave.md) property. Each time the closure executes, it executes serially with respect to the other record completion blocks of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.

## See Also

- [var perRecordProgressBlock: ((CKRecord, Double) -> Void)?](ckmodifyrecordsoperation/perrecordprogressblock.md)
  The closure to execute with progress information for individual records.
- [var modifyRecordsCompletionBlock: (([CKRecord]?, [CKRecord.ID]?, (any Error)?) -> Void)?](ckmodifyrecordsoperation/modifyrecordscompletionblock.md)
  The closure to execute after CloudKit modifies all of the records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/perrecordcompletionblock)*