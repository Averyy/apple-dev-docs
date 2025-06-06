# recordZones(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches the specified record zones and returns them to an awaiting caller.

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
func recordZones(for ids: [CKRecordZone.ID]) async throws -> [CKRecordZone.ID : Result<CKRecordZone, any Error>]
```

#### Return Value

A dictionary that contains the fetched record zones. The dictionary uses the specified record zone identifiers as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either the corresponding fetched record zone, or an error that describes why CloudKit can’t provide that record zone.

#### Discussion

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account; otherwise, the returned dictionary includes any individual record zone errors.

For information on a more configurable way to fetch specific record zones, see [`CKFetchRecordZonesOperation`](ckfetchrecordzonesoperation.md).

## Parameters

- `ids`: The identifiers of the record zones to fetch.

## See Also

- [func fetch(withRecordZoneIDs: [CKRecordZone.ID], completionHandler: (Result<[CKRecordZone.ID : Result<CKRecordZone, any Error>], any Error>) -> Void)](ckdatabase/fetch(withrecordzoneids:completionhandler:).md)
  Fetches the specified record zones and delivers them to a completion handler.
- [func fetchAllRecordZones(completionHandler: ([CKRecordZone]?, (any Error)?) -> Void)](ckdatabase/fetchallrecordzones(completionhandler:).md)
  Fetches all record zones from the current database.
- [func fetch(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone?, (any Error)?) -> Void)](ckdatabase/fetch(withrecordzoneid:completionhandler:).md)
  Fetches a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/recordzones(for:))*