# CKFetchRecordChangesOperation

**Framework**: CloudKit  
**Kind**: class

An operation that reports on the changed and deleted records in the specified record zone.

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
class CKFetchRecordChangesOperation
```

#### Overview

Use this type of operation object to optimize fetch operations for locally managed sets of records. Specifically, use it when you maintain a local cache of your record data and need to synchronize that cache periodically with the server.

To get the most benefit out of a `CKFetchRecordChangesOperation` object, you must maintain a local cache of the records from the specified zone. Each time you fetch changes from that zone, the server provides a token that identifies your request. With each subsequent fetch request, you initialize the operation object with the token from the previous request, and the server returns only the records with changes since that request.

The blocks you assign to process the fetched records execute serially on an internal queue that the operation manages. Your blocks must be capable of executing on a background thread, so any tasks that require access to the main thread must redirect accordingly.

If you assign a completion block to the [`completionBlock`](https://developer.apple.com/documentation/foundation/operation/1408085-completionblock) property of the operation object, the system calls the completion block after the operation executes and returns its results to you. You can use a completion block to perform housekeeping tasks for the operation, but don’t use it to process the results of the operation. Any completion block you specify should handle the failure of the operation to complete its task, whether due to an error or an explicit cancellation.

## Topics

### Creating the Fetch Record Changes Operation
- [convenience init(recordZoneID: CKRecordZone.ID, previousServerChangeToken: CKServerChangeToken?)](ckfetchrecordchangesoperation/init(recordzoneid:previousserverchangetoken:).md)
  Creates an operation for fetching changes in the specified record zone.
- [init()](ckfetchrecordchangesoperation/init.md)
  Creates an empty fetch record changes operation.
### Configuring the Fetch Record Changes Operation
- [var recordZoneID: CKRecordZone.ID?](ckfetchrecordchangesoperation/recordzoneid.md)
  The ID of the record zone with the records you want to fetch.
- [var previousServerChangeToken: CKServerChangeToken?](ckfetchrecordchangesoperation/previousserverchangetoken.md)
  The token that identifies the starting point for retrieving changes.
- [var desiredKeys: [String]?](ckfetchrecordchangesoperation/desiredkeys.md)
  The fields to fetch for the requested records.
- [var resultsLimit: Int](ckfetchrecordchangesoperation/resultslimit.md)
  The maximum number of changed records to report with this operation object.
- [var moreComing: Bool](ckfetchrecordchangesoperation/morecoming.md)
  A Boolean value that indicates whether more results are available.
### Processing the Fetch Record Changes Results
- [var recordChangedBlock: ((CKRecord) -> Void)?](ckfetchrecordchangesoperation/recordchangedblock.md)
  The block to execute with the contents of a changed record.
- [var recordWithIDWasDeletedBlock: ((CKRecord.ID) -> Void)?](ckfetchrecordchangesoperation/recordwithidwasdeletedblock.md)
  The block to execute with the ID of a deleted record.
- [var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, Data?, (any Error)?) -> Void)?](ckfetchrecordchangesoperation/fetchrecordchangescompletionblock.md)
  The block to execute when the system finishes processing all changes.

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

## See Also

- [class CKDiscoverAllUserIdentitiesOperation](ckdiscoveralluseridentitiesoperation.md)
  An operation that uses the device’s contacts to search for discoverable iCloud users.
- [class CKDiscoverUserIdentitiesOperation](ckdiscoveruseridentitiesoperation.md)
  An operation that uses the provided criteria to search for discoverable iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation)*