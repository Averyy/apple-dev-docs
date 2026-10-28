# perform(_:inZoneWith:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Searches for records matching a predicate in the specified record zone.

**Availability**:
- iOS 8.0+ - Deprecated in 15.0
- iPadOS 8.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.10+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: renamed to fetch(withQuery:inZoneWith:desiredKeys:resultsLimit:completionHandler:)

## Declaration

```swift
func perform(_ query: CKQuery, inZoneWith zoneID: CKRecordZone.ID?, completionHandler: @escaping @Sendable ([CKRecord]?, (any Error)?) -> Void)
```

```objc
- (void) performQuery:(CKQuery *) query inZoneWithID:(CKRecordZoneID *) zoneID completionHandler:(void (^)(NSArray<CKRecord *> *results, NSError *error)) completionHandler;
```

## Discussion

The completion handler takes the following parameters:

- The records that match the specified query, or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit completes the search successfully.

For information on a more convenient way to search a database, see [`records(matching:inZoneWith:desiredKeys:resultsLimit:)`](./records%28matching,inzonewith,desiredkeys,resultslimit%29.md).

## Parameters

- `query`: The query that contains the search parameters. For more information, see [`CKQuery`](../ckquery.md).
- `zoneID`: The identifier of the record zone to search. If you’re searching a shared database, provide a record zone identifier; otherwise, you can specify `nil` to search all record zones in the database.
- `completionHandler`: The closure to execute with the search results.

## See Also

### Querying Records
- [func records(matching: CKQuery, inZoneWith: CKRecordZone.ID?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int) async throws -> (matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?)](./records%28matching,inzonewith,desiredkeys,resultslimit%29.md)
  Searches for records that match a predicate and returns them to an awaiting caller.
- [func records(continuingMatchFrom: CKQueryOperation.Cursor, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int) async throws -> (matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?)](./records%28continuingmatchfrom,desiredkeys,resultslimit%29.md)
  Retrieves the next batch of records from an existing search and returns them to an awaiting caller.
- [func fetch(withQuery: CKQuery, inZoneWith: CKRecordZone.ID?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int, completionHandler: (Result<(matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?), any Error>) -> Void)](./fetch%28withquery,inzonewith,desiredkeys,resultslimit,completionhandler%29.md)
  Searches for records that match a predicate and delivers them to a completion handler.
- [func fetch(withCursor: CKQueryOperation.Cursor, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int, completionHandler: (Result<(matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?), any Error>) -> Void)](./fetch%28withcursor,desiredkeys,resultslimit,completionhandler%29.md)
  Retrieves the next batch of records from an existing search and delivers them to a completion handler.
- [func records(matching: CKQuery, inZoneWith: CKRecordZone.ID?) async throws -> [CKRecord]](./records%28matching,inzonewith%29.md)
  Searches for records in the specified record zone and returns them to an awaiting caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/perform(_:inzonewith:completionhandler:))*