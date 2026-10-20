# replaceCredentialIdentities(_:completion:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Replaces existing credential identities with new credential identities.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func replaceCredentialIdentities(_ newCredentialIdentities: [any ASCredentialIdentity], completion: (@Sendable (Bool, (any Error)?) -> Void)? = nil)
```

```swift
func replaceCredentialIdentities(_ newCredentialIdentities: [any ASCredentialIdentity]) async throws
```

```objc
- (void) replaceCredentialIdentityEntries:(NSArray<id<ASCredentialIdentity>> *) newCredentialIdentities completion:(void (^)(BOOL success, NSError *error)) completion;
```

#### Discussion

This method deletes existing credential identities in the store and saves the newly provided credential identity objects. On failure, this method calls the callback with an error with domain [`ASCredentialIdentityStoreErrorDomain`](../ascredentialidentitystoreerrordomain.md) and doesn’t save any of the objects in `newCredentialIdentities` to the store.

## See Also

### Adding and removing credential identities
- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./savecredentialidentities%28_,completion%29-1bbx6.md)
  Save the supplied credential identities to the store.
- [func removeAllCredentialIdentities(((Bool, (any Error)?) -> Void)?)](./removeallcredentialidentities%28_%29.md)
  Removes all existing credential identities from the store.
- [func removeCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](./removecredentialidentities%28_,completion%29-67lcw.md)
  Remove the given credential identities from the store.
- [protocol ASCredentialIdentity](../ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](../aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.
- [class ASPasswordCredentialIdentity](../aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/replacecredentialidentities(_:completion:))*