# ASPasswordCredentialIdentity

**Framework**: Authentication Services  
**Kind**: class

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

## Topics

### Creating a credential identity
- [init(serviceIdentifier: ASCredentialServiceIdentifier, user: String, recordIdentifier: String?)](aspasswordcredentialidentity/init(serviceidentifier:user:recordidentifier:).md)
  Initializes a password credential identity.
- [class ASCredentialServiceIdentifier](ascredentialserviceidentifier.md)
  An identifier representing a particular service for which the user needs a credential, like a web site.
### Ordering credential identities
- [var rank: Int](aspasswordcredentialidentity/rank.md)
  An indicator that enables you to prioritze credential identities relative to each other.
### Associating a user
- [var user: String](aspasswordcredentialidentity/user.md)
  The username associated with the credential.
### Distinguishing identities
- [var recordIdentifier: String?](aspasswordcredentialidentity/recordidentifier.md)
  A string used to correlate this identity to a record in your app’s own database.
- [var serviceIdentifier: ASCredentialServiceIdentifier](aspasswordcredentialidentity/serviceidentifier.md)
  An identifier that helps the system know with which apps or websites to associate this credential.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASCredentialIdentity](ascredentialidentity.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-1bbx6.md)
  Save the supplied credential identities to the store.
- [func replaceCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/replacecredentialidentities(_:completion:).md)
  Replaces existing credential identities with new credential identities.
- [func removeAllCredentialIdentities(((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removeallcredentialidentities(_:).md)
  Removes all existing credential identities from the store.
- [func removeCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removecredentialidentities(_:completion:)-67lcw.md)
  Remove the given credential identities from the store.
- [protocol ASCredentialIdentity](ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasswordcredentialidentity)*