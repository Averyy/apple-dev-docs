# CKModifyRecordsOperation.RecordSavePolicy

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate which policy to apply when saving records.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum RecordSavePolicy
```

```c
enum CKRecordSavePolicy : NSInteger;
```

## Topics

### Save Policies
- [CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged](./recordsavepolicy/ifserverrecordunchanged.md)
  A policy that instructs CloudKit to only proceed if the record’s change tag matches that of the server’s copy.
- [CKModifyRecordsOperation.RecordSavePolicy.changedKeys](./recordsavepolicy/changedkeys.md)
  A policy that instructs CloudKit to save only the fields of a record that contain changes.
- [CKModifyRecordsOperation.RecordSavePolicy.allKeys](./recordsavepolicy/allkeys.md)
  A policy that instructs CloudKit to save all keys of a record, even those without changes.
### Initializers
- [init?(rawValue: Int)](./recordsavepolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Modifying Records
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool) async throws -> (saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>])](../ckdatabase/modifyrecords%28saving,deleting,savepolicy,atomically%29.md)
  Modifies the specified records and returns the results to an awaiting caller.
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool, completionHandler: (Result<(saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>]), any Error>) -> Void)](../ckdatabase/modifyrecords%28saving,deleting,savepolicy,atomically,completionhandler%29.md)
  Modifies the specified records and delivers the results to a completion handler.
- [func save(CKRecord, completionHandler: (CKRecord?, (any Error)?) -> Void)](../ckdatabase/save%28_,completionhandler%29-3tatz.md)
  Saves a specific record.
- [func delete(withRecordID: CKRecord.ID, completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](../ckdatabase/delete%28withrecordid,completionhandler%29.md)
  Deletes a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordsavepolicy)*