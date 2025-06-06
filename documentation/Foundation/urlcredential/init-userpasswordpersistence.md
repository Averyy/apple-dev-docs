# init(user:password:persistence:)

**Framework**: Foundation  
**Kind**: init

Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.

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
init(user: String, password: String, persistence: URLCredential.Persistence)
```

#### Return Value

An instance of [`URLCredential`](urlcredential.md), initialized with user name `user`, password `password`, and using persistence setting `persistence`.

#### Discussion

If `persistence` is [`URLCredential.Persistence.permanent`](urlcredential/persistence-swift.enum/permanent.md), the credential is stored in the keychain. If `persistence` is [`URLCredential.Persistence.synchronizable`](urlcredential/persistence-swift.enum/synchronizable.md), it is also stored to the user’s other devices.

## Parameters

- `user`: The user for the credential.
- `password`: The password for  .
- `persistence`: A   value indicating whether the credential should be stored permanently, for the duration of the current session, or not at all.

## See Also

- [init(forTrust: SecTrust)](urlcredential/init(fortrust:).md)
  Creates a URL credential instance for server trust authentication with a given accepted trust.
- [init(identity: SecIdentity, certificates: [Any]?, persistence: URLCredential.Persistence)](urlcredential/init(identity:certificates:persistence:).md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(trust: SecTrust)](urlcredential/init(trust:).md)
  Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [URLCredential.Persistence](urlcredential/persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/init(user:password:persistence:))*