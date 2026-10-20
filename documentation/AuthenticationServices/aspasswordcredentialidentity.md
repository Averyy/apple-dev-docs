# ASPasswordCredentialIdentity

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A description that uniquely identifies a particular password credential.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class ASPasswordCredentialIdentity
```

```objc
@interface ASPasswordCredentialIdentity : NSObject
```

## Topics

### Creating a credential identity
- [init(serviceIdentifier: ASCredentialServiceIdentifier, user: String, recordIdentifier: String?)](./aspasswordcredentialidentity/init%28serviceidentifier,user,recordidentifier%29.md)
  Initializes a password credential identity.
- [class ASCredentialServiceIdentifier](./ascredentialserviceidentifier.md)
  An identifier representing a particular service for which the user needs a credential, like a web site.
### Ordering credential identities
- [var rank: Int](./aspasswordcredentialidentity/rank.md)
  An indicator that enables you to prioritze credential identities relative to each other.
### Associating a user
- [var user: String](./aspasswordcredentialidentity/user.md)
  The username associated with the credential.
### Distinguishing identities
- [var recordIdentifier: String?](./aspasswordcredentialidentity/recordidentifier.md)
  A string used to correlate this identity to a record in your app’s own database.
- [var serviceIdentifier: ASCredentialServiceIdentifier](./aspasswordcredentialidentity/serviceidentifier.md)
  An identifier that helps the system know with which apps or websites to associate this credential.
### Initializers
- [init?(coder: NSCoder)](./aspasswordcredentialidentity/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASCredentialIdentity](./ascredentialidentity.md)
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

### Adding and removing credential identities
- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./ascredentialidentitystore/savecredentialidentities%28_,completion%29-1bbx6.md)
  Save the supplied credential identities to the store.
- [func replaceCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./ascredentialidentitystore/replacecredentialidentities%28_,completion%29.md)
  Replaces existing credential identities with new credential identities.
- [func removeAllCredentialIdentities(((Bool, (any Error)?) -> Void)?)](./ascredentialidentitystore/removeallcredentialidentities%28_%29.md)
  Removes all existing credential identities from the store.
- [func removeCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./ascredentialidentitystore/removecredentialidentities%28_,completion%29-67lcw.md)
  Remove the given credential identities from the store.
- [protocol ASCredentialIdentity](./ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](./aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredentialidentity)*