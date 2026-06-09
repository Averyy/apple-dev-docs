# deleteRecord(withID:)

**Framework**: CloudKit  
**Kind**: method

Deletes a specific record.

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
@discardableResult
func deleteRecord(withID recordID: CKRecord.ID) async throws -> CKRecord.ID
```

#### Return Value

The identifier of the deleted record.

#### Discussion

Deleting a record may cause additional deletions if other records in the database reference the deleted record. CloudKit doesn’t provide the identifiers of any additional records it deletes. This method throws an error if the request fails, such as when the records doesn’t exist, the network is unavailable or the device doesn’t have an active iCloud account.

For information on a more convenient way to delete records, see [`modifyRecords(saving:deleting:savePolicy:atomically:)`](ckdatabase/modifyrecords(saving:deleting:savepolicy:atomically:).md).

## Parameters

- `recordID`: The identifier of the record to delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/deleterecord(withid:))*