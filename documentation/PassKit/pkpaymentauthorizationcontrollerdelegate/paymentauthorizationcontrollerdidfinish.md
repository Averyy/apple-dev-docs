# paymentAuthorizationControllerDidFinish(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Required**: Yes

Tells the delegate that payment authorization has completed.

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
func paymentAuthorizationControllerDidFinish(_ controller: PKPaymentAuthorizationController)
```

#### Discussion

Use this method to dismiss the payment authorization controller and update any other app state.

When the user authorizes a payment request, this method is called after the user is shown the status from the [`paymentAuthorizationController(_:didAuthorizePayment:completion:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:completion:).md) method’s completion block. When the user cancels without authorizing the payment request, only `paymentAuthorizationControllerDidFinish:` is called.

## Parameters

- `controller`: The payment authorization controller.

## See Also

- [func paymentAuthorizationController(PKPaymentAuthorizationController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didrequestmerchantsessionupdate:).md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationControllerWillAuthorizePayment(PKPaymentAuthorizationController)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerwillauthorizepayment(_:).md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:handler:).md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:completion:).md)
  Tells the delegate that the user authorized the payment request, and asks for a result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:))*