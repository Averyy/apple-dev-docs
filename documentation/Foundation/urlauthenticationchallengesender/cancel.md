# cancel(_:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Cancels a given authentication challenge.

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
func cancel(_ challenge: URLAuthenticationChallenge)
```

## Parameters

- `challenge`: The authentication challenge to cancel.

## See Also

- [URL Loading System](url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/continuewithoutcredential(for:).md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](urlauthenticationchallengesender/use(_:for:).md)
  Attempt to use a given credential for a given authentication challenge.
- [func performDefaultHandling(for: URLAuthenticationChallenge)](urlauthenticationchallengesender/performdefaulthandling(for:).md)
  Causes the system-provided default behavior to be used.
- [func rejectProtectionSpaceAndContinue(with: URLAuthenticationChallenge)](urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:).md)
  Rejects the currently supplied protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/cancel(_:))*