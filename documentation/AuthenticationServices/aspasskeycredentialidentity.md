# ASPasskeyCredentialIdentity

**Framework**: Authentication Services  
**Kind**: class

A description that uniquely identifies a particular passkey credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASPasskeyCredentialIdentity
```

## Topics

### Creating a credential identity
- [convenience init(relyingPartyIdentifier: String, userName: String, credentialID: Data, userHandle: Data, recordIdentifier: String?)](aspasskeycredentialidentity/init(relyingpartyidentifier:username:credentialid:userhandle:recordidentifier:)-7u7p1.md)
  Initializes a passkey credential identity.
- [convenience init(relyingPartyIdentifier: String, userName: String, credentialID: Data, userHandle: Data, recordIdentifier: String?)](aspasskeycredentialidentity/init(relyingpartyidentifier:username:credentialid:userhandle:recordidentifier:)-9iuhb.md)
  Creates and initializes a passkey credential identity.
### Ordering credential identities
- [var rank: Int](aspasskeycredentialidentity/rank.md)
  An indicator that enables you to prioritize credential identities relative to each other.
### Associating a user
- [var userName: String](aspasskeycredentialidentity/username.md)
  The username of this passkey credential.
- [var userHandle: Data](aspasskeycredentialidentity/userhandle.md)
  The user handle of this passkey credential.
### Associating a relying party
- [var relyingPartyIdentifier: String](aspasskeycredentialidentity/relyingpartyidentifier.md)
  A string that identifies this identity’s relying party.
### Distinguishing identities
- [var credentialID: Data](aspasskeycredentialidentity/credentialid.md)
  The credential identifier for this passkey credential identity.
- [var recordIdentifier: String?](aspasskeycredentialidentity/recordidentifier.md)
  A string used to correlate this identity to a record in your app’s own database.

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
- [class ASPasswordCredentialIdentity](aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialidentity)*