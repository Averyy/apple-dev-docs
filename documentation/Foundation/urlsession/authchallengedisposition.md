# URLSession.AuthChallengeDisposition

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSURLSessionAuthChallengeDisposition : NSInteger;
```

## Topics

### Constants
- [URLSession.AuthChallengeDisposition.useCredential](./authchallengedisposition/usecredential.md)
  Use the specified credential, which may be `nil`.
- [URLSession.AuthChallengeDisposition.performDefaultHandling](./authchallengedisposition/performdefaulthandling.md)
  Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge](./authchallengedisposition/cancelauthenticationchallenge.md)
  Cancel the entire request. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.rejectProtectionSpace](./authchallengedisposition/rejectprotectionspace.md)
  Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.
### Initializers
- [init?(rawValue: Int)](./authchallengedisposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling authentication challenges
- [func urlSession(URLSession, didReceive: URLAuthenticationChallenge, completionHandler: (URLSession.AuthChallengeDisposition, URLCredential?) -> Void)](../urlsessiondelegate/urlsession%28_,didreceive,completionhandler%29.md)
  Requests credentials from the delegate in response to a session-level authentication request from the remote server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition)*