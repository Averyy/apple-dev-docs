# authorizationController(_:didCompleteWithCustomMethod:)

**Framework**: Authentication Services  
**Kind**: method

Informs the delegate when authorization completes, and specifies the custom method the user selected.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
@MainActor
optional func authorizationController(_ controller: ASAuthorizationController, didCompleteWithCustomMethod method: ASAuthorizationCustomMethod)
```

## Parameters

- `controller`: The controller performing the authorization attempt.
- `method`: The custom method the user selected. For a list of custom methods, see   .

## See Also

- [var customAuthorizationMethods: [ASAuthorizationCustomMethod]](asauthorizationcontroller/customauthorizationmethods.md)
  An array of custom authorization methods for the user to choose.
- [struct ASAuthorizationCustomMethod](asauthorizationcustommethod.md)
  The custom authorization method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:))*