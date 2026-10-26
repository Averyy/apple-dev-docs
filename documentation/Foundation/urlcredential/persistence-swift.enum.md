# URLCredential.Persistence

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSURLCredentialPersistence : NSUInteger;
```

#### Overview

In iOS, credentials are stored in the app’s keychain, and can be accessed only by that app (and other apps in the same keychain access group, where applicable).

In macOS, credentials are stored in the user’s keychain. The credential’s initial access control list (ACL) allows access only by that app. However, other apps can see that a password exists for a given host, port, and realm combination, and can request that the user grant permission to use that credential.

## Topics

### Persistence strategies
- [URLCredential.Persistence.none](./persistence-swift.enum/none.md)
  The credential should not be stored.
- [URLCredential.Persistence.forSession](./persistence-swift.enum/forsession.md)
  The credential should be stored only for this session.
- [URLCredential.Persistence.permanent](./persistence-swift.enum/permanent.md)
  The credential should be stored in the keychain.
- [URLCredential.Persistence.synchronizable](./persistence-swift.enum/synchronizable.md)
  The credential should be stored permanently in the keychain, and in addition should be distributed to other devices based on the owning Apple ID.
### Initializers
- [init?(rawValue: UInt)](./persistence-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a credential
- [init(forTrust: SecTrust)](./init%28fortrust%29.md)
  Creates a URL credential instance for server trust authentication with a given accepted trust.
- [init(identity: SecIdentity, certificates: [Any]?, persistence: URLCredential.Persistence)](./init%28identity,certificates,persistence%29.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(trust: SecTrust)](./init%28trust%29.md)
  Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [init(user: String, password: String, persistence: URLCredential.Persistence)](./init%28user,password,persistence%29.md)
  Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [+ credentialWithUser:password:persistence:](../nsurlcredential/credentialwithuser_password_persistence_.md)
  Creates a URL credential instance for internet password authentication with a given user name and password, using a given persistence setting.
- [+ credentialWithIdentity:certificates:persistence:](../nsurlcredential/credentialwithidentity_certificates_persistence_.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/persistence-swift.enum)*