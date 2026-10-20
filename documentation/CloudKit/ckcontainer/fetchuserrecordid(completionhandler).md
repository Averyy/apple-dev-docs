# fetchUserRecordID(completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches the user record ID of the current user.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func fetchUserRecordID(completionHandler: @escaping @Sendable (CKRecord.ID?, (any Error)?) -> Void)
```

```swift
func userRecordID() async throws -> CKRecord.ID
```

```objc
- (void) fetchUserRecordIDWithCompletionHandler:(void (^)(CKRecordID *recordID, NSError *error)) completionHandler;
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The user record ID, or `nil` if the user disables iCloud or the device doesn’t have an iCloud account.
- An error if a problem occurs, or `nil` if CloudKit successfully retrieves the user record ID.

CloudKit returns a [`CKError.Code.notAuthenticated`](../ckerror/code/notauthenticated.md) error when any of the following conditions are met:

- The device has an iCloud account but the user disables iCloud.
- The device has an iCloud account with restricted access.
- The device doesn’t have an iCloud account.

> **Note**: At startup, fetching the user record ID may take longer while CloudKit makes the initial iCloud account request. After the initial fetch, accessing the ID generally takes less time.

## Parameters

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
- [func fetchShareParticipant(withUserRecordID: CKRecord.ID, completionHandler: (CKShare.Participant?, (any Error)?) -> Void)](./fetchshareparticipant%28withuserrecordid,completionhandler%29.md)
  Fetches the share participant with the specified user record ID.
- [let CKCurrentUserDefaultName: String](../ckcurrentuserdefaultname.md)
  A constant that provides the current user’s default name.
- [let CKOwnerDefaultName: String](../ckownerdefaultname.md)
  A constant that provides the default owner’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchuserrecordid(completionhandler:))*