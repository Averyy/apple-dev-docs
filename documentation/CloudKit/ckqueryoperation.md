# CKQueryOperation

**Framework**: CloudKit  
**Kind**: class

An operation for executing queries in a database.

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
class CKQueryOperation
```

#### Overview

A `CKQueryOperation` object is a concrete operation that you can use to execute queries. A query operation applies query parameters to the specified database and record zone, delivering any matching records asynchronously to the handlers that you provide.

To perform a new search:

1. Initialize a `CKQueryOperation` object with a [`CKQuery`](ckquery.md) object that contains the search criteria and sorting information for the records you want.
2. Assign a handler to the [`queryCompletionBlock`](ckqueryoperation/querycompletionblock.md) property so that you can process the results and execute the operation.

If the search yields many records, the operation object may deliver a portion of the total results to your blocks immediately, along with a cursor for obtaining the remaining records. Use the cursor to initialize and execute a separate `CKQueryOperation` instance when you’re ready to process the next batch of results. 3. Optionally, configure the results by specifying values for the [`resultsLimit`](ckqueryoperation/resultslimit.md) and [`desiredKeys`](ckqueryoperation/desiredkeys-4a6vy.md) properties. 4. Pass the query operation object to the [`add(_:)`](ckdatabase/add(_:).md) method of the target database to execute the operation.

CloudKit restricts queries to the records in a single record zone. For new queries, you specify the zone when you initialize the query operation object. For cursor-based queries, the cursor contains the zone information. To search for records in multiple zones, you must create a separate `CKQueryOperation` object for each zone you want to search, although you can initialize each of them with the same [`CKQuery`](ckquery.md) object.

If you assign a handler to the operation’s [`completionBlock`](https://developer.apple.com/documentation/Foundation/Operation/completionBlock) property, the operation calls it after it executes and returns any results. Use a handler to perform housekeeping tasks for the operation, but don’t use it to process the results of the operation. The handler you provide should manage any failures, whether due to an error or an explicit cancellation.

## Topics

### Creating a Query Operation
- [convenience init(query: CKQuery)](ckqueryoperation/init(query:).md)
  Creates an operation that searches for records in the specified record zone.
- [convenience init(cursor: CKQueryOperation.Cursor)](ckqueryoperation/init(cursor:).md)
  Creates an operation with additional results from a previous search.
- [init()](ckqueryoperation/init.md)
  Creates an empty query operation.
### Configuring the Query Operation
- [var query: CKQuery?](ckqueryoperation/query.md)
  The query for the search.
- [var cursor: CKQueryOperation.Cursor?](ckqueryoperation/cursor-swift.property.md)
  The  cursor for continuing the search.
- [CKQueryOperation.Cursor](ckqueryoperation/cursor-swift.class.md)
  An object that marks the stopping point for a query and the starting point for retrieving the remaining results.
- [var zoneID: CKRecordZone.ID?](ckqueryoperation/zoneid.md)
  The ID of the record zone that contains the records to search.
- [var resultsLimit: Int](ckqueryoperation/resultslimit.md)
  The maximum number of records to return at one time.
- [class let maximumResults: Int](ckqueryoperation/maximumresults.md)
  A constant value that represents the maximum number of results CloudKit retrieves.
- [var desiredKeys: [CKRecord.FieldKey]?](ckqueryoperation/desiredkeys-7qrse.md)
  The fields of the records to fetch.
### Processing the Query Results
- [var recordFetchedBlock: ((CKRecord) -> Void)?](ckqueryoperation/recordfetchedblock.md)
  The closure to execute when a record becomes available.
- [var queryCompletionBlock: ((CKQueryOperation.Cursor?, (any Error)?) -> Void)?](ckqueryoperation/querycompletionblock.md)
  The closure to execute after CloudKit retrieves all of the records.
### Instance Properties
- [var queryResultBlock: ((Result<CKQueryOperation.Cursor?, any Error>) -> Void)?](ckqueryoperation/queryresultblock.md)
- [var recordMatchedBlock: ((CKRecord.ID, Result<CKRecord, any Error>) -> Void)?](ckqueryoperation/recordmatchedblock-2qze7.md)

## Relationships

### Inherits From
- [CKDatabaseOperation](ckdatabaseoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CKQuery](ckquery.md)
  A query that describes the criteria to apply when searching for records in a database.
- [class CKLocationSortDescriptor](cklocationsortdescriptor.md)
  An object for sorting records that contain location data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation)*