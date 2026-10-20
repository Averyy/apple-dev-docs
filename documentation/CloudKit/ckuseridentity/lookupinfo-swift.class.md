# CKUserIdentity.LookupInfo

**Framework**: CloudKit  
**Kind**: class

The criteria to use when searching for discoverable iCloud users.

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
class LookupInfo
```

#### Overview

Use this object when you want to discover the identities of your app’s users with [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md), or to create a share’s participants with [`CKFetchShareParticipantsOperation`](ckfetchshareparticipantsoperation.md).

You create individual instances by providing an email address, phone number, or user record ID. Alternatively, create an array of objects all at once by using one of the convenience methods, such as [`lookupInfos(withEmails:)`](ckuseridentity/lookupinfo-swift.class/lookupinfos(withemails:).md).

## Topics

### Creating a Lookup Info
- [init(emailAddress: String)](ckuseridentity/lookupinfo-swift.class/init(emailaddress:).md)
  Creates a lookup info for the specified email address.
- [init(phoneNumber: String)](ckuseridentity/lookupinfo-swift.class/init(phonenumber:).md)
  Creates a lookup info for the specified phone number.
- [init(userRecordID: CKRecord.ID)](ckuseridentity/lookupinfo-swift.class/init(userrecordid:).md)
  Creates a lookup info for the specified user record ID.
### Creating Multiple Lookup Infos
- [class func lookupInfos(withEmails: [String]) -> [CKUserIdentity.LookupInfo]](ckuseridentity/lookupinfo-swift.class/lookupinfos(withemails:).md)
  Returns an array of lookup infos for the specified email addresses.
- [class func lookupInfos(withPhoneNumbers: [String]) -> [CKUserIdentity.LookupInfo]](ckuseridentity/lookupinfo-swift.class/lookupinfos(withphonenumbers:).md)
  Returns an array of lookup infos for the specified phone numbers.
- [class func lookupInfos(with: [CKRecord.ID]) -> [CKUserIdentity.LookupInfo]](ckuseridentity/lookupinfo-swift.class/lookupinfos(with:).md)
  Returns an array of lookup infos for the specified user record IDs.
### Accessing the Criteria
- [var emailAddress: String?](ckuseridentity/lookupinfo-swift.class/emailaddress.md)
  The user’s email address.
- [var phoneNumber: String?](ckuseridentity/lookupinfo-swift.class/phonenumber.md)
  The user’s phone number.
- [var userRecordID: CKRecord.ID?](ckuseridentity/lookupinfo-swift.class/userrecordid.md)
  The ID of the user record.
### Initializers
- [init?(coder: NSCoder)](ckuseridentity/lookupinfo-swift.class/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class CKUserIdentity](ckuseridentity.md)
  The identity of a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class)*