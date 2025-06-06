# records(for:desiredKeys:)

**Framework**: CloudKit  
**Kind**: method

Fetches the specified records and returns them to an awaiting caller.

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
func records(for ids: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]? = nil) async throws -> [CKRecord.ID : Result<CKRecord, any Error>]
```

#### Return Value

A dictionary that contains the fetched records. The dictionary uses the identifiers you specify in `ids` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either the corresponding fetched record, or an error that describes why CloudKit can’t provide that record.

#### Discussion

If you’re fetching records of different types, make sure that `desiredKeys` is the union of all the fields you require across each distinct record type. This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account; otherwise, the returned dictionary includes any individual record errors.

For information on a more configurable way to fetch specific records, see [`CKFetchRecordsOperation`](ckfetchrecordsoperation.md).

## Parameters

- `ids`: The identifiers of the records to fetch.
- `desiredKeys`: The fields to include on each fetched record. To include all fields, specify  ; to fetch only system fields, specify an empty array.

## See Also

- [func fetch(withRecordIDs: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]?, completionHandler: (Result<[CKRecord.ID : Result<CKRecord, any Error>], any Error>) -> Void)](ckdatabase/fetch(withrecordids:desiredkeys:completionhandler:).md)
  Fetches the specified records and delivers them to a completion handler.
- [func fetch(withRecordID: CKRecord.ID, completionHandler: (CKRecord?, (any Error)?) -> Void)](ckdatabase/fetch(withrecordid:completionhandler:).md)
  Fetches a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/records(for:desiredkeys:))*