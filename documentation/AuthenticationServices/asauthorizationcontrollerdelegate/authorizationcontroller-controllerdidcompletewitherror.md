# authorizationController(controller:didCompleteWithError:)

**Framework**: Authentication Services  
**Kind**: method

Tells the delegate when authorization fails, and provides an error explaining why.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
optional func authorizationController(controller: ASAuthorizationController, didCompleteWithError error: any Error)
```

## Mentions

- [Supporting passkeys](supporting-passkeys.md)
- [Supporting Security Key Authentication Using Physical Keys](supporting-security-key-authentication-using-physical-keys.md)

## Parameters

- `controller`: The controller that performs the authorization attempt.
- `error`: An error that explains the failure using one of the codes in  .

## See Also

- [let ASAuthorizationErrorDomain: String](asauthorizationerrordomain.md)
  The domain of authorization errors.
- [struct ASAuthorizationError](asauthorizationerror-swift.struct.md)
  Errors that can occur during authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewitherror:))*