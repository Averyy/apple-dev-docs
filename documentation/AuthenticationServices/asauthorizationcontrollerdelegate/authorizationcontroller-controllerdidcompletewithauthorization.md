# authorizationController(controller:didCompleteWithAuthorization:)

**Framework**: Authentication Services  
**Kind**: method

Tells the delegate when authorization completes successfully.

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
optional func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization authorization: ASAuthorization)
```

## Mentions

- [Supporting passkeys](supporting-passkeys.md)
- [Supporting Security Key Authentication Using Physical Keys](supporting-security-key-authentication-using-physical-keys.md)

## Parameters

- `controller`: The controller that performs the authorization request.
- `authorization`: An encapsulation of the successful authorization.

## See Also

- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:).md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [class ASAuthorization](asauthorization.md)
  The encapsulation of a successful authorization by a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:))*