# paymentAuthorizationController(_:didRequestMerchantSessionUpdate:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Requests an object that validates the identity of a merchant for a payment request.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didRequestMerchantSessionUpdate handler: @escaping (PKPaymentRequestMerchantSessionUpdate) -> Void)
```

```swift
@MainActor
optional func paymentAuthorizationControllerDidRequestMerchantSessionUpdate(controller: PKPaymentAuthorizationController) async -> PKPaymentRequestMerchantSessionUpdate
```

```objc
- (void) paymentAuthorizationController:(PKPaymentAuthorizationController *) controller didRequestMerchantSessionUpdate:(void (^)(PKPaymentRequestMerchantSessionUpdate *update)) handler;
```

## Parameters

- `controller`: The payment authorization controller.
- `handler`: The completion handler to call with the updated merchant session.

## See Also

### Handling user’s payment authorization
- [func paymentAuthorizationControllerWillAuthorizePayment(PKPaymentAuthorizationController)](./paymentauthorizationcontrollerwillauthorizepayment%28_%29.md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](./paymentauthorizationcontroller%28_,didauthorizepayment,handler%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](./paymentauthorizationcontroller%28_,didauthorizepayment,completion%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationControllerDidFinish(PKPaymentAuthorizationController)](./paymentauthorizationcontrollerdidfinish%28_%29.md)
  Tells the delegate that payment authorization has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didrequestmerchantsessionupdate:))*