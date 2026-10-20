# init(userRecordID:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a lookup info for the specified user record ID.

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
init(userRecordID: CKRecord.ID)
```

```objc
- (instancetype) initWithUserRecordID:(CKRecordID *) userRecordID;
```

#### Discussion

After you create a lookup info, use the [`CKDiscoverUserIdentitiesOperation`](../../ckdiscoveruseridentitiesoperation.md) operation or the  [`CKFetchShareParticipantsOperation`](../../ckfetchshareparticipantsoperation.md) operation to retrieve the corresponding user identity.

## Parameters

- `userRecordID`: The user record ID for looking up the user identity.

## See Also

### Creating a Lookup Info
- [init(emailAddress: String)](./init%28emailaddress%29.md)
  Creates a lookup info for the specified email address.
- [init(phoneNumber: String)](./init%28phonenumber%29.md)
  Creates a lookup info for the specified phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class/init(userrecordid:))*