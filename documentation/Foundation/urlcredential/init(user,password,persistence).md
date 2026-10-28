# init(user:password:persistence:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithUser:(NSString *) user password:(NSString *) password persistence:(NSURLCredentialPersistence) persistence;
```

## Return Value

An instance of [`URLCredential`](../urlcredential.md), initialized with user name `user`, password `password`, and using persistence setting `persistence`.

## Discussion

If `persistence` is [`URLCredential.Persistence.permanent`](./persistence-swift.enum/permanent.md), the credential is stored in the keychain. If `persistence` is [`URLCredential.Persistence.synchronizable`](./persistence-swift.enum/synchronizable.md), it is also stored to the user’s other devices.

## Parameters

- `user`: The user for the credential.
- `password`: The password for `user`.
- `persistence`: A [`URLCredential.Persistence`](./persistence-swift.enum.md) value indicating whether the credential should be stored permanently, for the duration of the current session, or not at all.

## See Also

### Creating a credential
- [init(forTrust: SecTrust)](./init%28fortrust%29.md)
  Creates a URL credential instance for server trust authentication with a given accepted trust.
- [init(identity: SecIdentity, certificates: [Any]?, persistence: URLCredential.Persistence)](./init%28identity,certificates,persistence%29.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(trust: SecTrust)](./init%28trust%29.md)
  Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [URLCredential.Persistence](./persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.
- [+ credentialWithIdentity:certificates:persistence:](../nsurlcredential/credentialwithidentity_certificates_persistence_.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
### Related Documentation
- [+ credentialWithUser:password:persistence:](../nsurlcredential/credentialwithuser_password_persistence_.md)
  Creates a URL credential instance for internet password authentication with a given user name and password, using a given persistence setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/init(user:password:persistence:))*