# removeAllCredentialIdentities(_:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Removes all existing credential identities from the store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeAllCredentialIdentities(_ completion: (@Sendable (Bool, (any Error)?) -> Void)? = nil)
```

```swift
func removeAllCredentialIdentities() async throws
```

```objc
- (void) removeAllCredentialIdentitiesWithCompletion:(void (^)(BOOL success, NSError *error)) completion;
```

## Parameters

- `completion`: An optional completion handler called after removing all existing credential identities. If the operation fails, an error with domain [`ASCredentialIdentityStoreErrorDomain`](../ascredentialidentitystoreerrordomain.md) is provided and none of the existing credential identities are removed from the store.

## See Also

### Adding and removing credential identities
- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./savecredentialidentities%28_,completion%29-1bbx6.md)
  Save the supplied credential identities to the store.
- [func replaceCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./replacecredentialidentities%28_,completion%29.md)
  Replaces existing credential identities with new credential identities.
- [func removeCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./removecredentialidentities%28_,completion%29-67lcw.md)
  Remove the given credential identities from the store.
- [protocol ASCredentialIdentity](../ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](../aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.
- [class ASPasswordCredentialIdentity](../aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/removeallcredentialidentities(_:))*