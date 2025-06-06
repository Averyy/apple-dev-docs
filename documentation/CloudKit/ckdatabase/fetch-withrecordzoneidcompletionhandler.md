# fetch(withRecordZoneID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches a specific record zone.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func recordZone(for zoneID: CKRecordZone.ID) async throws -> CKRecordZone
```

#### Discussion

The completion handler takes the following parameters:

- The fetched record zone, or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully fetches the specified record zone.

For information on a more convenient way to fetch specific record zones, see [`recordZones(for:)`](ckdatabase/recordzones(for:).md) in Swift or [`CKFetchRecordZonesOperation`](ckfetchrecordzonesoperation.md) in Objective-C.

## Parameters

- `zoneID`: The identifier of the record zone to fetch.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func recordZones(for: [CKRecordZone.ID]) async throws -> [CKRecordZone.ID : Result<CKRecordZone, any Error>]](ckdatabase/recordzones(for:).md)
  Fetches the specified record zones and returns them to an awaiting caller.
- [func fetch(withRecordZoneIDs: [CKRecordZone.ID], completionHandler: (Result<[CKRecordZone.ID : Result<CKRecordZone, any Error>], any Error>) -> Void)](ckdatabase/fetch(withrecordzoneids:completionhandler:).md)
  Fetches the specified record zones and delivers them to a completion handler.
- [func fetchAllRecordZones(completionHandler: ([CKRecordZone]?, (any Error)?) -> Void)](ckdatabase/fetchallrecordzones(completionhandler:).md)
  Fetches all record zones from the current database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withrecordzoneid:completionhandler:))*