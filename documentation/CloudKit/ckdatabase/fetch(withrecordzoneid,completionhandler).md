# fetch(withRecordZoneID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches a specific record zone.

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
func fetch(withRecordZoneID zoneID: CKRecordZone.ID, completionHandler: @escaping @Sendable (CKRecordZone?, (any Error)?) -> Void)
```

```swift
func fetch(withRecordZoneID zoneID: CKRecordZone.ID) async throws -> CKRecordZone
```

```objc
- (void) fetchRecordZoneWithID:(CKRecordZoneID *) zoneID completionHandler:(void (^)(CKRecordZone *zone, NSError *error)) completionHandler;
```

## Discussion

The completion handler takes the following parameters:

- The fetched record zone, or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully fetches the specified record zone.

For information on a more convenient way to fetch specific record zones, see [`recordZones(for:)`](./recordzones%28for%29.md) in Swift or [`CKFetchRecordZonesOperation`](../ckfetchrecordzonesoperation.md) in Objective-C.

## Parameters

- `zoneID`: The identifier of the record zone to fetch.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

### Fetching Record Zones
- [func recordZones(for: [CKRecordZone.ID]) async throws -> [CKRecordZone.ID : Result<CKRecordZone, any Error>]](./recordzones%28for%29.md)
  Fetches the specified record zones and returns them to an awaiting caller.
- [func fetch(withRecordZoneIDs: [CKRecordZone.ID], completionHandler: (Result<[CKRecordZone.ID : Result<CKRecordZone, any Error>], any Error>) -> Void)](./fetch%28withrecordzoneids,completionhandler%29.md)
  Fetches the specified record zones and delivers them to a completion handler.
- [func fetchAllRecordZones(completionHandler: ([CKRecordZone]?, (any Error)?) -> Void)](./fetchallrecordzones%28completionhandler%29.md)
  Fetches all record zones from the current database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withrecordzoneid:completionhandler:))*