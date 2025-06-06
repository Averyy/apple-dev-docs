# fetch(withCursor:desiredKeys:resultsLimit:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Retrieves the next batch of records from an existing search and delivers them to a completion handler.

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
func fetch(withCursor queryCursor: CKQueryOperation.Cursor, desiredKeys: [CKRecord.FieldKey]? = nil, resultsLimit: Int = CKQueryOperation.maximumResults, completionHandler: @escaping (Result<(matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?), any Error>) -> Void)
```

#### Discussion

The completion handler takes a single [`Result`](https://developer.apple.com/documentation/Swift/Result) parameter that contains either a tuple, or an error if the request fails. For example, when the network is unavailable or the device doesn’t have an active iCloud account.

When present, the tuple contains the following named elements:

If you specify `resultsLimit` and the number of matched records exceeds that value, CloudKit provides only that number of records and a  — an object that marks a specific location in the full search results. To retrieve the next subset of search results, execute this method again and pass the provided cursor from previous execution.

For information on a more configurable way to search a database, see [`CKQueryOperation`](ckqueryoperation.md).

## Parameters

- `queryCursor`: The cursor that identifies, within the full search results, the location of the next subset of results to retrieve.
- `desiredKeys`: The fields to include on each fetched record. To include all fields, specify  ; to fetch only system fields, specify an empty array.
- `resultsLimit`: The maximum number of records to return in a single set of results.
- `completionHandler`: The closure to execute with the search results.

## See Also

- [func records(matching: CKQuery, inZoneWith: CKRecordZone.ID?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int) async throws -> (matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?)](ckdatabase/records(matching:inzonewith:desiredkeys:resultslimit:).md)
  Searches for records that match a predicate and returns them to an awaiting caller.
- [func records(continuingMatchFrom: CKQueryOperation.Cursor, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int) async throws -> (matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?)](ckdatabase/records(continuingmatchfrom:desiredkeys:resultslimit:).md)
  Retrieves the next batch of records from an existing search and returns them to an awaiting caller.
- [func fetch(withQuery: CKQuery, inZoneWith: CKRecordZone.ID?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int, completionHandler: (Result<(matchResults: [(CKRecord.ID, Result<CKRecord, any Error>)], queryCursor: CKQueryOperation.Cursor?), any Error>) -> Void)](ckdatabase/fetch(withquery:inzonewith:desiredkeys:resultslimit:completionhandler:).md)
  Searches for records that match a predicate and delivers them to a completion handler.
- [func perform(CKQuery, inZoneWith: CKRecordZone.ID?, completionHandler: ([CKRecord]?, (any Error)?) -> Void)](ckdatabase/perform(_:inzonewith:completionhandler:).md)
  Searches for records matching a predicate in the specified record zone.
- [func records(matching: CKQuery, inZoneWith: CKRecordZone.ID?) async throws -> [CKRecord]](ckdatabase/records(matching:inzonewith:).md)
  Searches for records in the specified record zone and returns them to an awaiting caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withcursor:desiredkeys:resultslimit:completionhandler:))*