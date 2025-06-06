# saveCredentialIdentities(_:completion:)

**Framework**: Authentication Services  
**Kind**: method

Save the supplied credential identities to the store.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func saveCredentialIdentities(_ credentialIdentities: [any ASCredentialIdentity]) async throws
```

#### Discussion

Call this method if the credential store supports incremental updates to add new credential identities. Otherwise, call this method passing all credential identities. If any of the credential identities in the `credentialIdentities` array already exist in the store, this method overwrites them with the values in the array.

On failure, this method calls the callback with an error with domain [`ASCredentialIdentityStoreErrorDomain`](ascredentialidentitystoreerrordomain.md) and doesn’t save any of the objects in `credentialIdentities` to the store.

## Parameters

- `credentialIdentities`: A list of credential identities to save.
- `completion`: An optional completion handler that runs when the operation finishes.

## See Also

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
- [class ASPasswordCredentialIdentity](aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/savecredentialidentities(_:completion:)-1bbx6)*