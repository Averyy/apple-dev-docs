# fetchUserRecordID(completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the user record ID of the current user.

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
func userRecordID() async throws -> CKRecord.ID
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The user record ID, or `nil` if the user disables iCloud Drive or the device doesn’t have an iCloud account.
- An error if a problem occurs, or `nil` if CloudKit successfully retrieves the user record ID.

CloudKit returns a [`CKError.Code.notAuthenticated`](ckerror/code/notauthenticated.md) error when any of the following conditions are met:

- The device has an iCloud account but the user disables iCloud Drive.
- The device has an iCloud account with restricted access.
- The device doesn’t have an iCloud account.

> **Note**:  At startup, fetching the user record ID may take longer while CloudKit makes the initial iCloud account request. After the initial fetch, accessing the ID generally takes less time.

## Parameters

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
- [func fetchShareParticipant(withEmailAddress: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withemailaddress:completionhandler:).md)
  Fetches the share participant with the specified email address.
- [func fetchShareParticipant(withPhoneNumber: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withphonenumber:completionhandler:).md)
  Fetches the share participant with the specified phone number.
- [func fetchShareParticipant(withUserRecordID: CKRecord.ID, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](ckcontainer/fetchshareparticipant(withuserrecordid:completionhandler:).md)
  Fetches the share participant with the specified user record ID.
- [let CKCurrentUserDefaultName: String](ckcurrentuserdefaultname.md)
  A constant that provides the current user’s default name.
- [let CKOwnerDefaultName: String](ckownerdefaultname.md)
  A constant that provides the default owner’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchuserrecordid(completionhandler:))*