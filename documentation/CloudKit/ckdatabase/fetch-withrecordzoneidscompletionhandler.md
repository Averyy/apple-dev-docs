# fetch(withRecordZoneIDs:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the specified record zones and delivers them to a completion handler.

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
func fetch(withRecordZoneIDs zoneIDs: [CKRecordZone.ID], completionHandler: @escaping (Result<[CKRecordZone.ID : Result<CKRecordZone, any Error>], any Error>) -> Void)
```

#### Discussion

The completion handler takes the following parameters:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either a dictionary of fetched record zones, or an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account. When present, the dictionary uses the identifiers you specify in `zoneIDs` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either the corresponding fetched record zone, or an error that describes why CloudKit can’t provide that record zone.

For information on a more configurable way to fetch specific record zones, see [`CKFetchRecordZonesOperation`](ckfetchrecordzonesoperation.md).

## Parameters

- `zoneIDs`: The identifiers of the record zones to fetch.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func recordZones(for: [CKRecordZone.ID]) async throws -> [CKRecordZone.ID : Result<CKRecordZone, any Error>]](ckdatabase/recordzones(for:).md)
  Fetches the specified record zones and returns them to an awaiting caller.
- [func fetchAllRecordZones(completionHandler: ([CKRecordZone]?, (any Error)?) -> Void)](ckdatabase/fetchallrecordzones(completionhandler:).md)
  Fetches all record zones from the current database.
- [func fetch(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](ckdatabase/fetch(withrecordzoneid:completionhandler:).md)
  Fetches a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withrecordzoneids:completionhandler:))*