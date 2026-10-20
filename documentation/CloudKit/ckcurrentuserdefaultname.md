# CKCurrentUserDefaultName

**Framework**: CloudKit  
**Kind**: var  
**Role**: Global Variable

A constant that provides the current user’s default name.

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
let CKCurrentUserDefaultName: String
```

```c
extern NSString * const CKCurrentUserDefaultName;
```

## See Also

### Discovering User Records
- [func discoverAllIdentities(completionHandler: ([CKUserIdentity]?, (any Error)?) -> Void)](./ckcontainer/discoverallidentities%28completionhandler%29.md)
  Fetches all user identities that match entries in the user’s Contacts.
- [func discoverUserIdentity(withEmailAddress: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](./ckcontainer/discoveruseridentity%28withemailaddress,completionhandler%29.md)
  Fetches the user identity for the specified email address.
- [func discoverUserIdentity(withPhoneNumber: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](./ckcontainer/discoveruseridentity%28withphonenumber,completionhandler%29.md)
  Fetches the user identity for the specified phone number.
- [func discoverUserIdentity(withUserRecordID: CKRecord.ID, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](./ckcontainer/discoveruseridentity%28withuserrecordid,completionhandler%29.md)
  Fetches the user identity for the specified user record ID.
- [func fetchShareParticipant(withEmailAddress: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](./ckcontainer/fetchshareparticipant%28withemailaddress,completionhandler%29.md)
  Fetches the share participant with the specified email address.
- [func fetchShareParticipant(withPhoneNumber: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](./ckcontainer/fetchshareparticipant%28withphonenumber,completionhandler%29.md)
  Fetches the share participant with the specified phone number.
- [func fetchShareParticipant(withUserRecordID: CKRecord.ID, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](./ckcontainer/fetchshareparticipant%28withuserrecordid,completionhandler%29.md)
  Fetches the share participant with the specified user record ID.
- [func fetchUserRecordID(completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](./ckcontainer/fetchuserrecordid%28completionhandler%29.md)
  Fetches the user record ID of the current user.
- [let CKOwnerDefaultName: String](./ckownerdefaultname.md)
  A constant that provides the default owner’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcurrentuserdefaultname)*