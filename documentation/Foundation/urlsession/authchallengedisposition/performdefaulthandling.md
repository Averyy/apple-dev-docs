# URLSession.AuthChallengeDisposition.performDefaultHandling

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.

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
case performDefaultHandling
```

```c
NSURLSessionAuthChallengePerformDefaultHandling
```

## Mentions

- [Performing manual server trust authentication](../../performing-manual-server-trust-authentication.md)

## See Also

### Constants
- [URLSession.AuthChallengeDisposition.useCredential](./usecredential.md)
  Use the specified credential, which may be `nil`.
- [URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge](./cancelauthenticationchallenge.md)
  Cancel the entire request. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.rejectProtectionSpace](./rejectprotectionspace.md)
  Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/performdefaulthandling)*