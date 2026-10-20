# init(emailAddress:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a lookup info for the specified email address.

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
init(emailAddress: String)
```

```objc
- (instancetype) initWithEmailAddress:(NSString *) emailAddress;
```

#### Discussion

After you create a lookup info, use the [`CKDiscoverUserIdentitiesOperation`](../../ckdiscoveruseridentitiesoperation.md) operation or the  [`CKFetchShareParticipantsOperation`](../../ckfetchshareparticipantsoperation.md) operation to retrieve the corresponding user identity.

## Parameters

- `emailAddress`: The email address for looking up the user identity.

## See Also

### Creating a Lookup Info
- [init(phoneNumber: String)](./init%28phonenumber%29.md)
  Creates a lookup info for the specified phone number.
- [init(userRecordID: CKRecord.ID)](./init%28userrecordid%29.md)
  Creates a lookup info for the specified user record ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class/init(emailaddress:))*