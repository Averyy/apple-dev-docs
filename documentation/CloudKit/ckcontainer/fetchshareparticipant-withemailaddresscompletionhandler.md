# fetchShareParticipant(withEmailAddress:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the share participant with the specified email address.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func shareParticipant(forEmailAddress emailAddress: String) async throws -> CKShare.Participant
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The share participant, or `nil` if CloudKit can’t find the participant.
- An error if a problem occurs, or `nil` if CloudKit successfully retrieves the participant.

This method searches for the share participant asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) and configure it to use the necessary priority.

## Parameters

- `emailAddress`: The share participant’s email address.
- `completionHandler`: The handler to execute with the fetch results.

## See Also

- [func discoverAllIdentities(completionHandler: ([CKUserIdentity]?, (any Error)?) -> Void)](ckcontainer/discoverallidentities(completionhandler:).md)
  Fetches all user identities that match entries in the user’s Contacts.
- [func discoverUserIdentity(withEmailAddress: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](ckcontainer/discoveruseridentity(withemailaddress:completionhandler:).md)
  Fetches the user identity for the specified email address.
- [func discoverUserIdentity(withPhoneNumber: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](ckcontainer/discoveruseridentity(withphonenumber:completionhandler:).md)
  Fetches the user identity for the specified phone number.
- [func discoverUserIdentity(withUserRecordID: CKRecord.ID, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](ckcontainer/discoveruseridentity(withuserrecordid:completionhandler:).md)
  Fetches the user identity for the specified user record ID.
- [func fetchShareParticipant(withPhoneNumber: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withphonenumber:completionhandler:).md)
  Fetches the share participant with the specified phone number.
- [func fetchShareParticipant(withUserRecordID: CKRecord.ID, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withuserrecordid:completionhandler:).md)
  Fetches the share participant with the specified user record ID.
- [func fetchUserRecordID(completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](ckcontainer/fetchuserrecordid(completionhandler:).md)
  Fetches the user record ID of the current user.
- [let CKCurrentUserDefaultName: String](ckcurrentuserdefaultname.md)
  A constant that provides the current user’s default name.
- [let CKOwnerDefaultName: String](ckownerdefaultname.md)
  A constant that provides the default owner’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchshareparticipant(withemailaddress:completionhandler:))*