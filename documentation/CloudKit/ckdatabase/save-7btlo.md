# save(_:)

**Framework**: CloudKit  
**Kind**: method

Saves a specific record zone.

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
func save(_ zone: CKRecordZone) async throws -> CKRecordZone
```

#### Return Value

The saved record zone (as it appears on the server).

#### Discussion

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account.

For information on a more convenient way to save record zones, see [`modifyRecordZones(saving:deleting:)`](ckdatabase/modifyrecordzones(saving:deleting:).md).

## Parameters

- `zone`: The record zone to save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/save(_:)-7btlo)*