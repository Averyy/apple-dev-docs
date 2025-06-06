# save(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Saves a specific record.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func save(_ record: CKRecord) async throws -> CKRecord
```

#### Discussion

The completion handler takes the following parameters:

- The saved record (as it appears on the server), or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully saves the record.

The save succeeds only when the specified record is new, or is a more recent version than the one on the server.

For information on a more convenient way to save records, see [`modifyRecords(saving:deleting:savePolicy:atomically:)`](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:).md).

## Parameters

- `record`: The record to save.
- `completionHandler`: The closure to execute after CloudKit saves the record.

## See Also

- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool) async throws -> (saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>])](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:).md)
  Modifies the specified records and returns the results to an awaiting caller.
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool, completionHandler: (Result<(saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:completionhandler:).md)
  Modifies the specified records and delivers the results to a completion hander.
- [CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.
- [func delete(withRecordID: CKRecord.ID, completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](ckdatabase/delete(withrecordid:completionhandler:).md)
  Deletes a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/save(_:completionhandler:)-3tatz)*