# fetch(withRecordZoneIDs:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches the specified record zones and delivers them to a completion handler.

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
@preconcurrency
func fetch(withRecordZoneIDs zoneIDs: [CKRecordZone.ID], completionHandler: @escaping @Sendable (Result<[CKRecordZone.ID : Result<CKRecordZone, any Error>], any Error>) -> Void)
```

#### Discussion

The completion handler takes the following parameters:

- A [`Result`](../../Swift/result.md) that contains either a dictionary of fetched record zones, or an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account. When present, the dictionary uses the identifiers you specify in `zoneIDs` as its keys. The value of each key is a [`Result`](../../Swift/result.md) that contains either the corresponding fetched record zone, or an error that describes why CloudKit can’t provide that record zone.

For information on a more configurable way to fetch specific record zones, see [`CKFetchRecordZonesOperation`](../ckfetchrecordzonesoperation.md).

## Parameters

- `zoneIDs`: The identifiers of the record zones to fetch.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

### Fetching Record Zones
- [func recordZones(for: [CKRecordZone.ID]) async throws -> [CKRecordZone.ID : Result<CKRecordZone, any Error>]](./recordzones%28for%29.md)
  Fetches the specified record zones and returns them to an awaiting caller.
- [func fetchAllRecordZones(completionHandler: ([CKRecordZone]?, (any Error)?) -> Void)](./fetchallrecordzones%28completionhandler%29.md)
  Fetches all record zones from the current database.
- [func fetch(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](./fetch%28withrecordzoneid,completionhandler%29.md)
  Fetches a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withrecordzoneids:completionhandler:))*