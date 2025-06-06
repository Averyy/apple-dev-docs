# saveCredentialIdentities(_:completion:)

**Framework**: Authentication Services  
**Kind**: method

Saves the given credential identities to the store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func saveCredentialIdentities(_ credentialIdentities: [ASPasswordCredentialIdentity]) async throws
```

#### Discussion

If the store supports incremental updates, call this method to add new credential identities since the last time the store was updated. Otherwise, call this method to pass all credential identities. If some credential identities in `credentialIdentities` already exist in the store, they will be replaced by those from `credentialIdentities`.

## Parameters

- `credentialIdentities`: An array of   objects to save to the store.
- `completion`: An optional completion handler to be called after adding the credential identities. If the operation fails, an error with domain   will be provided and none of the objects in credentialIdentities are saved to the store.

## See Also

- [func replaceCredentialIdentities(with: [ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/replacecredentialidentities(with:completion:).md)
  Replaces existing credential identities with new credential identities.
- [func removeCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removecredentialidentities(_:completion:)-2ygnf.md)
  Removes the given credential identities from the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/savecredentialidentities(_:completion:)-5vs4m)*