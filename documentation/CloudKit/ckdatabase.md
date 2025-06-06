# CKDatabase

**Framework**: CloudKit  
**Kind**: class

An object that represents a collection of record zones and subscriptions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class CKDatabase
```

## Mentions

- [Deciding whether CloudKit is right for your app](deciding-whether-cloudkit-is-right-for-your-app.md)

#### Overview

A database takes requests and operations and applies them to the objects it contains, whether that’s record zones, records, or subscriptions. Each of your app’s users has access to the three separate databases:

- A public database that’s accessible to all users of your app.
- A private database that’s accessible only to the user of the current device.
- A shared database that’s accessible only to the user of the current device, which contains records that other iCloud users share with them.

The public database is always available, even when the device doesn’t have an active iCloud account. In this scenario, your app can fetch specific records and perform searches, but it can’t create or modify records. CloudKit requires an iCloud account for writing to the public database so it can identify the authors of any changes. All access to the private and shared databases requires an iCloud account.

You don’t create instances of [`CKDatabase`](ckdatabase.md), nor do you subclass it. Instead, you access the required database using one of your app’s containers. For more information, see [`CKContainer`](ckcontainer.md).

By default, CloudKit executes the methods in this class with a low-priority quality of service (QoS). To use a higher-priority QoS, perform the following:

1. Create an instance of [`CKOperation.Configuration`](ckoperation/configuration-swift.class.md) and set its [`qualityOfService`](ckoperation/configuration-swift.class/qualityofservice.md) property to the preferred value.
2. Call the databaseʼs [`configuredWith(configuration:group:body:)`](ckdatabase/configuredwith(configuration:group:body:)-637p1.md) method and provide the configuration and a trailing closure.
3. In the closure, use the provided database to execute the relevant methods at the preferred QoS.

```swift
func fetchRecords(with ids: [CKRecord.ID]) async throws
    -> [CKRecord.ID: Result<CKRecord, Error>] {

    // Get a reference to the user's private database.
    let database = CKContainer.default().privateCloudDatabase

    // Create a configuration with a higher-priority quality of service.
    let config = CKOperation.Configuration()
    config.qualityOfService = .userInitiated

    // Configure the database and execute the fetch.
    return try await database.configuredWith(configuration: config) { db in
        try await db.records(for: ids)
    }
}
```

## Topics

### Configuring Database Requests
- [func configuredWith<R>(configuration: CKOperation.Configuration?, group: CKOperationGroup?, body: (CKDatabase) async throws -> R) async rethrows -> R](ckdatabase/configuredwith(configuration:group:body:)-637p1.md)
  Applies a temporary configuration to the database within the scope of a closure that supports concurrency.
- [func configuredWith<R>(configuration: CKOperation.Configuration?, group: CKOperationGroup?, body: (CKDatabase) throws -> R) rethrows -> R](ckdatabase/configuredwith(configuration:group:body:)-12vrs.md)
  Applies a temporary configuration to the database within the scope of a closure.
### Fetching Records
- [func records(for: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]?) async throws -> [CKRecord.ID : Result<CKRecord, any Error>]](ckdatabase/records(for:desiredkeys:).md)
  Fetches the specified records and returns them to an awaiting caller.
- [func fetch(withRecordIDs: [CKRecord.ID], desiredKeys: [CKRecord.FieldKey]?, completionHandler: (Result<[CKRecord.ID : Result<CKRecord, any Error>], any Error>) -> Void)](ckdatabase/fetch(withrecordids:desiredkeys:completionhandler:).md)
  Fetches the specified records and delivers them to a completion handler.
- [func fetch(withRecordID: CKRecord.ID, completionHandler: (CKRecord?, (any Error)?) -> Void)](ckdatabase/fetch(withrecordid:completionhandler:).md)
  Fetches a specific record.
### Querying Records
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
- [func records(matching: CKQuery, inZoneWith: CKRecordZone.ID?) async throws -> [CKRecord]](ckdatabase/records(matching:inzonewith:).md)
  Searches for records in the specified record zone and returns them to an awaiting caller.
### Modifying Records
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool) async throws -> (saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>])](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:).md)
  Modifies the specified records and returns the results to an awaiting caller.
- [func modifyRecords(saving: [CKRecord], deleting: [CKRecord.ID], savePolicy: CKModifyRecordsOperation.RecordSavePolicy, atomically: Bool, completionHandler: (Result<(saveResults: [CKRecord.ID : Result<CKRecord, any Error>], deleteResults: [CKRecord.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:completionhandler:).md)
  Modifies the specified records and delivers the results to a completion hander.
- [CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.
- [func save(CKRecord, completionHandler: (CKRecord?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-3tatz.md)
  Saves a specific record.
- [func delete(withRecordID: CKRecord.ID, completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](ckdatabase/delete(withrecordid:completionhandler:).md)
  Deletes a specific record.
### Fetching Record Zones
- [func recordZones(for: [CKRecordZone.ID]) async throws -> [CKRecordZone.ID : Result<CKRecordZone, any Error>]](ckdatabase/recordzones(for:).md)
  Fetches the specified record zones and returns them to an awaiting caller.
- [func fetch(withRecordZoneIDs: [CKRecordZone.ID], completionHandler: (Result<[CKRecordZone.ID : Result<CKRecordZone, any Error>], any Error>) -> Void)](ckdatabase/fetch(withrecordzoneids:completionhandler:).md)
  Fetches the specified record zones and delivers them to a completion handler.
- [func fetchAllRecordZones(completionHandler: ([CKRecordZone]?, (any Error)?) -> Void)](ckdatabase/fetchallrecordzones(completionhandler:).md)
  Fetches all record zones from the current database.
- [func fetch(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](ckdatabase/fetch(withrecordzoneid:completionhandler:).md)
  Fetches a specific record zone.
### Modifying Record Zones
- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID]) async throws -> (saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>])](ckdatabase/modifyrecordzones(saving:deleting:).md)
  Modifies the specified record zones and returns the results to an awaiting caller.
- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID], completionHandler: (Result<(saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifyrecordzones(saving:deleting:completionhandler:).md)
  Modifies the specified record zones and delivers the results to a completion handler.
- [func save(CKRecordZone, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-32ffr.md)
  Saves a specific record zone.
- [func delete(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone.ID?, (any Error)?) -> Void)](ckdatabase/delete(withrecordzoneid:completionhandler:).md)
  Deletes a specific record zone.
### Fetching Subscriptions
- [func subscriptions(for: [CKSubscription.ID]) async throws -> [CKSubscription.ID : Result<CKSubscription, any Error>]](ckdatabase/subscriptions(for:).md)
  Fetches the specified subscriptions and returns them to an awaiting caller.
- [func fetch(withSubscriptionIDs: [CKSubscription.ID], completionHandler: (Result<[CKSubscription.ID : Result<CKSubscription, any Error>], any Error>) -> Void)](ckdatabase/fetch(withsubscriptionids:completionhandler:).md)
  Fetches the specified subscriptions and delivers them to a completion handler.
- [func subscription(for: CKSubscription.ID) async throws -> CKSubscription](ckdatabase/subscription(for:).md)
  Fetches a specific subscription and returns it to an awaiting caller.
- [func fetch(withSubscriptionID: CKSubscription.ID, completionHandler: (CKSubscription?, (any Error)?) -> Void)](ckdatabase/fetch(withsubscriptionid:completionhandler:).md)
  Fetches a specific subscription and delivers it to a completion handler.
- [func fetchAllSubscriptions(completionHandler: ([CKSubscription]?, (any Error)?) -> Void)](ckdatabase/fetchallsubscriptions(completionhandler:).md)
  Fetches all subscriptions from the current database.
### Modifying Subscriptions
- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID]) async throws -> (saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>])](ckdatabase/modifysubscriptions(saving:deleting:).md)
  Modifies the specified subscriptions and returns the results to an awaiting caller.
- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID], completionHandler: (Result<(saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifysubscriptions(saving:deleting:completionhandler:).md)
  Modifies the specified subscriptions and delivers the results to a completion handler.
- [func save(CKSubscription, completionHandler: (CKSubscription?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-9pona.md)
  Saves a specific subscription.
- [func deleteSubscription(withID: CKSubscription.ID) async throws -> CKSubscription.ID](ckdatabase/deletesubscription(withid:).md)
  Deletes a specific subscription and returns the deleted subscription’s identifier to an awaiting caller.
- [func delete(withSubscriptionID: CKSubscription.ID, completionHandler: (String?, (any Error)?) -> Void)](ckdatabase/delete(withsubscriptionid:completionhandler:).md)
  Deletes a specific subscription and delivers the deleted subscription’s identifier to a completion handler.
### Fetching Changes
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
- [CKDatabase.RecordZoneChange](ckdatabase/recordzonechange.md)
  Objects that indicate the type of record zone change.
### Running Operations
- [func add(CKDatabaseOperation)](ckdatabase/add(_:).md)
  Executes the specified operation in the current database.
### Getting the Database Type
- [var databaseScope: CKDatabase.Scope](ckdatabase/databasescope.md)
  The type of database.
- [CKDatabase.Scope](ckdatabase/scope.md)
  Constants that represent the scope of a database.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CKContainer](ckcontainer.md)
  A conduit to your app’s databases.
- [class CKOperationGroup](ckoperationgroup.md)
  An explicit association between two or more operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase)*