# customAuthorizationMethods

**Framework**: Authentication Services  
**Kind**: property

An array of custom authorization methods for the user to choose.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
var customAuthorizationMethods: [ASAuthorizationCustomMethod] { get set }
```

#### Discussion

Custom authorization methods provide a unified interface for signing in to apps, while allowing the developer to customize the login experience. For example, use [`other`](asauthorizationcustommethod/other.md) to display a username and password field, a web-based flow, or a custom user interface.

## See Also

- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:).md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [struct ASAuthorizationCustomMethod](asauthorizationcustommethod.md)
  The custom authorization method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/customauthorizationmethods)*