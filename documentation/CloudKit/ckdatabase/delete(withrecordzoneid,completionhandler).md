# delete(withRecordZoneID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Deletes a specific record zone.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func delete(withRecordZoneID zoneID: CKRecordZone.ID, completionHandler: @escaping @Sendable (CKRecordZone.ID?, (any Error)?) -> Void)
```

```swift
func delete(withRecordZoneID zoneID: CKRecordZone.ID) async throws -> CKRecordZone.ID
```

```objc
- (void) deleteRecordZoneWithID:(CKRecordZoneID *) zoneID completionHandler:(void (^)(CKRecordZoneID *zoneID, NSError *error)) completionHandler;
```

#### Discussion

> ⚠️ **Warning**: Deleting a record zone is a permanent action that deletes every record in that zone. You can’t restore a deleted record zone.

The completion handler takes the following parameters:

- The identifier of the deleted record zone, or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully deletes the record zone.

For information on a more convenient way to delete record zones, see [`modifyRecordZones(saving:deleting:)`](./modifyrecordzones%28saving,deleting%29.md).

## Parameters

- `zoneID`: The identifier of the record zone to delete.
- `completionHandler`: The closure to execute after CloudKit deletes the record zone.

## See Also

### Modifying Record Zones
- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID]) async throws -> (saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>])](./modifyrecordzones%28saving,deleting%29.md)
  Modifies the specified record zones and returns the results to an awaiting caller.
- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID], completionHandler: (Result<(saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>]), any Error>) -> Void)](./modifyrecordzones%28saving,deleting,completionhandler%29.md)
  Modifies the specified record zones and delivers the results to a completion handler.
- [func save(CKRecordZone, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](./save%28_,completionhandler%29-32ffr.md)
  Saves a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/delete(withrecordzoneid:completionhandler:))*