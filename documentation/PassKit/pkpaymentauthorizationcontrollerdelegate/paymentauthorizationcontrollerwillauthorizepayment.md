# paymentAuthorizationControllerWillAuthorizePayment(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user is authorizing the payment request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@MainActor
optional func paymentAuthorizationControllerWillAuthorizePayment(_ controller: PKPaymentAuthorizationController)
```

#### Discussion

This method is called before the payment request is authorized but after the user has authenticated by using either a passcode, Touch ID, or Face ID.

## Parameters

- `controller`: The payment authorization controller.

## See Also

- [func paymentAuthorizationController(PKPaymentAuthorizationController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didrequestmerchantsessionupdate:).md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:handler:).md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:completion:).md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationControllerDidFinish(PKPaymentAuthorizationController)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:).md)
  Tells the delegate that payment authorization has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerwillauthorizepayment(_:))*