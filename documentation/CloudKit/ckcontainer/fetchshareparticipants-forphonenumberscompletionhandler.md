# fetchShareParticipants(forPhoneNumbers:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches share participants with the specified phone numbers.

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
@preconcurrency
func fetchShareParticipants(forPhoneNumbers phoneNumbers: [String], completionHandler: @escaping @Sendable (Result<[String : Result<CKShare.Participant, any Error>], any Error>) -> Void)
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- A dictionary of fetched share participants. The dictionary uses the phone numbers you specify in `phoneNumbers` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either the corresponding fetched share participant, or an error that describes why CloudKit can’t fetch that share participant.

CloudKit can translate any valid phone number into a share participant. If the phone number doesn’t correspond to a known iCloud account, then at share-accept-time, CloudKit offers the accepting participant a vetting process. The accepting participant uses this vetting process to link the phone number to an iCloud account.

This method searches for share participants asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) and configure it to use the necessary priority.

## Parameters

- `phoneNumbers`: The share participants’ phone numbers.
- `completionHandler`: The handler to execute with the fetch results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchshareparticipants(forphonenumbers:completionhandler:))*