# CKUserIdentity

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

The identity of a user.

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
class CKUserIdentity
```

```objc
@interface CKUserIdentity : NSObject
```

#### Overview

A user identity provides identifiable data about an iCloud user, including their name, user record ID, and an email address or phone number. CloudKit retrieves this information from the user’s iCloud account. A user must give their consent to be discoverable before CloudKit can provide this data to your app. For more information, see [`requestApplicationPermission(_:completionHandler:)`](./ckcontainer/requestapplicationpermission%28_,completionhandler%29.md).

You don’t create instances of this class. Instead, CloudKit provides them in certain contexts. A share’s owner has a user identity, as does each of its participants. When creating participants, CloudKit tries to find iCloud accounts it can use to populate their identities. If CloudKit doesn’t find an account, it sets the identity’s [`hasiCloudAccount`](./ckuseridentity/hasicloudaccount.md) property to [`false`](../Swift/false.md).

You can also discover the identities of your app’s users by executing one of the user discovery operations: [`CKDiscoverAllUserIdentitiesOperation`](./ckdiscoveralluseridentitiesoperation.md) and [`CKDiscoverUserIdentitiesOperation`](./ckdiscoveruseridentitiesoperation.md). Identities that CloudKit discovers using [`CKDiscoverAllUserIdentitiesOperation`](./ckdiscoveralluseridentitiesoperation.md) correspond to entries in the device’s Contacts database. These identities contain the identifiers of their Contact records, which you can use to fetch those records from the Contacts database. For more information, see [`contactIdentifiers`](./ckuseridentity/contactidentifiers.md).

## Topics

### Accessing iCloud Information
- [var hasiCloudAccount: Bool](./ckuseridentity/hasicloudaccount.md)
  A Boolean value that indicates whether the user has an iCloud account.
- [var lookupInfo: CKUserIdentity.LookupInfo?](./ckuseridentity/lookupinfo-swift.property.md)
  The lookup info for retrieving the user identity.
- [CKUserIdentity.LookupInfo](./ckuseridentity/lookupinfo-swift.class.md)
  The criteria to use when searching for discoverable iCloud users.
### Accessing User Information
- [var userRecordID: CKRecord.ID?](./ckuseridentity/userrecordid.md)
  The user record ID for the corresponding user record.
- [var contactIdentifiers: [String]](./ckuseridentity/contactidentifiers.md)
  Identifiers that match contacts in the local Contacts database.
- [var nameComponents: PersonNameComponents?](./ckuseridentity/namecomponents.md)
  The user’s name.
### Initializers
- [init?(coder: NSCoder)](./ckuseridentity/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### User discovery
- [CKUserIdentity.LookupInfo](./ckuseridentity/lookupinfo-swift.class.md)
  The criteria to use when searching for discoverable iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckuseridentity)*