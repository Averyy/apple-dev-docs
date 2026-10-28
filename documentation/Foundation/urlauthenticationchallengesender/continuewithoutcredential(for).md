# continueWithoutCredential(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Attempt to continue downloading a request without providing a credential for a given challenge.

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
func continueWithoutCredential(for challenge: URLAuthenticationChallenge)
```

```objc
- (void) continueWithoutCredentialForAuthenticationChallenge:(NSURLAuthenticationChallenge *) challenge;
```

## Discussion

This method has no effect if it is called with an authentication challenge that has already been handled.

## Parameters

- `challenge`: A challenge without authentication credentials.

## See Also

### Protocol Methods
- [func cancel(URLAuthenticationChallenge)](./cancel%28_%29.md)
  Cancels a given authentication challenge.
- [func use(URLCredential, for: URLAuthenticationChallenge)](./use%28_,for%29.md)
  Attempt to use a given credential for a given authentication challenge.
- [func performDefaultHandling(for: URLAuthenticationChallenge)](./performdefaulthandling%28for%29.md)
  Causes the system-provided default behavior to be used.
- [func rejectProtectionSpaceAndContinue(with: URLAuthenticationChallenge)](./rejectprotectionspaceandcontinue%28with%29.md)
  Rejects the currently supplied protection space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallengesender/continuewithoutcredential(for:))*