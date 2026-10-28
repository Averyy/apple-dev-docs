# removeCredentialIdentities(_:completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Remove the given credential identities from the store.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeCredentialIdentities(_ credentialIdentities: [any ASCredentialIdentity], completion: (@Sendable (Bool, (any Error)?) -> Void)? = nil)
```

```swift
func removeCredentialIdentities(_ credentialIdentities: [any ASCredentialIdentity]) async throws
```

```objc
- (void) removeCredentialIdentityEntries:(NSArray<id<ASCredentialIdentity>> *) credentialIdentities completion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

Call this method if the credential store supports incremental updates to remove previously-added credential identities. On failure, this method calls the callback with an error with domain [`ASCredentialIdentityStoreErrorDomain`](../ascredentialidentitystoreerrordomain.md) and doesn’t remove any of the objects in `credentialIdentities` from the store.

## Parameters

- `credentialIdentities`: A list of credential identities to remove.
- `completion`: An optional completion handler that runs when the operation finishes.

## See Also

### Adding and removing credential identities
- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./savecredentialidentities%28_,completion%29-1bbx6.md)
  Save the supplied credential identities to the store.
- [func replaceCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./replacecredentialidentities%28_,completion%29.md)
  Replaces existing credential identities with new credential identities.
- [func removeAllCredentialIdentities(((Bool, (any Error)?) -> Void)?)](./removeallcredentialidentities%28_%29.md)
  Removes all existing credential identities from the store.
- [protocol ASCredentialIdentity](../ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](../aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.
- [class ASPasswordCredentialIdentity](../aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/removecredentialidentities(_:completion:)-67lcw)*