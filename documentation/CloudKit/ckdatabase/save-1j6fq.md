# save(_:)

**Framework**: CloudKit  
**Kind**: method

Saves a specific record.

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
func save(_ record: CKRecord) async throws -> CKRecord
```

#### Return Value

The saved record (as it appears on the server)

#### Discussion

The save succeeds only when the specified record is new, or is a more recent version than the one on the server.

For information on a more convenient way to save records, see [`modifyRecords(saving:deleting:savePolicy:atomically:)`](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:).md).

## Parameters

- `record`: The record to save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/save(_:)-1j6fq)*