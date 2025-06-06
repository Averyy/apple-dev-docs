# records(matching:inZoneWith:)

**Framework**: CloudKit  
**Kind**: method

Searches for records in the specified record zone and returns them to an awaiting caller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+ - Deprecated
- watchOS 8.0+

## Declaration

```swift
func records(matching query: CKQuery, inZoneWith zoneID: CKRecordZone.ID?) async throws -> [CKRecord]
```

#### Return Value

An array of records that match the specified query.

#### Discussion

For information on a more configurable way to search a database, see [`CKQueryOperation`](ckqueryoperation.md).

## Parameters

- `query`: The query that contains the search parameters. For more information, see  .
- `zoneID`: The identifier of the record zone to search. If you’re searching a shared database, provide a record zone identifier; otherwise, you can specify   to search all record zones in the database.

## See Also

- [func records(matching: CKQuery, inZoneWith: CKRecordZone.ID?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int) async throws -> (matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?)](ckdatabase/records(matching:inzonewith:desiredkeys:resultslimit:).md)
  Searches for records that match a predicate and returns them to an awaiting caller.
- [func records(continuingMatchFrom: CKQueryOperation.Cursor, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int) async throws -> (matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?)](ckdatabase/records(continuingmatchfrom:desiredkeys:resultslimit:).md)
  Retrieves the next batch of records from an existing search and returns them to an awaiting caller.
- [func fetch(withQuery: CKQuery, inZoneWith: CKRecordZone.ID?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int, completionHandler: (Result<(matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?), any Error>) -> Void)](ckdatabase/fetch(withquery:inzonewith:desiredkeys:resultslimit:completionhandler:).md)
  Searches for records that match a predicate and delivers them to a completion handler.
- [func fetch(withCursor: CKQueryOperation.Cursor, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int, completionHandler: (Result<(matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?), any Error>) -> Void)](ckdatabase/fetch(withcursor:desiredkeys:resultslimit:completionhandler:).md)
  Retrieves the next batch of records from an existing search and delivers them to a completion handler.
- [func perform(CKQuery, inZoneWith: CKRecordZone.ID?, completionHandler: ([CKRecord]?, (any Error)?) -> Void)](ckdatabase/perform(_:inzonewith:completionhandler:).md)
  Searches for records matching a predicate in the specified record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/records(matching:inzonewith:))*