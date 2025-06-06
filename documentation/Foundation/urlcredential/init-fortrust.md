# init(forTrust:)

**Framework**: Foundation  
**Kind**: init

Creates a URL credential instance for server trust authentication with a given accepted trust.

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
init(forTrust trust: SecTrust)
```

#### Return Value

A new URL credential object, containing the accepted server trust.

#### Discussion

Before creating a server trust credential, it is the responsibility of the delegate of an [`NSURLConnection`](nsurlconnection.md) instance or an [`NSURLDownload`](nsurldownload.md) instance to evaluate the trust. Do this by calling [`SecTrustEvaluate(_:_:)`](https://developer.apple.com/documentation/Security/SecTrustEvaluate(_:_:)), passing it the trust obtained from the `serverTrust` method of the server’s [`URLProtectionSpace`](urlprotectionspace.md) instance. If the trust is invalid, the authentication challenge should be cancelled with [`cancel(_:)`](urlauthenticationchallengesender/cancel(_:).md).

## Parameters

- `trust`: The accepted trust.

## See Also

- [init(identity: SecIdentity, certificates: [Any]?, persistence: URLCredential.Persistence)](urlcredential/init(identity:certificates:persistence:).md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(trust: SecTrust)](urlcredential/init(trust:).md)
  Creates a URL credential instance for server trust authentication, initialized with a accepted trust.
- [init(user: String, password: String, persistence: URLCredential.Persistence)](urlcredential/init(user:password:persistence:).md)
  Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [URLCredential.Persistence](urlcredential/persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/init(fortrust:))*