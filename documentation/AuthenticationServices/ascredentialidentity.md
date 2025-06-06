# ASCredentialIdentity

**Framework**: Authentication Services  
**Kind**: protocol

A protocol that credential identity classes conform to that uniquely identifies credentials.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol ASCredentialIdentity : NSObjectProtocol
```

## Topics

### Ordering credential identities
- [var rank: Int](ascredentialidentity/rank.md)
  An indicator that enables you to prioritize credential identities relative to each other.
### Associating a user
- [var user: String](ascredentialidentity/user.md)
  The username associated with this credential.
### Distinguishing identities
- [var recordIdentifier: String?](ascredentialidentity/recordidentifier.md)
  A string used to correlate this identity to a record in your app’s own database.
- [var serviceIdentifier: ASCredentialServiceIdentifier](ascredentialidentity/serviceidentifier.md)
  An identifier that helps the system know with which apps or websites to associate this credential.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [ASOneTimeCodeCredentialIdentity](asonetimecodecredentialidentity.md)
- [ASPasskeyCredentialIdentity](aspasskeycredentialidentity.md)
- [ASPasswordCredentialIdentity](aspasswordcredentialidentity.md)

## See Also

- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-1bbx6.md)
  Save the supplied credential identities to the store.
- [func replaceCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/replacecredentialidentities(_:completion:).md)
  Replaces existing credential identities with new credential identities.
- [func removeAllCredentialIdentities(((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removeallcredentialidentities(_:).md)
  Removes all existing credential identities from the store.
- [func removeCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removecredentialidentities(_:completion:)-67lcw.md)
  Remove the given credential identities from the store.
- [class ASPasskeyCredentialIdentity](aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.
- [class ASPasswordCredentialIdentity](aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentity)*