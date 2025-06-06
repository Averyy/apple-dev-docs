# fetchRecordZoneChangesCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when the operation finishes.

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
var fetchRecordZoneChangesCompletionBlock: (((any Error)?) -> Void)? { get set }
```

#### Discussion

The closure has no return value and takes the following parameter:

- An error object that contains information about a problem, or `nil` if CloudKit successfully retrieves the record zone changes.

## See Also

- [var recordChangedBlock: ((CKRecord) -> Void)?](ckfetchrecordzonechangesoperation/recordchangedblock.md)
  The closure to execute with the contents of a changed record.
- [var recordWithIDWasDeletedBlock: ((CKRecord.ID, CKRecord.RecordType) -> Void)?](ckfetchrecordzonechangesoperation/recordwithidwasdeletedblock-3z14c.md)
  The closure to execute when a record no longer exists.
- [var recordZoneChangeTokensUpdatedBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonechangetokensupdatedblock.md)
  The closure to execute when the change token updates.
- [var recordZoneFetchCompletionBlock: ((CKRecordZone.ID, CKServerChangeToken?, Data?, Bool, (any Error)?) -> Void)?](ckfetchrecordzonechangesoperation/recordzonefetchcompletionblock.md)
  The closure to execute when a record zone’s fetch finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonechangesoperation/fetchrecordzonechangescompletionblock)*