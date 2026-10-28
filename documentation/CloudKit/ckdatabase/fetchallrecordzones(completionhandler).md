# fetchAllRecordZones(completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches all record zones from the current database.

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
func fetchAllRecordZones(completionHandler: @escaping @Sendable ([CKRecordZone]?, (any Error)?) -> Void)
```

```objc
- (void) fetchAllRecordZonesWithCompletionHandler:(void (^)(NSArray<CKRecordZone *> *zones, NSError *error)) completionHandler;
```

## Discussion

The completion handler takes the following parameters:

- An array of fetched record zones, or `nil` if there’s an error. When present, the array contains at least one record zone, the default zone.
- An error if a problem occurs, or `nil` if CloudKit successfully fetches all record zones.

## Parameters

- `completionHandler`: The closure to execute with the fetch results.

## See Also

### Fetching Record Zones
- [func recordZones(for: [CKRecordZone.ID]) async throws -> [CKRecordZone.ID : Result<CKRecordZone, any Error>]](./recordzones%28for%29.md)
  Fetches the specified record zones and returns them to an awaiting caller.
- [func fetch(withRecordZoneIDs: [CKRecordZone.ID], completionHandler: (Result<[CKRecordZone.ID : Result<CKRecordZone, any Error>], any Error>) -> Void)](./fetch%28withrecordzoneids,completionhandler%29.md)
  Fetches the specified record zones and delivers them to a completion handler.
- [func fetch(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](./fetch%28withrecordzoneid,completionhandler%29.md)
  Fetches a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetchallrecordzones(completionhandler:))*