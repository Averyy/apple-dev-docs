# modifyRecordZones(saving:deleting:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Modifies the specified record zones and delivers the results to a completion handler.

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
func modifyRecordZones(saving recordZonesToSave: [CKRecordZone], deleting recordZoneIDsToDelete: [CKRecordZone.ID], completionHandler: @escaping (Result<(saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>]), any Error>) -> Void)
```

#### Discussion

> ⚠️ **Warning**:  Deleting a record zone is a permanent action that deletes every record in that zone. You can’t restore a deleted record zone.

The completion handler takes a single [`Result`](https://developer.apple.com/documentation/Swift/Result) parameter that contains either a tuple, or an error if the request fails. For example, when the network is unavailable or the device doesn’t have an active iCloud account.

When present, the tuple contains the following named elements:

For information on a more configurable way to modify record zones, see [`CKModifyRecordZonesOperation`](ckmodifyrecordzonesoperation.md).

## Parameters

- `recordZonesToSave`: The record zones to save.
- `recordZoneIDsToDelete`: The identifiers of the record zones to permanently delete.
- `completionHandler`: The closure to execute after CloudKit processes the changes.

## See Also

- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID]) async throws -> (saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>])](ckdatabase/modifyrecordzones(saving:deleting:).md)
  Modifies the specified record zones and returns the results to an awaiting caller.
- [func save(CKRecordZone, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-32ffr.md)
  Saves a specific record zone.
- [func delete(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone.ID?, (any Error)?) -> Void)](ckdatabase/delete(withrecordzoneid:completionhandler:).md)
  Deletes a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/modifyrecordzones(saving:deleting:completionhandler:))*