# fetchShareParticipant(withUserRecordID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches the share participant with the specified user record ID.

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
func fetchShareParticipant(withUserRecordID userRecordID: CKRecord.ID, completionHandler: @escaping @Sendable (CKShare.Participant?, (any Error)?) -> Void)
```

```objc
- (void) fetchShareParticipantWithUserRecordID:(CKRecordID *) userRecordID completionHandler:(void (^)(CKShareParticipant *shareParticipant, NSError *error)) completionHandler;
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The share participant, or `nil` if CloudKit can’t find the participant.
- An error if a problem occurs, or `nil` if CloudKit successfully retrieves the participant.

This method searches for the share participant asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareParticipantsOperation`](../ckfetchshareparticipantsoperation.md) and configure it to use the necessary priority.

## Parameters

- `userRecordID`: The share participant’s user record ID.
- `completionHandler`: The handler to execute with the fetch results.

## See Also

### Discovering User Records
- [func discoverAllIdentities(completionHandler: ([CKUserIdentity]?, (any Error)?) -> Void)](./discoverallidentities%28completionhandler%29.md)
  Fetches all user identities that match entries in the user’s Contacts.
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
- [func fetchUserRecordID(completionHandler: (CKRecord.ID?, (any Error)?) -> Void)](./fetchuserrecordid%28completionhandler%29.md)
  Fetches the user record ID of the current user.
- [let CKCurrentUserDefaultName: String](../ckcurrentuserdefaultname.md)
  A constant that provides the current user’s default name.
- [let CKOwnerDefaultName: String](../ckownerdefaultname.md)
  A constant that provides the default owner’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchshareparticipant(withuserrecordid:completionhandler:))*