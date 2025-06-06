# databaseChanges(since:resultsLimit:)

**Framework**: CloudKit  
**Kind**: method

Fetches all modified record zones and returns them to an awaiting caller.

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
func databaseChanges(since changeToken: CKServerChangeToken?, resultsLimit: Int? = nil) async throws -> (modifications: [CKDatabase.DatabaseChange.Modification], deletions: [CKDatabase.DatabaseChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool)
```

#### Return Value

A tuple with the following named elements:

#### Discussion

#### Discussion

This method fetches record zone changes in a database, which includes new record zones, changed zones — including deleted or purged zones — and zones that contain record changes. It throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account.

Along with the fetched changes, CloudKit supplies a , which is an opaque token that denotes a specific point in the database’s history. Store this token and provide it the next time you execute this method. Change tokens conform to [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) and are safe to cache on-disk. Don’t infer any behavior or order from a token’s contents.

For information on a more configurable way to fetch database changes, see [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md).

## Parameters

- `changeToken`: The change token from the previous execution of this method. If this is your app’s first fetch, or you want to refetch every change in the database’s history, specify  .
- `resultsLimit`: The maximum number of changes to return. The server may use a limit lower than this value.

## See Also

- [func fetchDatabaseChanges(since: CKServerChangeToken?, resultsLimit: Int?, completionHandler: (Result<(modifications: [CKDatabase.DatabaseChange.Modification], deletions: [CKDatabase.DatabaseChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)](ckdatabase/fetchdatabasechanges(since:resultslimit:completionhandler:).md)
  Fetches all modified record zones and delivers them to a completion handler.
- [CKDatabase.DatabaseChange](ckdatabase/databasechange.md)
  Objects that indicate the type of database change.
- [func recordZoneChanges(inZoneWith: CKRecordZone.ID, since: CKServerChangeToken?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int?) async throws -> (modificationResultsByID: [CKRecord.ID : Result<CKDatabase.RecordZoneChange.Modification, any Error>], deletions: [CKDatabase.RecordZoneChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool)](ckdatabase/recordzonechanges(inzonewith:since:desiredkeys:resultslimit:).md)
  Fetches all modified records from a specific record zone and returns them to an awaiting caller.
- [func fetchRecordZoneChanges(inZoneWith: CKRecordZone.ID, since: CKServerChangeToken?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int?, completionHandler: (Result<(modificationResultsByID: [CKRecord.ID : Result<CKDatabase.RecordZoneChange.Modification, any Error>], deletions: [CKDatabase.RecordZoneChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)](ckdatabase/fetchrecordzonechanges(inzonewith:since:desiredkeys:resultslimit:completionhandler:).md)
  Fetches all modified records from a specific record zone and delivers them to a completion handler.
- [CKDatabase.RecordZoneChange](ckdatabase/recordzonechange.md)
  Objects that indicate the type of record zone change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/databasechanges(since:resultslimit:))*