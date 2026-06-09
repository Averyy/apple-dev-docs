# allRecordZones()

**Framework**: CloudKit  
**Kind**: method

Fetches all record zones from the current database.

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
func allRecordZones() async throws -> [CKRecordZone]
```

#### Return Value

An array of fetched record zones which contains at least one record zone, the default zone.

#### Discussion

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/allrecordzones())*