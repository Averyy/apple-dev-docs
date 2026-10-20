# performDefaultHandling(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) performDefaultHandlingForAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge;
```

## Parameters

- `challenge`: The challenge for which the default behavior should be used.

## See Also

### Protocol Methods
- [func cancel(URLAuthenticationChallenge)](./cancel%28_%29.md)
  Cancels a given authentication challenge.
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](./continuewithoutcredential%28for%29.md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](./use%28_,for%29.md)
  Attempt to use a given credential for a given authentication challenge.
- [func rejectProtectionSpaceAndContinue(with: URLAuthenticationChallenge)](./rejectprotectionspaceandcontinue%28with%29.md)
  Rejects the currently supplied protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/performdefaulthandling(for:))*