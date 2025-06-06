# removeCredentialIdentities(_:completion:)

**Framework**: Authentication Services  
**Kind**: method

Removes the given credential identities from the store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeCredentialIdentities(_ credentialIdentities: [ASPasswordCredentialIdentity]) async throws
```

#### Discussion

Use this method only if the store supports incremental updates to remove previously added credentials to the store.

## Parameters

- `credentialIdentities`: An array of   objects to remove from the store.
- `completion`: An optional completion handler called after removing the credential identities. If the operation fails, an error with domain   is provided and none of the objects in   is removed from the store.

## See Also

- [func saveCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-5vs4m.md)
  Saves the given credential identities to the store.
- [func replaceCredentialIdentities(with: [ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/replacecredentialidentities(with:completion:).md)
  Replaces existing credential identities with new credential identities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/removecredentialidentities(_:completion:)-2ygnf)*