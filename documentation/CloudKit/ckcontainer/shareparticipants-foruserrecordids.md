# shareParticipants(forUserRecordIDs:)

**Framework**: CloudKit  
**Kind**: method

Fetches share participants with the specified user record IDs and returns them to an awaiting caller.

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
func shareParticipants(forUserRecordIDs userRecordIDs: [CKRecord.ID]) async throws -> [CKRecord.ID : Result<CKShare.Participant, any Error>]
```

#### Return Value

A dictionary of fetched share participants. The dictionary uses the user record IDs you specify in `userRecordIDs` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/swift/result) that contains either the corresponding fetched share participant, or an error that describes why CloudKit can’t fetch that share participant.

#### Discussion

This method searches for share participants asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) and configure it to use the necessary priority.

## Parameters

- `userRecordIDs`: The share participants’ user record IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/shareparticipants(foruserrecordids:))*