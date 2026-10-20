# authorizationController(controller:didCompleteWithAuthorization:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

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
optional func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization authorization: ASAuthorization)
```

```objc
- (void) authorizationController:(ASAuthorizationController *) controller didCompleteWithAuthorization:(ASAuthorization *) authorization;
```

## Mentions

- [Supporting passkeys](../supporting-passkeys.md)
- [Supporting Security Key Authentication Using Physical Keys](../supporting-security-key-authentication-using-physical-keys.md)

## Parameters

- `controller`: The controller that performs the authorization request.
- `authorization`: An encapsulation of the successful authorization.

## See Also

### Handling Successful Authorization
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](./authorizationcontroller%28_,didcompletewithcustommethod%29.md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [class ASAuthorization](../asauthorization.md)
  The encapsulation of a successful authorization by a controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerdelegate/authorizationcontroller(controller:didcompletewithauthorization:))*