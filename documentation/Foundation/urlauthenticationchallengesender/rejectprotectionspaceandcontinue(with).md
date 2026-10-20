# rejectProtectionSpaceAndContinue(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) rejectProtectionSpaceAndContinueWithChallenge:(NSURLAuthenticationChallenge *) challenge;
```

## Parameters

- `challenge`: The challenge that should be rejected.

## See Also

### Protocol Methods
- [func cancel(URLAuthenticationChallenge)](./cancel%28_%29.md)
  Cancels a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](./continuewithoutcredential%28for%29.md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](./use%28_,for%29.md)
  Attempt to use a given credential for a given authentication challenge.
- [func performDefaultHandling(for: URLAuthenticationChallenge)](./performdefaulthandling%28for%29.md)
  Causes the system-provided default behavior to be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/rejectprotectionspaceandcontinue(with:))*