# save(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Saves a specific record zone.

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
func save(_ zone: CKRecordZone, completionHandler: @escaping @Sendable (CKRecordZone?, (any Error)?) -> Void)
```

```objc
- (void) saveRecordZone:(CKRecordZone *) zone completionHandler:(void (^)(CKRecordZone *zone, NSError *error)) completionHandler;
```

#### Discussion

The completion handler takes the following parameters:

- The saved record zone (as it appears on the server), or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully saves the record zone.

For information on a more convenient way to save record zones, see [`modifyRecordZones(saving:deleting:)`](./modifyrecordzones%28saving,deleting%29.md).

## Parameters

- `zone`: The record zone to save.
- `completionHandler`: The closure to execute after CloudKit saves the record.

## See Also

### Modifying Record Zones
- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID]) async throws -> (saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>])](./modifyrecordzones%28saving,deleting%29.md)
  Modifies the specified record zones and returns the results to an awaiting caller.
- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID], completionHandler: (Result<(saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>]), any Error>) -> Void)](./modifyrecordzones%28saving,deleting,completionhandler%29.md)
  Modifies the specified record zones and delivers the results to a completion handler.
- [func delete(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone.ID?, (any Error)?) -> Void)](./delete%28withrecordzoneid,completionhandler%29.md)
  Deletes a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/save(_:completionhandler:)-32ffr)*