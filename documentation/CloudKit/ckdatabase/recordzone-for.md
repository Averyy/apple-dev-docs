# recordZone(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches a specific record zone.

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
func recordZone(for zoneID: CKRecordZone.ID) async throws -> CKRecordZone
```

#### Return Value

The fetched record zone.

#### Discussion

This method throws an error if the request fails, such as when the zone does not exist, the network is unavailable or the device doesn’t have an active iCloud account.

For information on a more convenient way to fetch specific record zones, see [`recordZones(for:)`](ckdatabase/recordzones(for:).md).

## Parameters

- `zoneID`: The identifier of the record zone to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/recordzone(for:))*