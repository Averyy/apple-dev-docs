# CKOwnerDefaultName

**Framework**: CloudKit  
**Kind**: var

A constant that provides the default owner’s name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let CKOwnerDefaultName: String
```

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
- [func fetchUserRecordID(completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](ckcontainer/fetchuserrecordid(completionhandler:).md)
  Fetches the user record ID of the current user.
- [let CKCurrentUserDefaultName: String](ckcurrentuserdefaultname.md)
  A constant that provides the current user’s default name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckownerdefaultname)*