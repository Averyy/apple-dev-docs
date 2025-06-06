# CKDatabase.RecordZoneChange

**Framework**: CloudKit  
**Kind**: enum

Objects that indicate the type of record zone change.

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
enum RecordZoneChange
```

## Topics

### Modifications
- [CKDatabase.RecordZoneChange.Modification](ckdatabase/recordzonechange/modification.md)
  A record zone change that represents the modification of a record.
### Deletions
- [CKDatabase.RecordZoneChange.Deletion](ckdatabase/recordzonechange/deletion.md)
  A record zone change that represents the deletion of a record.

## See Also

- [func databaseChanges(since: CKServerChangeToken?, resultsLimit: Int?) async throws -> (modifications: [CKDatabase.DatabaseChange.Modification], deletions: [CKDatabase.DatabaseChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool)](ckdatabase/databasechanges(since:resultslimit:).md)
  Fetches all modified record zones and returns them to an awaiting caller.
- [func fetchDatabaseChanges(since: CKServerChangeToken?, resultsLimit: Int?, completionHandler: (Result<(modifications: [CKDatabase.DatabaseChange.Modification], deletions: [CKDatabase.DatabaseChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)](ckdatabase/fetchdatabasechanges(since:resultslimit:completionhandler:).md)
  Fetches all modified record zones and delivers them to a completion handler.
- [CKDatabase.DatabaseChange](ckdatabase/databasechange.md)
  Objects that indicate the type of database change.
- [func recordZoneChanges(inZoneWith: CKRecordZone.ID, since: CKServerChangeToken?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int?) async throws -> (modificationResultsByID: [CKRecord.ID : Result<CKDatabase.RecordZoneChange.Modification, any Error>], deletions: [CKDatabase.RecordZoneChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool)](ckdatabase/recordzonechanges(inzonewith:since:desiredkeys:resultslimit:).md)
  Fetches all modified records from a specific record zone and returns them to an awaiting caller.
- [func fetchRecordZoneChanges(inZoneWith: CKRecordZone.ID, since: CKServerChangeToken?, desiredKeys: [CKRecord.FieldKey]?, resultsLimit: Int?, completionHandler: (Result<(modificationResultsByID: [CKRecord.ID : Result<CKDatabase.RecordZoneChange.Modification, any Error>], deletions: [CKDatabase.RecordZoneChange.Deletion], changeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)](ckdatabase/fetchrecordzonechanges(inzonewith:since:desiredkeys:resultslimit:completionhandler:).md)
  Fetches all modified records from a specific record zone and delivers them to a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/recordzonechange)*