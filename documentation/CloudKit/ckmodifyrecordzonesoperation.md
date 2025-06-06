# CKModifyRecordZonesOperation

**Framework**: CloudKit  
**Kind**: class

An operation that modifies one or more record zones.

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
class CKModifyRecordZonesOperation
```

## Mentions

- [Encrypting User Data](encrypting-user-data.md)
- [Responding to Requests to Delete Data](responding-to-requests-to-delete-data.md)

#### Overview

After you create one or more record zones, use this operation to save those zones to the database. You can also use the operation to delete record zones and their records.

If you assign a handler to the [`completionBlock`](https://developer.apple.com/documentation/foundation/operation/1408085-completionblock) property of the operation, CloudKit calls the handler after the operation executes and returns its results. Use the handler to perform housekeeping tasks for the operation, but don’t use it to process the results of the operation. The handler you provide should manage any failures of the operation, whether due to an error or an explicit cancellation.

## Topics

### Creating a Modify Zones Operation
- [convenience init(recordZonesToSave: [CKRecordZone]?, recordZoneIDsToDelete: [CKRecordZone.ID]?)](ckmodifyrecordzonesoperation/init(recordzonestosave:recordzoneidstodelete:).md)
  Creates an operation for modifying the specified record zones.
- [init()](ckmodifyrecordzonesoperation/init.md)
  Creates an empty modify record zones operation.
### Configuring the Modify Zones Operation
- [var recordZonesToSave: [CKRecordZone]?](ckmodifyrecordzonesoperation/recordzonestosave.md)
  The record zones to save to the database.
- [var recordZoneIDsToDelete: [CKRecordZone.ID]?](ckmodifyrecordzonesoperation/recordzoneidstodelete.md)
  The IDs of the record zones to delete permanently from the database.
### Processing the Modify Zones Results
- [var modifyRecordZonesCompletionBlock: (([CKRecordZone]?, [CKRecordZone.ID]?, (any Error)?) -> Void)?](ckmodifyrecordzonesoperation/modifyrecordzonescompletionblock.md)
  The closure to execute after CloudKit modifies all of the record zones.
### Instance Properties
- [var modifyRecordZonesResultBlock: ((Result<Void, any Error>) -> Void)?](ckmodifyrecordzonesoperation/modifyrecordzonesresultblock.md)
- [var perRecordZoneDeleteBlock: ((CKRecordZone.ID, Result<Void, any Error>) -> Void)?](ckmodifyrecordzonesoperation/perrecordzonedeleteblock-6c82y.md)
- [var perRecordZoneSaveBlock: ((CKRecordZone.ID, Result<CKRecordZone, any Error>) -> Void)?](ckmodifyrecordzonesoperation/perrecordzonesaveblock-1m45y.md)

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

- [class CKModifyRecordsOperation](ckmodifyrecordsoperation.md)
  An operation that modifies one or more records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation)*