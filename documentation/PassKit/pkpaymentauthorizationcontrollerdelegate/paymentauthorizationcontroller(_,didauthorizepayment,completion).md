# paymentAuthorizationController(_:didAuthorizePayment:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user authorized the payment request, and asks for a result.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`paymentAuthorizationController(_:didAuthorizePayment:handler:)`](./paymentauthorizationcontroller%28_,didauthorizepayment,handler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS*

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didAuthorizePayment payment: PKPayment, completion: @escaping @Sendable (PKPaymentAuthorizationStatus) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didAuthorizePayment payment: PKPayment) async -> PKPaymentAuthorizationStatus
```

```objc
- (void) paymentAuthorizationController:(PKPaymentAuthorizationController *) controller didAuthorizePayment:(PKPayment *) payment completion:(void (^)(PKPaymentAuthorizationStatus status)) completion;
```

#### Discussion

This method is called after the payment request is authorized. You submit the payment information to your payment processor to authorize the transaction, and then call the completion block.

> **Note**:  The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](./paymentauthorizationcontrollerdidfinish%28_%29.md) until it has invoked the completion block.

## Parameters

- `controller`: The payment authorization controller.
- `payment`: The authorized payment. This object contains the payment token you need to submit to your payment processor, as well as the billing and shipping information required by the payment request.
- `completion`: The completion block to call with the result of authorizing the payment.

  This block takes the following parameters:

  - **`status`**: The authorization status for the payment. For values, see [`paymentAuthorizationControllerDidFinish(_:)`](./paymentauthorizationcontrollerdidfinish%28_%29.md).

## See Also

### Handling user’s payment authorization
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](./paymentauthorizationcontroller%28_,didrequestmerchantsessionupdate%29.md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationControllerWillAuthorizePayment(PKPaymentAuthorizationController)](./paymentauthorizationcontrollerwillauthorizepayment%28_%29.md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](./paymentauthorizationcontroller%28_,didauthorizepayment,handler%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationControllerDidFinish(PKPaymentAuthorizationController)](./paymentauthorizationcontrollerdidfinish%28_%29.md)
  Tells the delegate that payment authorization has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didauthorizepayment:completion:))*