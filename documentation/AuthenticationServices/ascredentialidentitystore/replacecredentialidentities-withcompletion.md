# replaceCredentialIdentities(with:completion:)

**Framework**: Authentication Services  
**Kind**: method

Replaces existing credential identities with new credential identities.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func replaceCredentialIdentities(with newCredentialIdentities: [ASPasswordCredentialIdentity]) async throws
```

#### Discussion

This method deletes existing credential identities that are persisted in the store and saves the newly provided credential identity objects. If the operation fails, an error with domain [`ASCredentialIdentityStoreErrorDomain`](ascredentialidentitystoreerrordomain.md) is provided and none of the new credential identities are saved.

## Parameters

- `newCredentialIdentities`: An array of new credential identity objects to replace the old ones.
- `completion`: An optional completion block called after the operation finishes.

## See Also

- [func saveCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-5vs4m.md)
  Saves the given credential identities to the store.
- [func removeCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removecredentialidentities(_:completion:)-2ygnf.md)
  Removes the given credential identities from the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/replacecredentialidentities(with:completion:))*