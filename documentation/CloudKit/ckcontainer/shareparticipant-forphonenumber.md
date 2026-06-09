# shareParticipant(forPhoneNumber:)

**Framework**: CloudKit  
**Kind**: method

Fetches the share participant with the specified phone number.

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
func shareParticipant(forPhoneNumber phoneNumber: String) async throws -> CKShare.Participant
```

#### Return Value

The share participant for the phone number.

#### Discussion

CloudKit can translate any valid phone number into a share participant.  If the phone number doesn’t correspond to a known iCloud account, then at share-accept-time, CloudKit offers the accepting participant a vetting process. The accepting participant uses this vetting process to link the phone number to an iCloud account.

This method searches for the share participant asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) and configure it to use the necessary priority.

## Parameters

- `phoneNumber`: The share participant’s phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/shareparticipant(forphonenumber:))*