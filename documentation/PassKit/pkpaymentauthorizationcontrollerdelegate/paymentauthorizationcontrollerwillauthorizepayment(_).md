# paymentAuthorizationControllerWillAuthorizePayment(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) paymentAuthorizationControllerWillAuthorizePayment:(PKPaymentAuthorizationController *) controller;
```

## Discussion

This method is called before the payment request is authorized but after the user has authenticated by using either a passcode, Touch ID, or Face ID.

## Parameters

- `controller`: The payment authorization controller.

## See Also

### Handling user’s payment authorization
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](./paymentauthorizationcontroller%28_,didrequestmerchantsessionupdate%29.md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](./paymentauthorizationcontroller%28_,didauthorizepayment,handler%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](./paymentauthorizationcontroller%28_,didauthorizepayment,completion%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationControllerDidFinish(PKPaymentAuthorizationController)](./paymentauthorizationcontrollerdidfinish%28_%29.md)
  Tells the delegate that payment authorization has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerwillauthorizepayment(_:))*