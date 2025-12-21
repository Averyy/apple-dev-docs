# URLCredential.Persistence

**Framework**: Foundation  
**Kind**: enum

Constants that specify how long the credential will be kept.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Persistence
```

#### Overview

In iOS, credentials are stored in the app’s keychain, and can be accessed only by that app (and other apps in the same keychain access group, where applicable).

In macOS, credentials are stored in the user’s keychain. The credential’s initial access control list (ACL) allows access only by that app. However, other apps can see that a password exists for a given host, port, and realm combination, and can request that the user grant permission to use that credential.

## Topics

### Persistence strategies
- [URLCredential.Persistence.none](urlcredential/persistence-swift.enum/none.md)
  The credential should not be stored.
- [URLCredential.Persistence.forSession](urlcredential/persistence-swift.enum/forsession.md)
  The credential should be stored only for this session.
- [URLCredential.Persistence.permanent](urlcredential/persistence-swift.enum/permanent.md)
  The credential should be stored in the keychain.
- [URLCredential.Persistence.synchronizable](urlcredential/persistence-swift.enum/synchronizable.md)
  The credential should be stored permanently in the keychain, and in addition should be distributed to other devices based on the owning Apple ID.
### Initializers
- [init?(rawValue: UInt)](urlcredential/persistence-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(forTrust: SecTrust)](urlcredential/init(fortrust:).md)
  Creates a URL credential instance for server trust authentication with a given accepted trust.
- [init(identity: SecIdentity, certificates: [Any]?, persistence: URLCredential.Persistence)](urlcredential/init(identity:certificates:persistence:).md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(trust: SecTrust)](urlcredential/init(trust:).md)
  Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [init(user: String, password: String, persistence: URLCredential.Persistence)](urlcredential/init(user:password:persistence:).md)
  Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.enum)*