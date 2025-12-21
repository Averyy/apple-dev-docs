# URLSession.AuthChallengeDisposition.useCredential

**Framework**: Foundation  
**Kind**: case

Use the specified credential, which may be `nil`.

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
case useCredential
```

## Mentions

- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)

## See Also

- [URLSession.AuthChallengeDisposition.performDefaultHandling](urlsession/authchallengedisposition/performdefaulthandling.md)
  Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge](urlsession/authchallengedisposition/cancelauthenticationchallenge.md)
  Cancel the entire request. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.rejectProtectionSpace](urlsession/authchallengedisposition/rejectprotectionspace.md)
  Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/usecredential)*