# discoverAllIdentities(completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches all user identities that match entries in the user’s Contacts.

**Availability**:
- iOS 10.0+ - Deprecated in 17.0
- iPadOS 10.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.12+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
func discoverAllIdentities(completionHandler: @escaping @Sendable ([CKUserIdentity]?, (any Error)?) -> Void)
```

```objc
- (void) discoverAllIdentitiesWithCompletionHandler:(void (^)(NSArray<CKUserIdentity *> *userIdentities, NSError *error)) completionHandler;
```

## Discussion

The closure doesn’t return a value and takes the following parameters:

- The user identities that match entries in the user’s Contacts.
- An error if a problem occurs, or `nil` if the system successfully completes the request.

This method searches for the users asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKDiscoverAllUserIdentitiesOperation`](../ckdiscoveralluseridentitiesoperation.md) and configure it to use the necessary priority.

## Parameters

- `completionHandler`: The handler to execute with the fetch results.

## See Also

### Discovering User Records
- [func discoverUserIdentity(withEmailAddress: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](./discoveruseridentity%28withemailaddress,completionhandler%29.md)
  Fetches the user identity for the specified email address.
- [func discoverUserIdentity(withPhoneNumber: String, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](./discoveruseridentity%28withphonenumber,completionhandler%29.md)
  Fetches the user identity for the specified phone number.
- [func discoverUserIdentity(withUserRecordID: CKRecord.ID, completionHandler: (CKUserIdentity?, (any Error)?) -> Void)](./discoveruseridentity%28withuserrecordid,completionhandler%29.md)
  Fetches the user identity for the specified user record ID.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/discoverallidentities(completionhandler:))*