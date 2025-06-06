# network

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A string, suitable for display, that describes the payment network for the card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var network: PKPaymentNetwork? { get }
```

#### Discussion

To protect the user’s privacy, the `network` property is `nil` until after the user authenticates the purchase. You can safely access this property as soon as the system calls your delegate’s [`paymentAuthorizationController(_:didAuthorizePayment:completion:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:completion:).md) method.

## See Also

- [var type: PKPaymentMethodType](pkpaymentmethod/type.md)
  A value that represents the card’s type.
- [enum PKPaymentMethodType](pkpaymentmethodtype.md)
  The type of cards available in Apple Pay.
- [var displayName: String?](pkpaymentmethod/displayname.md)
  A string, suitable for display, that describes the card.
- [var billingAddress: CNContact?](pkpaymentmethod/billingaddress.md)
  The user’s billing address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmethod/network)*