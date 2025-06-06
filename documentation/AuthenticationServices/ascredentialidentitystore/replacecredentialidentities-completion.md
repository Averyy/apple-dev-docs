# replaceCredentialIdentities(_:completion:)

**Framework**: Authentication Services  
**Kind**: method

Replaces existing credential identities with new credential identities.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func replaceCredentialIdentities(_ newCredentialIdentities: [any ASCredentialIdentity]) async throws
```

#### Discussion

This method deletes existing credential identities in the store and saves the newly provided credential identity objects. On failure, this method calls the callback with an error with domain [`ASCredentialIdentityStoreErrorDomain`](ascredentialidentitystoreerrordomain.md) and doesn’t save any of the objects in `newCredentialIdentities` to the store.

## See Also

- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-1bbx6.md)
  Save the supplied credential identities to the store.
- [func removeAllCredentialIdentities(((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removeallcredentialidentities(_:).md)
  Removes all existing credential identities from the store.
- [func removeCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removecredentialidentities(_:completion:)-67lcw.md)
  Remove the given credential identities from the store.
- [protocol ASCredentialIdentity](ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.
- [class ASPasswordCredentialIdentity](aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/replacecredentialidentities(_:completion:))*