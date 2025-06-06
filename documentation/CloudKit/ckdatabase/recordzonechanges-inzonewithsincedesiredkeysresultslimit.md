# recordZoneChanges(inZoneWith:since:desiredKeys:resultsLimit:)

**Framework**: CloudKit  
**Kind**: method

Fetches all modified records from a specific record zone and returns them to an awaiting caller.

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
func recordZoneChanges(inZoneWith zoneID: CKRecordZone.ID, since changeToken: CKServerChangeToken?, desiredKeys: [CKRecord.FieldKey]? = nil, resultsLimit: Int? = nil) async throws -> (modificationResultsByID: [CKRecord.ID : Result<CKDatabase.RecordZoneChange.Modification, any Error>], deletions: [CKDatabase.RecordZoneChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool)
```

#### Return Value

A tuple with the following named elements:

#### Discussion

#### Discussion

This method fetches record changes in the specfied record zone, such as those that occur during record creation, modification, and deletion. It throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account; otherwise, the returned tuple includes any individual record errors.

Along with the fetched changes, CloudKit supplies a , which is an opaque token that denotes a specific point in the record zone’s history. Store this token and provide it the next time you execute this method. Change tokens conform to [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding) and are safe to cache on-disk. Don’t infer any behavior or order from a token’s contents.

For information on a more configurable way to fetch record zone changes, see [`CKFetchRecordZoneChangesOperation`](ckfetchrecordzonechangesoperation.md).

## Parameters

- `zoneID`: The identifier of the record zone with changes.
- `changeToken`: The change token from the previous execution of this method. If this is your app’s first fetch, or you want to refetch every change in the record zone’s history, specify  .
- `desiredKeys`: The fields to include on each fetched record. To include all fields, specify  ; to fetch only system fields, specify an empty array.
- `resultsLimit`: The maximum number of changes to return. The server may use a limit lower than this value.

## See Also

- [func databaseChanges(since: CKServerChangeToken?, resultsLimit: Int?) async throws -> (modifications: [CKDatabase.DatabaseChange.Modification], deletions: [CKDatabase.DatabaseChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool)](ckdatabase/databasechanges(since:resultslimit:).md)
  Fetches all modified record zones and returns them to an awaiting caller.
- [func fetchDatabaseChanges(since: CKServerChangeToken?, resultsLimit: Int?, completionHandler: (Result<(modifications: [CKDatabase.DatabaseChange.Modification], deletions: [CKDatabase.DatabaseChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)](ckdatabase/fetchdatabasechanges(since:resultslimit:completionhandler:).md)
  Fetches all modified record zones and delivers them to a completion handler.
- [CKDatabase.DatabaseChange](ckdatabase/databasechange.md)
  Objects that indicate the type of database change.
- [func fetchRecordZoneChanges(inZoneWith: CKRecordZone.ID, since: CKServerChangeToken?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int?, completionHandler: (Result<(modificationResultsByID: [CKRecord.ID : Result<CKDatabase.RecordZoneChange.Modification, any Error>], deletions: [CKDatabase.RecordZoneChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)](ckdatabase/fetchrecordzonechanges(inzonewith:since:desiredkeys:resultslimit:completionhandler:).md)
  Fetches all modified records from a specific record zone and delivers them to a completion handler.
- [CKDatabase.RecordZoneChange](ckdatabase/recordzonechange.md)
  Objects that indicate the type of record zone change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/recordzonechanges(inzonewith:since:desiredkeys:resultslimit:))*