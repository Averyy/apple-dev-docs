# shareParticipant(forEmailAddress:)

**Framework**: CloudKit  
**Kind**: method

Fetches the share participant with the specified email address.

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
func shareParticipant(forEmailAddress email: String) async throws -> CKShare.Participant
```

#### Discussion

- Returns The share participant for the email address.

CloudKit can translate any valid email address into a share participant. If the email address doesn’t correspond to a known iCloud account, then at share-accept-time, CloudKit offers the accepting participant a vetting process. The accepting participant uses this vetting process to link the email address to an iCloud account.

This method searches for the share participant asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) and configure it to use the necessary priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/shareparticipant(foremailaddress:))*