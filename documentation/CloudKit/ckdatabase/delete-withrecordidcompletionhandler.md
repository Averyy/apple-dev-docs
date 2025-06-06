# delete(withRecordID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Deletes a specific record.

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
func deleteRecord(withID recordID: CKRecord.ID) async throws -> CKRecord.ID
```

#### Discussion

The completion handler takes the following parameters:

- The identifier of the deleted record, or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully deletes the record.

Deleting a record may cause additional deletions if other records in the database reference the deleted record. CloudKit doesn’t provide the identifiers of any additional records it deletes.

For information on a more convenient way to delete records, see [`modifyRecords(saving:deleting:savePolicy:atomically:)`](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:).md).

## Parameters

- `recordID`: The identifier of the record to delete.
- `completionHandler`: The closure to execute after CloudKit deletes the record.

## See Also

- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool) async throws -> (saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>])](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:).md)
  Modifies the specified records and returns the results to an awaiting caller.
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool, completionHandler: (Result<(saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:completionhandler:).md)
  Modifies the specified records and delivers the results to a completion hander.
- [CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.
- [func save(CKRecord, completionHandler: (CKRecord?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-3tatz.md)
  Saves a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/delete(withrecordid:completionhandler:))*