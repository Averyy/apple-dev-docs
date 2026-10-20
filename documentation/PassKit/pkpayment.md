# PKPayment

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

Represents the result of authorizing a payment request and contains payment information, encrypted in the payment token.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKPayment
```

```objc
@interface PKPayment : NSObject
```

## Topics

### Working with the payment token
- [var token: PKPaymentToken](./pkpayment/token.md)
  The encrypted payment information.
- [class PKPaymentToken](./pkpaymenttoken.md)
  Contains the user’s payment credentials.
### Working with billing and shipping information
- [var billingContact: PKContact?](./pkpayment/billingcontact.md)
  The user-selected billing address for this transaction.
- [var shippingContact: PKContact?](./pkpayment/shippingcontact.md)
  The user-selected shipping address for this transaction.
- [var shippingMethod: PKShippingMethod?](./pkpayment/shippingmethod.md)
  The user-selected shipping method for this transaction.
- [class PKContact](./pkcontact.md)
  An object that encapsulates contact information needed for billing and shipping.
- [class PKShippingMethod](./pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.
### Deprecated
- [var billingAddress: ABRecord?](./pkpayment/billingaddress.md)
  The user-selected billing address for this transaction.
- [var shippingAddress: ABRecord?](./pkpayment/shippingaddress.md)
  The user-selected shipping address for this transaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Payment sheet interactions and authorization
- [class PKPaymentAuthorizationResult](./pkpaymentauthorizationresult.md)
  An object that reports the status code and errors for a payment authorization request.
- [class PKPaymentOrderDetails](./pkpaymentorderdetails.md)
  Optional metadata with payment order details for the placed order.
- [class PKPaymentAuthorizationController](./pkpaymentauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
- [class PKPaymentAuthorizationViewController](./pkpaymentauthorizationviewcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpayment)*