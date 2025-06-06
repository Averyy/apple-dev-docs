# fetch(withRecordID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches a specific record.

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
func record(for recordID: CKRecord.ID) async throws -> CKRecord
```

#### Discussion

The completion handler takes the following parameters:

- The requested record, or `nil` if CloudKit can’t provide that record.
- An error if a problem occurs, or `nil` if the fetch completes successfully.

For information on a more convenient way to fetch specific records, see [`records(for:desiredKeys:)`](ckdatabase/records(for:desiredkeys:).md).

## Parameters

- `recordID`: The identifier of the record to fetch.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func records(for: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]?) async throws -> [CKRecord.ID : Result<CKRecord, any Error>]](ckdatabase/records(for:desiredkeys:).md)
  Fetches the specified records and returns them to an awaiting caller.
- [func fetch(withRecordIDs: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]?, completionHandler: (Result<[CKRecord.ID : Result<CKRecord, any Error>], any Error>) -> Void)](ckdatabase/fetch(withrecordids:desiredkeys:completionhandler:).md)
  Fetches the specified records and delivers them to a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withrecordid:completionhandler:))*