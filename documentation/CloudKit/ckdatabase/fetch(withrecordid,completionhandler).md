# fetch(withRecordID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches a specific record.

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
func fetch(withRecordID recordID: CKRecord.ID, completionHandler: @escaping @Sendable (CKRecord?, (any Error)?) -> Void)
```

```swift
func fetch(withRecordID recordID: CKRecord.ID) async throws -> CKRecord
```

```objc
- (void) fetchRecordWithID:(CKRecordID *) recordID completionHandler:(void (^)(CKRecord *record, NSError *error)) completionHandler;
```

#### Discussion

The completion handler takes the following parameters:

- The requested record, or `nil` if CloudKit can’t provide that record.
- An error if a problem occurs, or `nil` if the fetch completes successfully.

For information on a more convenient way to fetch specific records, see [`records(for:desiredKeys:)`](./records%28for,desiredkeys%29.md).

## Parameters

- `recordID`: The identifier of the record to fetch.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

### Fetching Records
- [func records(for: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]?) async throws -> [CKRecord.ID : Result<CKRecord, any Error>]](./records%28for,desiredkeys%29.md)
  Fetches the specified records and returns them to an awaiting caller.
- [func fetch(withRecordIDs: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]?, completionHandler: (Result<[CKRecord.ID : Result<CKRecord, any Error>], any Error>) -> Void)](./fetch%28withrecordids,desiredkeys,completionhandler%29.md)
  Fetches the specified records and delivers them to a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withrecordid:completionhandler:))*