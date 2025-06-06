# CBIdentity

**Framework**: Collaboration  
**Kind**: class

A `CBIdentity` object is used for accessing the attributes of an identity stored in an identity authority. You can use an identity object for finding identities, and storing them in an access control list (ACL). If you need to edit these attributes, take advantage of the `CSIdentity` class in Core Services.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class CBIdentity
```

#### Overview

You can obtain a `CBIdentity` object from one of the following class factory methods: [`init(name:authority:)`](cbidentity/init(name:authority:).md), [`init(uuidString:authority:)`](cbidentity/init(uuidstring:authority:).md), [`init(persistentReference:)`](cbidentity/init(persistentreference:).md), or [`identityWithCSIdentity:`](cbidentity/identitywithcsidentity:.md).

A `CBIdentity` object has methods to support for interoperability with the Core Services Identity API. Send [`CSIdentity`](cbidentity/csidentity.md) to your `CBIdentity` object to return an opaque object for use in the Core Services Identity API. Similarly, call [`identityWithCSIdentity:`](cbidentity/identitywithcsidentity:.md) to use an Core Services Identity opaque object in the Collaboration framework.

There are two subclasses of `CBIdentity`: `CBGroupIdentity` and `CBUserIdentity`. If you are working specifically with a group identity, use `CBGroupIdentity`. Similarly, if you are working with a user identity, use `CBUserIdentity`.

## Topics

### Finding Identities
- [init?(name: String, authority: CBIdentityAuthority)](cbidentity/init(name:authority:).md)
  Returns the identity object with the given name from the specified identity authority.
- [init?(persistentReference: Data)](cbidentity/init(persistentreference:).md)
  Returns the identity object matching the persistent reference data.
- [init?(uuidString: String, authority: CBIdentityAuthority)](cbidentity/init(uuidstring:authority:).md)
  Returns the identity object with the given UUID from the specified identity authority.
### Getting Identity Attributes
- [var aliases: [String]](cbidentity/aliases.md)
  Returns an array of aliases (alternate names) for the identity.
- [var authority: CBIdentityAuthority](cbidentity/authority.md)
  Returns the identity authority where the identity is stored.
- [var emailAddress: String?](cbidentity/emailaddress.md)
  Returns the email address of an identity.
- [var fullName: String](cbidentity/fullname.md)
  Returns the full name of the identity.
- [var image: NSImage?](cbidentity/image.md)
  Returns the image associated with an identity.
- [var isHidden: Bool](cbidentity/ishidden.md)
  Returns a Boolean value indicating the state of the identity’s hidden property.
- [func isMember(ofGroup: CBGroupIdentity) -> Bool](cbidentity/ismember(ofgroup:).md)
  Returns a Boolean value indicating whether the identity is a member of the specified group.
- [var posixName: String](cbidentity/posixname.md)
  Returns the POSIX name of the identity.
- [var uuidString: String](cbidentity/uuidstring.md)
  Returns the UUID of the identity as a string.
### Storing Identities
- [var persistentReference: Data?](cbidentity/persistentreference.md)
  Returns a persistent reference to store a reference to an identity.
### Initializers
- [init?(uniqueIdentifier: UUID, authority: CBIdentityAuthority)](cbidentity/init(uniqueidentifier:authority:).md)
### Instance Properties
- [var uniqueIdentifier: UUID](cbidentity/uniqueidentifier.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CBGroupIdentity](cbgroupidentity.md)
- [CBUserIdentity](cbuseridentity.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity)*