# PKPaymentOrderDetails

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

Optional metadata with payment order details for the placed order.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class PKPaymentOrderDetails
```

#### Overview

The device only retreives metadata if the status is `PKPaymentAuthorizationStatusSuccess`.

## Topics

### Creating payment order details
- [init(orderTypeIdentifier: String, orderIdentifier: String, webServiceURL: URL, authenticationToken: String)](pkpaymentorderdetails/init(ordertypeidentifier:orderidentifier:webserviceurl:authenticationtoken:).md)
  Initializes a payment order details object with the identifier, web service URL, and authentication token you provide.
### Identifying and authenticating the order
- [var authenticationToken: String](pkpaymentorderdetails/authenticationtoken.md)
  The authentification token supplied to your web service.
- [var orderIdentifier: String](pkpaymentorderdetails/orderidentifier.md)
  A unique order identifier scoped to your order type identifier.
- [var orderTypeIdentifier: String](pkpaymentorderdetails/ordertypeidentifier.md)
  An identifier for the order type associated with the order.
- [var webServiceURL: URL](pkpaymentorderdetails/webserviceurl.md)
  The URL for your web service.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKPaymentAuthorizationResult](pkpaymentauthorizationresult.md)
  An object that reports the status code and errors for a payment authorization request.
- [class PKPaymentAuthorizationController](pkpaymentauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
- [class PKPaymentAuthorizationViewController](pkpaymentauthorizationviewcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
- [class PKPayment](pkpayment.md)
  Represents the result of authorizing a payment request and contains payment information, encrypted in the payment token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentorderdetails)*