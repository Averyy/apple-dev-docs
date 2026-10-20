# CKUserIdentity.LookupInfo

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface CKUserIdentityLookupInfo : NSObject
```

#### Overview

Use this object when you want to discover the identities of your app’s users with [`CKDiscoverUserIdentitiesOperation`](../ckdiscoveruseridentitiesoperation.md), or to create a share’s participants with [`CKFetchShareParticipantsOperation`](../ckfetchshareparticipantsoperation.md).

You create individual instances by providing an email address, phone number, or user record ID. Alternatively, create an array of objects all at once by using one of the convenience methods, such as [`lookupInfos(withEmails:)`](./lookupinfo-swift.class/lookupinfos%28withemails%29.md).

## Topics

### Creating a Lookup Info
- [init(emailAddress: String)](./lookupinfo-swift.class/init%28emailaddress%29.md)
  Creates a lookup info for the specified email address.
- [init(phoneNumber: String)](./lookupinfo-swift.class/init%28phonenumber%29.md)
  Creates a lookup info for the specified phone number.
- [init(userRecordID: CKRecord.ID)](./lookupinfo-swift.class/init%28userrecordid%29.md)
  Creates a lookup info for the specified user record ID.
### Creating Multiple Lookup Infos
- [class func lookupInfos(withEmails: [String]) -> [CKUserIdentity.LookupInfo]](./lookupinfo-swift.class/lookupinfos%28withemails%29.md)
  Returns an array of lookup infos for the specified email addresses.
- [class func lookupInfos(withPhoneNumbers: [String]) -> [CKUserIdentity.LookupInfo]](./lookupinfo-swift.class/lookupinfos%28withphonenumbers%29.md)
  Returns an array of lookup infos for the specified phone numbers.
- [class func lookupInfos(with: [CKRecord.ID]) -> [CKUserIdentity.LookupInfo]](./lookupinfo-swift.class/lookupinfos%28with%29.md)
  Returns an array of lookup infos for the specified user record IDs.
### Accessing the Criteria
- [var emailAddress: String?](./lookupinfo-swift.class/emailaddress.md)
  The user’s email address.
- [var phoneNumber: String?](./lookupinfo-swift.class/phonenumber.md)
  The user’s phone number.
- [var userRecordID: CKRecord.ID?](./lookupinfo-swift.class/userrecordid.md)
  The ID of the user record.
### Initializers
- [init?(coder: NSCoder)](./lookupinfo-swift.class/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### User discovery
- [class CKUserIdentity](../ckuseridentity.md)
  The identity of a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity/lookupinfo-swift.class)*