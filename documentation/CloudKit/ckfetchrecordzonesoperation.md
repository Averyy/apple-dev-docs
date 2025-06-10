# CKFetchRecordZonesOperation

**Framework**: CloudKit  
**Kind**: class

An operation for retrieving record zones from a database.

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
class CKFetchRecordZonesOperation
```

## Mentions

- [Encrypting User Data](encrypting-user-data.md)

#### Overview

Use this operation object to fetch record zones so that you can ascertain their capabilities.

If you assign a handler to the [`completionBlock`](https://developer.apple.com/documentation/Foundation/Operation/completionBlock) property of the operation, CloudKit calls it after the operation executes and returns its results. You can use the handler to perform any housekeeping tasks that relate to the operation, but don’t use it to process the results of the operation. The handler you specify should manage any failures, whether due to an error or an explicit cancellation.

## Topics

### Initializing the Zone Fetch Operation
- [convenience init(recordZoneIDs: [CKRecordZone.ID])](ckfetchrecordzonesoperation/init(recordzoneids:).md)
  Creates an operation for fetching the specified record zones.
- [init()](ckfetchrecordzonesoperation/init.md)
  Creates an empty fetch zones operation.
### Getting All Record Zones
- [class func fetchAllRecordZonesOperation() -> Self](ckfetchrecordzonesoperation/fetchallrecordzonesoperation.md)
  Returns an operation for fetching all record zones in the current database.
### Configuring a Zone Fetch Operation
- [var recordZoneIDs: [CKRecordZone.ID]?](ckfetchrecordzonesoperation/recordzoneids.md)
  The IDs of the record zones to retrieve.
### Processing Zone Fetch Results
- [var fetchRecordZonesCompletionBlock: (([CKRecordZone.ID : CKRecordZone]?, (any Error)?) -> Void)?](ckfetchrecordzonesoperation/fetchrecordzonescompletionblock.md)
  The closure to execute after CloudKit retrieves all of the record zones.
### Instance Properties
- [var fetchRecordZonesResultBlock: ((Result<Void, any Error>) -> Void)?](ckfetchrecordzonesoperation/fetchrecordzonesresultblock.md)
- [var perRecordZoneResultBlock: ((CKRecordZone.ID, Result<CKRecordZone, any Error>) -> Void)?](ckfetchrecordzonesoperation/perrecordzoneresultblock.md)

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

- [class CKFetchRecordsOperation](ckfetchrecordsoperation.md)
  An operation for retrieving records from a database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation)*