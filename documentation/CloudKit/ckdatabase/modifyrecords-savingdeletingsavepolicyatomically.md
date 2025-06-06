# modifyRecords(saving:deleting:savePolicy:atomically:)

**Framework**: CloudKit  
**Kind**: method

Modifies the specified records and returns the results to an awaiting caller.

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
func modifyRecords(saving recordsToSave: [CKRecord], deleting recordIDsToDelete: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy = .ifServerRecordUnchanged, atomically: Bool = true) async throws -> (saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>])
```

#### Return Value

A tuple with the following named elements:

#### Discussion

#### Discussion

Deleting records may cause additional deletions if other records in the database reference the deleted records. CloudKit doesn’t provide the identifiers of any additional records it deletes. This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account, or when `atomically` is [`true`](https://developer.apple.com/documentation/swift/true) and one or more of the specified changes fail; otherwise, the returned tuple includes any individual record errors.

For information on a more configurable way to modify records, see [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md).

## Parameters

- `recordsToSave`: The records to save.
- `recordIDsToDelete`: The identifiers of the records to permanently delete.
- `savePolicy`: The policy to use when modifying existing records. For possible values, see  .
- `atomically`: If  , the entire operation fails if CloudKit can’t modify one or more of the specified records; otherwise, CloudKit reports individual failures in the returned tuple. Atomic changes are only applicable in record zones that have the   capability.

## See Also

- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool, completionHandler: (Result<(saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:completionhandler:).md)
  Modifies the specified records and delivers the results to a completion hander.
- [CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.
- [func save(CKRecord, completionHandler: (CKRecord?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-3tatz.md)
  Saves a specific record.
- [func delete(withRecordID: CKRecord.ID, completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](ckdatabase/delete(withrecordid:completionhandler:).md)
  Deletes a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:))*