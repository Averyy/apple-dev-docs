# init(trust:)

**Framework**: Foundation  
**Kind**: init

Creates a URL credential instance for server trust authentication, initialized with a accepted trust.

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
init(trust: SecTrust)
```

#### Return Value

A new URL credential object, containing the provided server trust.

#### Discussion

Before your implementation of [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) uses this initializer to create a server trust credential, you are responsible for evaluating the received [`SecTrust`](https://developer.apple.com/documentation/Security/SecTrust) instance. You get this [`serverTrust`](urlprotectionspace/servertrust.md) from the [`protectionSpace`](urlauthenticationchallenge/protectionspace.md) of the [`URLAuthenticationChallenge`](urlauthenticationchallenge.md) parameter that is passed to your delegate method. Pass the trust instance to [`SecTrustEvaluate(_:_:)`](https://developer.apple.com/documentation/Security/SecTrustEvaluate(_:_:)) to evaluate it. If this call indicates the trust is invalid, you should cancel the challenge by passing the [`URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge`](urlsession/authchallengedisposition/cancelauthenticationchallenge.md) disposition to the completion handler.

## Parameters

- `trust`: The accepted trust.

## See Also

- [init(forTrust: SecTrust)](urlcredential/init(fortrust:).md)
  Creates a URL credential instance for server trust authentication with a given accepted trust.
- [init(identity: SecIdentity, certificates: [Any]?, persistence: URLCredential.Persistence)](urlcredential/init(identity:certificates:persistence:).md)
  Creates a URL credential instance for resolving a client certificate authentication challenge.
- [init(user: String, password: String, persistence: URLCredential.Persistence)](urlcredential/init(user:password:persistence:).md)
  Creates a URL credential instance initialized with a given user name and password, using a given persistence setting.
- [URLCredential.Persistence](urlcredential/persistence-swift.enum.md)
  Constants that specify how long the credential will be kept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcredential/init(trust:))*