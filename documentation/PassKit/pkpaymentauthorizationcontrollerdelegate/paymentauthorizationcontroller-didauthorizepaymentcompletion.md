# paymentAuthorizationController(_:didAuthorizePayment:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user authorized the payment request, and asks for a result.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didAuthorizePayment payment: PKPayment) async -> PKPaymentAuthorizationStatus
```

#### Discussion

This method is called after the payment request is authorized. You submit the payment information to your payment processor to authorize the transaction, and then call the completion block.

> **Note**:  The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:).md) until it has invoked the completion block.

 The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:).md) until it has invoked the completion block.

## Parameters

- `controller`: The payment authorization controller.
- `payment`: The authorized payment. This object contains the payment token you need to submit to your payment processor, as well as the billing and shipping information required by the payment request.
- `completion`: This block takes the following parameters:

## See Also

- [func paymentAuthorizationController(PKPaymentAuthorizationController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didrequestmerchantsessionupdate:).md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationControllerWillAuthorizePayment(PKPaymentAuthorizationController)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerwillauthorizepayment(_:).md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:handler:).md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationControllerDidFinish(PKPaymentAuthorizationController)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:).md)
  Tells the delegate that payment authorization has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:completion:))*