# rejectProtectionSpaceAndContinue(with:)

**Framework**: Foundation  
**Kind**: method

Rejects the currently supplied protection space.

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
optional func rejectProtectionSpaceAndContinue(with challenge: URLAuthenticationChallenge)
```

## Parameters

- `challenge`: The challenge that should be rejected.

## See Also

- [func cancel(URLAuthenticationChallenge)](urlauthenticationchallengesender/cancel(_:).md)
  Cancels a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/continuewithoutcredential(for:).md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](urlauthenticationchallengesender/use(_:for:).md)
  Attempt to use a given credential for a given authentication challenge.
- [func performDefaultHandling(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/performdefaulthandling(for:).md)
  Causes the system-provided default behavior to be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:))*