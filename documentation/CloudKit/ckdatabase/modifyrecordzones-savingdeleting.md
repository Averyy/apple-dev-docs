# modifyRecordZones(saving:deleting:)

**Framework**: CloudKit  
**Kind**: method

Modifies the specified record zones and returns the results to an awaiting caller.

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
func modifyRecordZones(saving recordZonesToSave: [CKRecordZone], deleting recordZoneIDsToDelete: [CKRecordZone.ID]) async throws -> (saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>])
```

#### Return Value

A tuple with the following named elements:

#### Discussion

#### Discussion

> ⚠️ **Warning**:  Deleting a record zone is a permanent action that deletes every record in that zone. You can’t restore a deleted record zone.

 Deleting a record zone is a permanent action that deletes every record in that zone. You can’t restore a deleted record zone.

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account; otherwise, the returned tuple includes any individual record zone errors.

For information on a more configurable way to modify record zones, see [`CKModifyRecordZonesOperation`](ckmodifyrecordzonesoperation.md).

## Parameters

- `recordZonesToSave`: The record zones to save.
- `recordZoneIDsToDelete`: The identifiers of the record zones to permanently delete.

## See Also

- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID], completionHandler: (Result<(saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifyrecordzones(saving:deleting:completionhandler:).md)
  Modifies the specified record zones and delivers the results to a completion handler.
- [func save(CKRecordZone, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-32ffr.md)
  Saves a specific record zone.
- [func delete(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone.ID?, (any Error)?) -> Void)](ckdatabase/delete(withrecordzoneid:completionhandler:).md)
  Deletes a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/modifyrecordzones(saving:deleting:))*