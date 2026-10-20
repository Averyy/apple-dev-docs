# removeCredentialIdentities(_:completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Removes the given credential identities from the store.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`removeCredentialIdentities(_:completion:)`](./removecredentialidentities%28_,completion%29-67lcw.md) instead.

## Declaration

```swift
func removeCredentialIdentities(_ credentialIdentities: [ASPasswordCredentialIdentity], completion: (@Sendable (Bool, (any Error)?) -> Void)? = nil)
```

```swift
func removeCredentialIdentities(_ credentialIdentities: [ASPasswordCredentialIdentity]) async throws
```

```objc
- (void) removeCredentialIdentities:(NSArray<ASPasswordCredentialIdentity *> *) credentialIdentities completion:(void (^)(BOOL success, NSError *error)) completion;
```

#### Discussion

Use this method only if the store supports incremental updates to remove previously added credentials to the store.

## Parameters

- `credentialIdentities`: An array of [`ASPasswordCredentialIdentity`](../aspasswordcredentialidentity.md) objects to remove from the store.
- `completion`: An optional completion handler called after removing the credential identities. If the operation fails, an error with domain [`ASCredentialIdentityStoreErrorDomain`](../ascredentialidentitystoreerrordomain.md) is provided and none of the objects in `credentialIdentities` is removed from the store.

## See Also

### Deprecated methods
- [func saveCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./savecredentialidentities%28_,completion%29-5vs4m.md)
  Saves the given credential identities to the store.
- [func replaceCredentialIdentities(with: [ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./replacecredentialidentities%28with,completion%29.md)
  Replaces existing credential identities with new credential identities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/removecredentialidentities(_:completion:)-2ygnf)*