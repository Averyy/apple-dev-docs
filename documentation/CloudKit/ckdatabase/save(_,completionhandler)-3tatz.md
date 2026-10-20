# save(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Saves a specific record.

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
func save(_ record: CKRecord, completionHandler: @escaping @Sendable (CKRecord?, (any Error)?) -> Void)
```

```objc
- (void) saveRecord:(CKRecord *) record completionHandler:(void (^)(CKRecord *record, NSError *error)) completionHandler;
```

#### Discussion

The completion handler takes the following parameters:

- The saved record (as it appears on the server), or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully saves the record.

The save succeeds only when the specified record is new, or is a more recent version than the one on the server.

For information on a more convenient way to save records, see [`modifyRecords(saving:deleting:savePolicy:atomically:)`](./modifyrecords%28saving,deleting,savepolicy,atomically%29.md).

## Parameters

- `record`: The record to save.
- `completionHandler`: The closure to execute after CloudKit saves the record.

## See Also

### Modifying Records
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool) async throws -> (saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>])](./modifyrecords%28saving,deleting,savepolicy,atomically%29.md)
  Modifies the specified records and returns the results to an awaiting caller.
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool, completionHandler: (Result<(saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>]), any Error>) -> Void)](./modifyrecords%28saving,deleting,savepolicy,atomically,completionhandler%29.md)
  Modifies the specified records and delivers the results to a completion handler.
- [CKModifyRecordsOperation.RecordSavePolicy](../ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.
- [func delete(withRecordID: CKRecord.ID, completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](./delete%28withrecordid,completionhandler%29.md)
  Deletes a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/save(_:completionhandler:)-3tatz)*