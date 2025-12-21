# URLSession.AuthChallengeDisposition.rejectProtectionSpace

**Framework**: Foundation  
**Kind**: case

Reject this challenge, and call the authentication delegate method again with the next authentication protection space. The provided credential parameter is ignored.

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
case rejectProtectionSpace
```

#### Discussion

The [`URLSession.AuthChallengeDisposition.rejectProtectionSpace`](urlsession/authchallengedisposition/rejectprotectionspace.md) disposition is only appropriate in fairly unusual situations. For example, a Windows server might use both [`NSURLAuthenticationMethodNegotiate`](nsurlauthenticationmethodnegotiate.md) and [`NSURLAuthenticationMethodNTLM`](nsurlauthenticationmethodntlm.md). If your app can only handle NTLM, you would want to reject the Negotiate challenge, in order to then receive the queued NTLM challenge.

However, most apps won’t face this scenario, and if you cannot provide a credential for a certain authentication method, you should usually fall back to the [`URLSession.AuthChallengeDisposition.performDefaultHandling`](urlsession/authchallengedisposition/performdefaulthandling.md) disposition instead.

## See Also

- [URLSession.AuthChallengeDisposition.useCredential](urlsession/authchallengedisposition/usecredential.md)
  Use the specified credential, which may be `nil`.
- [URLSession.AuthChallengeDisposition.performDefaultHandling](urlsession/authchallengedisposition/performdefaulthandling.md)
  Use the default handling for the challenge as though this delegate method were not implemented. The provided credential parameter is ignored.
- [URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge](urlsession/authchallengedisposition/cancelauthenticationchallenge.md)
  Cancel the entire request. The provided credential parameter is ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/authchallengedisposition/rejectprotectionspace)*