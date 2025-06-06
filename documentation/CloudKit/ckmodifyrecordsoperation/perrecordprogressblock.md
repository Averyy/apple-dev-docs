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
var perRecordProgressBlock: ((CKRecord, Double) -> Void)? { get set }
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- The record that CloudKit saves.
- The amount of data, as a percentage, that CloudKit saves for the record. The range is `0.0` to `1.0`, where `0.0` indicates that CloudKit hasn’t saved any data, and `1.0` means that CloudKit has saved the entire record.

The modify records operation executes this closure one or more times for each record in the [`recordsToSave`](ckmodifyrecordsoperation/recordstosave.md) property. Each time the closure executes, it executes serially with respect to the other progress closures of the operation. You can use this closure to track the ongoing progress of the operation.

If you intend to use this closure to process results, set it before you execute the operation or add the operation to a queue.

## See Also

- [var perRecordCompletionBlock: ((CKRecord, (any Error)?) -> Void)?](ckmodifyrecordsoperation/perrecordcompletionblock.md)
  The closure to execute when CloudKit saves a record.
- [var modifyRecordsCompletionBlock: (([CKRecord]?, [CKRecord.ID]?, (any Error)?) -> Void)?](ckmodifyrecordsoperation/modifyrecordscompletionblock.md)
  The closure to execute after CloudKit modifies all of the records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/perrecordprogressblock)*