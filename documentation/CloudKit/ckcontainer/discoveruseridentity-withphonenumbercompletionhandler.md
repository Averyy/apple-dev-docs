# discoverUserIdentity(withPhoneNumber:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the user identity for the specified phone number.

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
func userIdentity(forPhoneNumber phoneNumber: String) async throws -> CKUserIdentity?
```

#### Discussion

This closure doesn’t return a value and takes the following parameters:

- The user identity for the phone number, or `nil` if CloudKit can’t find an identity.
- An error if a problem occurs, or `nil` if CloudKit successfully fetches a user identity.

Use this method to retrieve the identity of a user who the current user knows. The user you’re searching for must meet the following criteria:

- The user must be in the current user’s Contacts.
- The user has run the app.
- The user grants the [`userDiscoverability`](ckcontainer/applicationpermissions/userdiscoverability.md) permission for the container.

This method searches for the user asynchronously and with a low priority. If you want the task to execute the request with a higher priority, create an instance of [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md) and configure it to use the necessary priority.

## Parameters

- `phoneNumber`: The user’s phone number.
- `completionHandler`: The handler to execute with the fetch results.

## See Also

- [func discoverAllIdentities(completionHandler: ([CKUserIdentity]?, (any Error)?) -> Void)](ckcontainer/discoverallidentities(completionhandler:).md)
  Fetches all user identities that match entries in the user’s Contacts.
- [func discoverUserIdentity(withEmailAddress: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](ckcontainer/discoveruseridentity(withemailaddress:completionhandler:).md)
  Fetches the user identity for the specified email address.
- [func discoverUserIdentity(withUserRecordID: CKRecord.ID, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](ckcontainer/discoveruseridentity(withuserrecordid:completionhandler:).md)
  Fetches the user identity for the specified user record ID.
- [func fetchShareParticipant(withEmailAddress: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withemailaddress:completionhandler:).md)
  Fetches the share participant with the specified email address.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/discoveruseridentity(withphonenumber:completionhandler:))*