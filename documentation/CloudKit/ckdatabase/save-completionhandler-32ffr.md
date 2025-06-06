# save(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Saves a specific record zone.

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
func save(_ zone: CKRecordZone) async throws -> CKRecordZone
```

#### Discussion

The completion handler takes the following parameters:

- The saved record zone (as it appears on the server), or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully saves the record zone.

For information on a more convenient way to save record zones, see [`modifyRecordZones(saving:deleting:)`](ckdatabase/modifyrecordzones(saving:deleting:).md).

## Parameters

- `zone`: The record zone to save.
- `completionHandler`: The closure to execute after CloudKit saves the record.

## See Also

- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID]) async throws -> (saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>])](ckdatabase/modifyrecordzones(saving:deleting:).md)
  Modifies the specified record zones and returns the results to an awaiting caller.
- [func modifyRecordZones(saving: [CKRecordZone], deleting: [CKRecordZone.ID], completionHandler: (Result<(saveResults: [CKRecordZone.ID : Result<CKRecordZone, any Error>], deleteResults: [CKRecordZone.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifyrecordzones(saving:deleting:completionhandler:).md)
  Modifies the specified record zones and delivers the results to a completion handler.
- [func delete(withRecordZoneID: CKRecordZone.ID, completionHandler: (CKRecordZone.ID?, (any Error)?) -> Void)](ckdatabase/delete(withrecordzoneid:completionhandler:).md)
  Deletes a specific record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/save(_:completionhandler:)-32ffr)*