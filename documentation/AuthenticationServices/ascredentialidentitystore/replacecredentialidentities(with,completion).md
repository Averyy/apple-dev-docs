# replaceCredentialIdentities(with:completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Replaces existing credential identities with new credential identities.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`replaceCredentialIdentities(_:completion:)`](./replacecredentialidentities%28_,completion%29.md) instead.

## Declaration

```swift
func replaceCredentialIdentities(with newCredentialIdentities: [ASPasswordCredentialIdentity], completion: (@Sendable (Bool, (any Error)?) -> Void)? = nil)
```

```swift
func replaceCredentialIdentities(with newCredentialIdentities: [ASPasswordCredentialIdentity]) async throws
```

```objc
- (void) replaceCredentialIdentitiesWithIdentities:(NSArray<ASPasswordCredentialIdentity *> *) newCredentialIdentities completion:(void (^)(BOOL success, NSError *error)) completion;
```

#### Discussion

This method deletes existing credential identities that are persisted in the store and saves the newly provided credential identity objects. If the operation fails, an error with domain [`ASCredentialIdentityStoreErrorDomain`](../ascredentialidentitystoreerrordomain.md) is provided and none of the new credential identities are saved.

## Parameters

- `newCredentialIdentities`: An array of new credential identity objects to replace the old ones.
- `completion`: An optional completion block called after the operation finishes.

## See Also

### Deprecated methods
- [func saveCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./savecredentialidentities%28_,completion%29-5vs4m.md)
  Saves the given credential identities to the store.
- [func removeCredentialIdentities([ASPasswordCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./removecredentialidentities%28_,completion%29-2ygnf.md)
  Removes the given credential identities from the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/replacecredentialidentities(with:completion:))*