# init(phoneNumber:)

**Framework**: CloudKit  
**Kind**: init

Creates a lookup info for the specified phone number.

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
init(phoneNumber: String)
```

#### Discussion

After you create a lookup info, use the [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md) operation or the  [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md) operation to retrieve the corresponding user identity.

## Parameters

- `phoneNumber`: The phone number for looking up the user identity.

## See Also

- [init(emailAddress: String)](ckuseridentity/lookupinfo-swift.class/init(emailaddress:).md)
  Creates a lookup info for the specified email address.
- [init(userRecordID: CKRecord.ID)](ckuseridentity/lookupinfo-swift.class/init(userrecordid:).md)
  Creates a lookup info for the specified user record ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class/init(phonenumber:))*