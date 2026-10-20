# cancel(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) cancelAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge;
```

## Parameters

- `challenge`: The authentication challenge to cancel.

## See Also

### Related Documentation
- [URL Loading System](../url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.
### Protocol Methods
- [func continueWithoutCredential(for: URLAuthenticationChallenge)](./continuewithoutcredential%28for%29.md)
  Attempt to continue downloading a request without providing a credential for a given challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](./use%28_,for%29.md)
  Attempt to use a given credential for a given authentication challenge.
- [func performDefaultHandling(for: URLAuthenticationChallenge)](./performdefaulthandling%28for%29.md)
  Causes the system-provided default behavior to be used.
- [func rejectProtectionSpaceAndContinue(with: URLAuthenticationChallenge)](./rejectprotectionspaceandcontinue%28with%29.md)
  Rejects the currently supplied protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/cancel(_:))*