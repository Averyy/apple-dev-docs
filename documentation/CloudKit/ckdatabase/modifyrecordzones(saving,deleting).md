# modifyRecordZones(saving:deleting:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Modifies the specified record zones and returns the results to an awaiting caller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
func modifyRecordZones(saving recordZonesToSave: [CKRecordZone], deleting recordZoneIDsToDelete: [CKRecordZone.ID]) async throws -> (saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>])
```

## Return Value

A tuple with the following named elements:

- **`saveResults`**: A dictionary of saved record zones. The dictionary uses the identifiers of the record zones you specify in `recordZonesToSave` as its keys. The value of each key is a [`Result`](../../Swift/result.md) that contains either the corresponding modified record zone (as it appears on the server), or an error that describes why CloudKit can’t modify that record zone.
- **`deleteResults`**: A dictionary of deleted record zones. The dictionary uses the identifiers you specify in `recordZoneIDsToDelete` as its keys. The value of each key is a [`Result`](../../Swift/result.md) that contains either [`Void`](../../Swift/void.md) to indicate a successful deletion, or an error that describes why CloudKit can’t delete that record zone.

## Discussion

> ⚠️ **Warning**: Deleting a record zone is a permanent action that deletes every record in that zone. You can’t restore a deleted record zone.

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account; otherwise, the returned tuple includes any individual record zone errors.

For information on a more configurable way to modify record zones, see [`CKModifyRecordZonesOperation`](../ckmodifyrecordzonesoperation.md).

## Parameters

- `recordZonesToSave`: The record zones to save.
- `recordZoneIDsToDelete`: The identifiers of the record zones to permanently delete.

## See Also

### Modifying Record Zones
- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID], completionHandler: (Result<(saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>]), any Error>) -> Void)](./modifyrecordzones%28saving,deleting,completionhandler%29.md)
  Modifies the specified record zones and delivers the results to a completion handler.
- [func save(CKRecordZone, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](./save%28_,completionhandler%29-32ffr.md)
  Saves a specific record zone.
- [func delete(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone.ID?, (any Error)?) -> Void)](./delete%28withrecordzoneid,completionhandler%29.md)
  Deletes a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/modifyrecordzones(saving:deleting:))*