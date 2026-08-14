# recordWasChangedBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute with the results of retrieving a record change.

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
var recordWasChangedBlock: ((CKRecord.ID, Result<CKRecord, any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- A [`Result`](https://developer.apple.com/documentation/swift/result) that contains either: - The changed record. If you specify a value for the [`desiredKeys`](ckfetchrecordzonechangesoperation/zoneconfiguration/desiredkeys.md) property, the record contains only the corresponding fields.
- An error that contains information about a problem encountered retrieving the changed record.

The operation executes this closure once for each record in the record zone with changes since the previous fetch request. Each time the closure executes, it executes serially with respect to the other closures of the operation. If there aren’t any record changes, this closure doesn’t execute.

Set this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/recordwaschangedblock-x5bw)*