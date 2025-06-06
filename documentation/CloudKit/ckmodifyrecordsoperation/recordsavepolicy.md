# CKModifyRecordsOperation.RecordSavePolicy

**Framework**: CloudKit  
**Kind**: enum

Constants that indicate which policy to apply when saving records.

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
enum RecordSavePolicy
```

## Topics

### Save Policies
- [CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged](ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md)
  A policy that instructs CloudKit to only proceed if the record’s change tag matches that of the server’s copy.
- [CKModifyRecordsOperation.RecordSavePolicy.changedKeys](ckmodifyrecordsoperation/recordsavepolicy/changedkeys.md)
  A policy that instructs CloudKit to save only the fields of a record that contain changes.
- [CKModifyRecordsOperation.RecordSavePolicy.allKeys](ckmodifyrecordsoperation/recordsavepolicy/allkeys.md)
  A policy that instructs CloudKit to save all keys of a record, even those without changes.
### Initializers
- [init?(rawValue: Int)](ckmodifyrecordsoperation/recordsavepolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool) async throws -> (saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>])](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:).md)
  Modifies the specified records and returns the results to an awaiting caller.
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool, completionHandler: (Result<(saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:completionhandler:).md)
  Modifies the specified records and delivers the results to a completion hander.
- [func save(CKRecord, completionHandler: (CKRecord?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-3tatz.md)
  Saves a specific record.
- [func delete(withRecordID: CKRecord.ID, completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](ckdatabase/delete(withrecordid:completionhandler:).md)
  Deletes a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy)*