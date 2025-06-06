# fetchDatabaseChanges(since:resultsLimit:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches all modified record zones and delivers them to a completion handler.

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
func fetchDatabaseChanges(since changeToken: CKServerChangeToken?, resultsLimit: Int? = nil, completionHandler: @escaping (Result<(modifications: [CKDatabase.DatabaseChange.Modification], deletions: [CKDatabase.DatabaseChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)
```

#### Discussion

The completion handler takes a single [`Result`](https://developer.apple.com/documentation/Swift/Result) parameter that contains either a tuple, or an error if the request fails. For example, when the network is unavailable or the device doesn’t have an active iCloud account.

When present, the tuple contains the following named elements:

This method fetches record zone changes in a database, which includes new record zones, changed zones — including deleted or purged zones — and zones that contain record changes.

Along with the fetched changes, CloudKit supplies a , which is an opaque token that denotes a specific point in the database’s history. Store this token and provide it the next time you execute this method. Change tokens conform to [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) and are safe to cache on-disk. Don’t infer any behavior or order from a token’s contents.

For information on a more configurable way to fetch database changes, see [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md).

## Parameters

- `changeToken`: The change token from the previous execution of this method. If this is your app’s first fetch, or you want to refetch every change in the database’s history, specify  .
- `resultsLimit`: The maximum number of changes to return. The server may use a limit lower than this value.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func databaseChanges(since: CKServerChangeToken?, resultsLimit: Int?) async throws -> (modifications: [CKDatabase.DatabaseChange.Modification], deletions: [CKDatabase.DatabaseChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool)](ckdatabase/databasechanges(since:resultslimit:).md)
  Fetches all modified record zones and returns them to an awaiting caller.
- [CKDatabase.DatabaseChange](ckdatabase/databasechange.md)
  Objects that indicate the type of database change.
- [func recordZoneChanges(inZoneWith: CKRecordZone.ID, since: CKServerChangeToken?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int?) async throws -> (modificationResultsByID: [CKRecord.ID : Result<CKDatabase.RecordZoneChange.Modification, any Error>], deletions: [CKDatabase.RecordZoneChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool)](ckdatabase/recordzonechanges(inzonewith:since:desiredkeys:resultslimit:).md)
  Fetches all modified records from a specific record zone and returns them to an awaiting caller.
- [func fetchRecordZoneChanges(inZoneWith: CKRecordZone.ID, since: CKServerChangeToken?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int?, completionHandler: (Result<(modificationResultsByID: [CKRecord.ID : Result<CKDatabase.RecordZoneChange.Modification, any Error>], deletions: [CKDatabase.RecordZoneChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)](ckdatabase/fetchrecordzonechanges(inzonewith:since:desiredkeys:resultslimit:completionhandler:).md)
  Fetches all modified records from a specific record zone and delivers them to a completion handler.
- [CKDatabase.RecordZoneChange](ckdatabase/recordzonechange.md)
  Objects that indicate the type of record zone change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetchdatabasechanges(since:resultslimit:completionhandler:))*