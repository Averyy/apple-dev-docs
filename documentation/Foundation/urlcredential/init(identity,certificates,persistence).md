# init(identity:certificates:persistence:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a URL credential instance for resolving a client certificate authentication challenge.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(identity: SecIdentity, certificates certArray: [Any]?, persistence: URLCredential.Persistence)
```

```objc
- (instancetype) initWithIdentity:(SecIdentityRef) identity certificates:(NSArray *) certArray persistence:(NSURLCredentialPersistence) persistence;
```

## Return Value

A new URL credential object, using the provided identity and, optionally, an array of intermediate certificates.

## Discussion

When you receive a client certificate authentication challenge ([`NSURLAuthenticationMethodClientCertificate`](../nsurlauthenticationmethodclientcertificate.md)) and want to resolve it successfully, you must supply a credential created using this initializer.

In most cases you should pass `nil` to the `certArray` parameter. You only need to supply an array of intermediate certificates if the server needs those intermediate certificates to authenticate the client. Typically this isn’t necessary because the server already has a copy of the relevant intermediate certificates.

## Parameters

- `identity`: The identity for the credential.
- `certArray`: An array of one or more `SecCertificateRef` objects representing intermediate certificates leading from the identity’s certificate to a trusted root, or `nil` if the server does not need any intermediate certificates to authenticate the client.
- `persistence`: The method ignores this parameter; you should supply a value of [`URLCredential.Persistence.forSession`](./persistence-swift.enum/forsession.md) because that most accurately reflects the actual behaviour.

## See Also

### Creating a credential
- [init(forTrust: SecTrust)](./init%28fortrust%29.md)
  Creates a URL credential instance for server trust authentication with a given accepted trust.
- [init(trust: SecTrust)](./init%28trust%29.md)
  Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [init(user: String, password: String, persistence: URLCredential.Persistence)](./init%28user,password,persistence%29.md)
  Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [URLCredential.Persistence](./persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.
- [+ credentialWithUser:password:persistence:](../nsurlcredential/credentialwithuser_password_persistence_.md)
  Creates a URL credential instance for internet password authentication with a given user name and password, using a given persistence setting.
- [+ credentialWithIdentity:certificates:persistence:](../nsurlcredential/credentialwithidentity_certificates_persistence_.md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/init(identity:certificates:persistence:))*