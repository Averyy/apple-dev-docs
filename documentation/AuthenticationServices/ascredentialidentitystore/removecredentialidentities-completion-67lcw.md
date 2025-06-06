# removeCredentialIdentities(_:completion:)

**Framework**: Authentication Services  
**Kind**: method

Remove the given credential identities from the store.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeCredentialIdentities(_ credentialIdentities: [any ASCredentialIdentity]) async throws
```

#### Discussion

Call this method if the credential store supports incremental updates to remove previously-added credential identities. On failure, this method calls the callback with an error with domain [`ASCredentialIdentityStoreErrorDomain`](ascredentialidentitystoreerrordomain.md) and doesn’t remove any of the objects in `credentialIdentities` from the store.

## Parameters

- `credentialIdentities`: A list of credential identities to remove.
- `completion`: An optional completion handler that runs when the operation finishes.

## See Also

- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-1bbx6.md)
  Save the supplied credential identities to the store.
- [func replaceCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/replacecredentialidentities(_:completion:).md)
  Replaces existing credential identities with new credential identities.
- [func removeAllCredentialIdentities(((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removeallcredentialidentities(_:).md)
  Removes all existing credential identities from the store.
- [protocol ASCredentialIdentity](ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.
- [class ASPasswordCredentialIdentity](aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/removecredentialidentities(_:completion:)-67lcw)*