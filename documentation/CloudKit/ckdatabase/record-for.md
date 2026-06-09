# record(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches a specific record.

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
func record(for recordID: CKRecord.ID) async throws -> CKRecord
```

#### Return Value

The requested record.

#### Discussion

This method throws an error if the record cannot be found or if request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account.

For information on a more convenient way to fetch specific records, see [`records(for:desiredKeys:)`](ckdatabase/records(for:desiredkeys:).md).

## Parameters

- `recordID`: The identifier of the record to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/record(for:))*