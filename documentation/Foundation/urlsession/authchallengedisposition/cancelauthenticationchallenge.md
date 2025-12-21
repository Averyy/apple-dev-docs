# URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge

**Framework**: Foundation  
**Kind**: case

Cancel the entire request. The provided credential parameter is ignored.

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
case cancelAuthenticationChallenge
```

## Mentions

- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)

## See Also

- [URLSession.AuthChallengeDisposition.useCredential](urlsession/authchallengedisposition/usecredential.md)
  Use the specified credential, which may be `nil`.
- [URLSession.AuthChallengeDisposition.performDefaultHandling](urlsession/authchallengedisposition/performdefaulthandling.md)
  Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.rejectProtectionSpace](urlsession/authchallengedisposition/rejectprotectionspace.md)
  Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/cancelauthenticationchallenge)*