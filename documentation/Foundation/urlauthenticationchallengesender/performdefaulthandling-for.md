# performDefaultHandling(for:)

**Framework**: Foundation  
**Kind**: method

Causes the system-provided default behavior to be used.

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
optional func performDefaultHandling(for challenge: URLAuthenticationChallenge)
```

## Parameters

- `challenge`: The challenge for which the default behavior should be used.

## See Also

- [func cancel(URLAuthenticationChallenge)](urlauthenticationchallengesender/cancel(_:).md)
  Cancels a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/continuewithoutcredential(for:).md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](urlauthenticationchallengesender/use(_:for:).md)
  Attempt to use a given credential for a given authentication challenge.
- [func rejectProtectionSpaceAndContinue(with: URLAuthenticationChallenge)](urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:).md)
  Rejects the currently supplied protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/performdefaulthandling(for:))*