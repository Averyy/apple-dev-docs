# shareParticipant(forUserRecordID:)

**Framework**: CloudKit  
**Kind**: method

Fetches the share participant with the specified user record ID.

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
func shareParticipant(forUserRecordID userRecordID: CKRecord.ID) async throws -> CKShare.Participant
```

#### Discussion

- Returns The share participant for the user record ID.

This method searches for the share participant asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) and configure it to use the necessary priority.

## Parameters

- `userRecordID`: The share participant’s user record ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/shareparticipant(foruserrecordid:))*