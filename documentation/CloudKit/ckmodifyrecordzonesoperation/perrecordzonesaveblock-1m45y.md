# perRecordZoneSaveBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when CloudKit saves a record zone.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var perRecordZoneSaveBlock: ((CKRecordZone.ID, Result<CKRecordZone, any Error>) -> Void)? { get set }
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- The ID of the record zone that CloudKit saves.
- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either - The record zone that CloudKit saves
- An error that provides information about a failure saving the record zone.

The closure executes once for each record zone in the [`recordZonesToSave`](ckmodifyrecordzonesoperation/recordzonestosave.md) property. Each time the closure executes, it executes serially with respect to the other record zone completion blocks of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/perrecordzonesaveblock-1m45y)*