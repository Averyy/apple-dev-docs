# delete(withRecordID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Deletes a specific record.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func delete(withRecordID recordID: CKRecord.ID, completionHandler: @escaping @Sendable (CKRecord.ID?, (any Error)?) -> Void)
```

```swift
func delete(withRecordID recordID: CKRecord.ID) async throws -> CKRecord.ID
```

```objc
- (void) deleteRecordWithID:(CKRecordID *) recordID completionHandler:(void (^)(CKRecordID *recordID, NSError *error)) completionHandler;
```

## Discussion

The completion handler takes the following parameters:

- The identifier of the deleted record, or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully deletes the record.

Deleting a record may cause additional deletions if other records in the database reference the deleted record. CloudKit doesn’t provide the identifiers of any additional records it deletes.

For information on a more convenient way to delete records, see [`modifyRecords(saving:deleting:savePolicy:atomically:)`](./modifyrecords%28saving,deleting,savepolicy,atomically%29.md).

## Parameters

- `recordID`: The identifier of the record to delete.
- `completionHandler`: The closure to execute after CloudKit deletes the record.

## See Also

### Modifying Records
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool) async throws -> (saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>])](./modifyrecords%28saving,deleting,savepolicy,atomically%29.md)
  Modifies the specified records and returns the results to an awaiting caller.
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool, completionHandler: (Result<(saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>]), any Error>) -> Void)](./modifyrecords%28saving,deleting,savepolicy,atomically,completionhandler%29.md)
  Modifies the specified records and delivers the results to a completion handler.
- [CKModifyRecordsOperation.RecordSavePolicy](../ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.
- [func save(CKRecord, completionHandler: (CKRecord?, (any Error)?) -> Void)](./save%28_,completionhandler%29-3tatz.md)
  Saves a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/delete(withrecordid:completionhandler:))*