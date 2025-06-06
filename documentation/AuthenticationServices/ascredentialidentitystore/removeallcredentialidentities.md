# removeAllCredentialIdentities(_:)

**Framework**: Authentication Services  
**Kind**: method

Removes all existing credential identities from the store.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeAllCredentialIdentities() async throws
```

## Parameters

- `completion`: An optional completion handler called after removing all existing credential identities. If the operation fails, an error with domain   is provided and none of the existing credential identities are removed from the store.

## See Also

- [func saveCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/savecredentialidentities(_:completion:)-1bbx6.md)
  Save the supplied credential identities to the store.
- [func replaceCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/replacecredentialidentities(_:completion:).md)
  Replaces existing credential identities with new credential identities.
- [func removeCredentialIdentities([any ASCredentialIdentity], completion: ((Bool, (any Error)?) -> Void)?)](ascredentialidentitystore/removecredentialidentities(_:completion:)-67lcw.md)
  Remove the given credential identities from the store.
- [protocol ASCredentialIdentity](ascredentialidentity.md)
  A protocol that credential identity classes conform to that uniquely identifies credentials.
- [class ASPasskeyCredentialIdentity](aspasskeycredentialidentity.md)
  A description that uniquely identifies a particular passkey credential.
- [class ASPasswordCredentialIdentity](aspasswordcredentialidentity.md)
  A description that uniquely identifies a particular password credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystore/removeallcredentialidentities(_:))*