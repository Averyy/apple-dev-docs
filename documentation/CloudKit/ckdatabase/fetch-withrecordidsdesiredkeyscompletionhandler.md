# fetch(withRecordIDs:desiredKeys:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the specified records and delivers them to a completion handler.

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
@preconcurrency
func fetch(withRecordIDs recordIDs: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]? = nil, completionHandler: @escaping (Result<[CKRecord.ID : Result<CKRecord, any Error>], any Error>) -> Void)
```

#### Discussion

The completion handler takes the following parameters:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either a dictionary of fetched records, or an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account. When present, the dictionary uses the identifiers you specify in `recordIDs` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either the corresponding fetched record, or an error that describes why CloudKit can’t provide that record.

If you’re fetching records of different types, make sure that `desiredKeys` is the union of all the fields you require across each distinct record type.

For information on a more configurable way to fetch specific records, see [`CKFetchRecordsOperation`](ckfetchrecordsoperation.md).

## Parameters

- `recordIDs`: The identifiers of the records to fetch.
- `desiredKeys`: The fields to include on each fetched record. To include all fields, specify  ; to fetch only system fields, specify an empty array.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func records(for: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]?) async throws -> [CKRecord.ID : Result<CKRecord, any Error>]](ckdatabase/records(for:desiredkeys:).md)
  Fetches the specified records and returns them to an awaiting caller.
- [func fetch(withRecordID: CKRecord.ID, completionHandler: (CKRecord?, (any Error)?) -> Void)](ckdatabase/fetch(withrecordid:completionhandler:).md)
  Fetches a specific record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withrecordids:desiredkeys:completionhandler:))*