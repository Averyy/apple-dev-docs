# URLSession.AuthChallengeDisposition

**Framework**: Foundation  
**Kind**: enum

Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum AuthChallengeDisposition
```

## Topics

### Constants
- [URLSession.AuthChallengeDisposition.useCredential](urlsession/authchallengedisposition/usecredential.md)
  Use the specified credential, which may be `nil`.
- [URLSession.AuthChallengeDisposition.performDefaultHandling](urlsession/authchallengedisposition/performdefaulthandling.md)
  Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge](urlsession/authchallengedisposition/cancelauthenticationchallenge.md)
  Cancel the entire request. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.rejectProtectionSpace](urlsession/authchallengedisposition/rejectprotectionspace.md)
  Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.useCredential](urlsession/authchallengedisposition/usecredential.md)
  Use the specified credential, which may be `nil`.
- [URLSession.AuthChallengeDisposition.performDefaultHandling](urlsession/authchallengedisposition/performdefaulthandling.md)
  Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge](urlsession/authchallengedisposition/cancelauthenticationchallenge.md)
  Cancel the entire request. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.rejectProtectionSpace](urlsession/authchallengedisposition/rejectprotectionspace.md)
  Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.
### Initializers
- [init?(rawValue: Int)](urlsession/authchallengedisposition/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func urlSession(URLSession, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](urlsessiondelegate/urlsession(_:didreceive:completionhandler:).md)
  Requests credentials from the delegate in response to a session-level authentication request from the remote server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition)*