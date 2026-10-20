# CKOwnerDefaultName

**Framework**: CloudKit  
**Kind**: var  
**Role**: Global Variable

A constant that provides the default owner’s name.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0 (renamed: CKCurrentUserDefaultName)
- iPadOS 8.0+ - Deprecated in 10.0 (renamed: CKCurrentUserDefaultName)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: CKCurrentUserDefaultName)
- macOS 10.10+ - Deprecated in 10.12 (renamed: CKCurrentUserDefaultName)
- tvOS 9.0+ - Deprecated in 10.0 (renamed: CKCurrentUserDefaultName)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: CKCurrentUserDefaultName)
- watchOS 3.0+ - Deprecated in 3.0 (renamed: CKCurrentUserDefaultName)

## Declaration

```swift
let CKOwnerDefaultName: String
```

```c
extern NSString * const CKOwnerDefaultName;
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
- [let CKCurrentUserDefaultName: String](./ckcurrentuserdefaultname.md)
  A constant that provides the current user’s default name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckownerdefaultname)*