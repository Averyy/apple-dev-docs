# discoverUserIdentity(withUserRecordID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches the user identity for the specified user record ID.

**Availability**:
- iOS 10.0+ - Deprecated in 17.0
- iPadOS 10.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.12+ - Deprecated in 14.0
- tvOS 10.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
func discoverUserIdentity(withUserRecordID userRecordID: CKRecord.ID, completionHandler: @escaping @Sendable (CKUserIdentity?, (any Error)?) -> Void)
```

```objc
- (void) discoverUserIdentityWithUserRecordID:(CKRecordID *) userRecordID completionHandler:(void (^)(CKUserIdentity *userInfo, NSError *error)) completionHandler;
```

#### Discussion

This closure doesn’t return a value and takes the following parameters:

- The user identity for the user record ID, or `nil` if CloudKit can’t find an identity.
- An error if a problem occurs, or `nil` if CloudKit successfully fetches a user identity.

Use this method to retrieve the identity of a user who you already have a user record ID for. The user you’re searching for must meet the following criteria:

- The user has run the app.
- The user grants the [`userDiscoverability`](./applicationpermissions/userdiscoverability.md) permission for the container.

This method searches for the user asynchronously and with a low priority. If you want the task to execute the request with a higher priority, create an instance of [`CKDiscoverUserIdentitiesOperation`](../ckdiscoveruseridentitiesoperation.md) and configure it to use the necessary priority.

## Parameters

- `userRecordID`: The user record’s ID.
- `completionHandler`: The handler to execute with the fetch results.

## See Also

### Discovering User Records
- [func discoverAllIdentities(completionHandler: ([CKUserIdentity]?, (any Error)?) -> Void)](./discoverallidentities%28completionhandler%29.md)
  Fetches all user identities that match entries in the user’s Contacts.
- [func discoverUserIdentity(withEmailAddress: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](./discoveruseridentity%28withemailaddress,completionhandler%29.md)
  Fetches the user identity for the specified email address.
- [func discoverUserIdentity(withPhoneNumber: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](./discoveruseridentity%28withphonenumber,completionhandler%29.md)
  Fetches the user identity for the specified phone number.
- [func fetchShareParticipant(withEmailAddress: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](./fetchshareparticipant%28withemailaddress,completionhandler%29.md)
  Fetches the share participant with the specified email address.
- [func fetchShareParticipant(withPhoneNumber: String, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](./fetchshareparticipant%28withphonenumber,completionhandler%29.md)
  Fetches the share participant with the specified phone number.
- [func fetchShareParticipant(withUserRecordID: CKRecord.ID, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](./fetchshareparticipant%28withuserrecordid,completionhandler%29.md)
  Fetches the share participant with the specified user record ID.
- [func fetchUserRecordID(completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](./fetchuserrecordid%28completionhandler%29.md)
  Fetches the user record ID of the current user.
- [let CKCurrentUserDefaultName: String](../ckcurrentuserdefaultname.md)
  A constant that provides the current user’s default name.
- [let CKOwnerDefaultName: String](../ckownerdefaultname.md)
  A constant that provides the default owner’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/discoveruseridentity(withuserrecordid:completionhandler:))*