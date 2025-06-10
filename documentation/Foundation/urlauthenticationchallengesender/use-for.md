# use(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Attempt to use a given credential for a given authentication challenge.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func use(_ credential: URLCredential, for challenge: URLAuthenticationChallenge)
```

#### Discussion

This method has no effect if it is called with an authentication challenge that has already been handled.

## Parameters

- `credential`: The credential to use for authentication.
- `challenge`: The challenge for which to use  .

## See Also

- [func cancel(URLAuthenticationChallenge)](urlauthenticationchallengesender/cancel(_:).md)
  Cancels a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/continuewithoutcredential(for:).md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func performDefaultHandling(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/performdefaulthandling(for:).md)
  Causes the system-provided default behavior to be used.
- [func rejectProtectionSpaceAndContinue(with: URLAuthenticationChallenge)](urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:).md)
  Rejects the currently supplied protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/use(_:for:))*