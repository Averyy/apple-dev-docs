# perform(_:inZoneWith:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Searches for records matching a predicate in the specified record zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func perform(_ query: CKQuery, inZoneWith zoneID: CKRecordZone.ID?) async throws -> [CKRecord]
```

#### Discussion

The completion handler takes the following parameters:

- The records that match the specified query, or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit completes the search successfully.

For information on a more convenient way to search a database, see [`records(matching:inZoneWith:desiredKeys:resultsLimit:)`](ckdatabase/records(matching:inzonewith:desiredkeys:resultslimit:).md).

## Parameters

- `query`: The query that contains the search parameters. For more information, see  .
- `zoneID`: The identifier of the record zone to search. If you’re searching a shared database, provide a record zone identifier; otherwise, you can specify   to search all record zones in the database.
- `completionHandler`: The closure to execute with the search results.

## See Also

- [func records(matching: CKQuery, inZoneWith: CKRecordZone.ID?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int) async throws -> (matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?)](ckdatabase/records(matching:inzonewith:desiredkeys:resultslimit:).md)
  Searches for records that match a predicate and returns them to an awaiting caller.
- [func records(continuingMatchFrom: CKQueryOperation.Cursor, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int) async throws -> (matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?)](ckdatabase/records(continuingmatchfrom:desiredkeys:resultslimit:).md)
  Retrieves the next batch of records from an existing search and returns them to an awaiting caller.
- [func fetch(withQuery: CKQuery, inZoneWith: CKRecordZone.ID?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int, completionHandler: (Result<(matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?), any Error>) -> Void)](ckdatabase/fetch(withquery:inzonewith:desiredkeys:resultslimit:completionhandler:).md)
  Searches for records that match a predicate and delivers them to a completion handler.
- [func fetch(withCursor: CKQueryOperation.Cursor, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int, completionHandler: (Result<(matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?), any Error>) -> Void)](ckdatabase/fetch(withcursor:desiredkeys:resultslimit:completionhandler:).md)
  Retrieves the next batch of records from an existing search and delivers them to a completion handler.
- [func records(matching: CKQuery, inZoneWith: CKRecordZone.ID?) async throws -> [CKRecord]](ckdatabase/records(matching:inzonewith:).md)
  Searches for records in the specified record zone and returns them to an awaiting caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/perform(_:inzonewith:completionhandler:))*