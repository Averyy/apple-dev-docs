# ASAuthorizationCustomMethod

**Framework**: Authentication Services  
**Kind**: struct

The custom authorization method.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
struct ASAuthorizationCustomMethod
```

#### Discussion

Use [`ASAuthorizationCustomMethod`](asauthorizationcustommethod.md) to specify a type of custom sign-in in tvOS, like enabling the user to sign in manually or by restoring a purchase.

## Topics

### Creating the Structure
- [init(rawValue: String)](asauthorizationcustommethod/init(rawvalue:).md)
  Initializes the object with a custom authorization method.
### Getting the Properties
- [static let videoSubscriberAccount: ASAuthorizationCustomMethod](asauthorizationcustommethod/videosubscriberaccount.md)
  A type of authorization that uses a TV provider account to sign in.
- [static let restorePurchase: ASAuthorizationCustomMethod](asauthorizationcustommethod/restorepurchase.md)
  A type of authorization that restores an in-app purchase to sign in.
- [static let other: ASAuthorizationCustomMethod](asauthorizationcustommethod/other.md)
  A type of authorization that uses a custom sign-in method.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var customAuthorizationMethods: [ASAuthorizationCustomMethod]](asauthorizationcontroller/customauthorizationmethods.md)
  An array of custom authorization methods for the user to choose.
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](asauthorizationcontrollerdelegate/authorizationcontroller(_:didcompletewithcustommethod:).md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcustommethod)*